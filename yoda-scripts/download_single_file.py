#!/usr/bin/env python3
"""
Simple file download script for Delta-Enigma
"""

from pathlib import Path
from ibridges.interactive import interactive_auth
from ibridges import IrodsPath, download

def download_file(irods_file_path, local_download_dir=None, metadata_filter=None):
    """
    Download a single file from iRODS
    
    Args:
        irods_file_path (str): Path to the file in iRODS (e.g., "/deltaenigma/home/username/file.txt")
        local_download_dir (str): Local directory to download to (default: /downloads)
        metadata_filter (dict): Optional metadata filter to find files
    """
    
    # Create iRODS session
    print("🔗 Connecting to iRODS...")
    session = interactive_auth()
    
    print(f"   Username: {session.username}")
    print(f"   Zone: {session.zone}")
    print(f"   Home: {session.home}")
    
    # Set up download directory
    if local_download_dir is None:
        # Use a downloads folder in the current project directory
        local_download_dir = Path.cwd() / "downloads"
    else:
        local_download_dir = Path(local_download_dir)
    
    local_download_dir.mkdir(exist_ok=True)
    print(f"📁 Download directory: {local_download_dir}")
    
    # Handle different input formats for iRODS path
    if irods_file_path.startswith('/'):
        # Absolute path
        irods_path = IrodsPath(session, irods_file_path)
    elif irods_file_path.startswith('~'):
        # Home-relative path
        irods_path = IrodsPath(session, irods_file_path)
    else:
        # Relative to home
        irods_path = IrodsPath(session, session.home, irods_file_path)
    
    print(f"🎯 Target file: {irods_path}")
    
    # Check if file exists
    if not irods_path.exists():
        print(f"❌ File not found: {irods_path}")
        return None
    
    if irods_path.dataobject_exists():
        print(f"📄 Found data object: {irods_path.name}")
        print(f"   Size: {irods_path.size} bytes")
        print(f"   Checksum: {irods_path.checksum}")
        
        # Show metadata if available
        try:
            metadata = irods_path.dataobject.metadata
            if metadata:
                print("   Metadata:")
                for md in metadata:
                    print(f"     {md.name}: {md.value}")
        except Exception as e:
            print(f"   No metadata available: {e}")
        
        # Download the file
        print("📥 Downloading file...")
        changes = download(session, irods_path, local_download_dir, overwrite=True)
        
        # Handle the changes object properly
        if hasattr(changes, 'print_summary'):
            changes.print_summary()
        else:
            print(f"   Download completed")
            if isinstance(changes, dict):
                print(f"   Files processed: {len(changes)}")
        
        # Verify download
        local_file = local_download_dir / irods_path.name
        if local_file.exists():
            print(f"✅ Download successful!")
            print(f"   Local path: {local_file}")
            print(f"   Size: {local_file.stat().st_size} bytes")
            return local_file
        else:
            print("❌ Download failed!")
            return None
            
    elif irods_path.collection_exists():
        print(f"📁 Found collection: {irods_path}")
        print("   Downloading entire collection...")
        
        # Download the collection
        changes = download(session, irods_path, local_download_dir, overwrite=True)
        
        # Handle the changes object properly
        if hasattr(changes, 'print_summary'):
            changes.print_summary()
        else:
            print(f"   Collection download completed")
            if isinstance(changes, dict):
                print(f"   Files processed: {len(changes)}")
        
        # Verify download
        local_dir = local_download_dir / irods_path.name
        if local_dir.exists():
            print(f"✅ Collection download successful!")
            print(f"   Local path: {local_dir}")
            return local_dir
        else:
            print("❌ Collection download failed!")
            return None
    else:
        print(f"❌ Path not found: {irods_path}")
        return None

def search_and_download(collection_path=None, metadata_filter=None, local_download_dir=None):
    """
    Search for files and download them
    
    Args:
        collection_path (str): Collection to search in (default: home directory)
        metadata_filter (dict): Metadata filter (e.g., {"Project": "Delta-Enigma"})
        local_download_dir (str): Local download directory
    """
    
    # Set up download directory
    if local_download_dir is None:
        local_download_dir = Path.cwd() / "downloads"
    else:
        local_download_dir = Path(local_download_dir)
    local_download_dir.mkdir(exist_ok=True)
    
    print("🔍 Searching for files...")
    session = interactive_auth()
    
    # Set up search parameters
    if collection_path is None:
        collection_path = session.home
    
    # Recursively find all files in the collection
    print(f"   Searching in: {collection_path}")
    all_files = []
    
    try:
        # Create IrodsPath for the collection
        collection_irods_path = IrodsPath(session, collection_path)
        
        if not collection_irods_path.exists():
            print(f"❌ Collection not found: {collection_path}")
            return []
        
        # Recursively find all files
        all_files = find_all_files_recursive(session, collection_irods_path)
        
        if not all_files:
            print("❌ No files found in collection")
            return []
        
        # Show overview of files found
        print(f"\n📋 Found {len(all_files)} files:")
        total_size = 0
        for i, file_path in enumerate(all_files, 1):
            size_mb = file_path.size / (1024 * 1024)
            total_size += file_path.size
            print(f"   {i:2d}. {file_path.name} ({size_mb:.1f} MB)")
        
        total_size_mb = total_size / (1024 * 1024)
        print(f"\n💾 Total size: {total_size_mb:.1f} MB")
        
        # Download each found file
        downloaded_files = []
        print(f"\n📥 Downloading to: {local_download_dir}")
        
        for i, file_path in enumerate(all_files, 1):
            local_file = local_download_dir / file_path.name
            
            # Check if file already exists
            if local_file.exists():
                local_size = local_file.stat().st_size
                if local_size == file_path.size:
                    print(f"   {i:2d}. ✅ {file_path.name} (already downloaded)")
                    downloaded_files.append(local_file)
                    continue
                else:
                    print(f"   {i:2d}. 🔄 {file_path.name} (updating)")
            else:
                print(f"   {i:2d}. 📥 {file_path.name}")
            
            # Download the file
            result = download_file_silent(str(file_path), local_download_dir, session)
            if result:
                downloaded_files.append(result)
        
        return downloaded_files
        
    except Exception as e:
        print(f"   Search error: {e}")
        return []

def find_all_files_recursive(session, collection_path):
    """
    Recursively find all files in a collection and its subcollections
    
    Args:
        session: iBridges session
        collection_path: IrodsPath object for the collection
    
    Returns:
        list: List of IrodsPath objects for all files found
    """
    all_files = []
    
    try:
        # Get the collection object
        collection = collection_path.collection
        
        # Find all data objects (files) in this collection
        for data_object in collection.data_objects:
            file_path = IrodsPath(session, data_object.path)
            all_files.append(file_path)
        
        # Recursively search subcollections
        for subcollection in collection.subcollections:
            sub_path = IrodsPath(session, subcollection.path)
            sub_files = find_all_files_recursive(session, sub_path)
            all_files.extend(sub_files)
            
    except Exception as e:
        print(f"     ❌ Error searching {collection_path}: {e}")
    
    return all_files

def download_file_silent(irods_file_path, local_download_dir, session):
    """
    Download a single file from iRODS (silent version)
    """
    try:
        # Handle different input formats for iRODS path
        if irods_file_path.startswith('/'):
            irods_path = IrodsPath(session, irods_file_path)
        elif irods_file_path.startswith('~'):
            irods_path = IrodsPath(session, irods_file_path)
        else:
            irods_path = IrodsPath(session, session.home, irods_file_path)
        
        if not irods_path.exists():
            return None
        
        if irods_path.dataobject_exists():
            # Download the file
            changes = download(session, irods_path, local_download_dir, overwrite=True)
            
            # Verify download
            local_file = local_download_dir / irods_path.name
            if local_file.exists():
                return local_file
                
        return None
        
    except Exception as e:
        return None

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python download_single_file.py <irods_file_path> [local_download_dir]")
        print("  python download_single_file.py --search [collection_path] [local_download_dir]")
        print("\nExamples:")
        print("  python download_single_file.py /deltaenigma/home/username/data.csv")
        print("  python download_single_file.py data.csv")
        print("  python download_single_file.py --search uploads")
        print("  python download_single_file.py --search research-deltares/WP2")
        print("\nNote: Files will be downloaded to ./downloads/ folder by default")
        sys.exit(1)
    
    print("🚀 Delta-Enigma File Download")
    print("=" * 40)
    
    if sys.argv[1] == "--search":
        # Search and download all files in a collection
        collection = sys.argv[2] if len(sys.argv) > 2 else None
        download_dir = sys.argv[3] if len(sys.argv) > 3 else None
        
        results = search_and_download(collection, None, download_dir)
        
        if results:
            print(f"\n🎉 Successfully processed {len(results)} files")
        else:
            print("\n❌ No files were downloaded")
        
    else:
        # Download a specific file
        irods_file = sys.argv[1]
        download_dir = sys.argv[2] if len(sys.argv) > 2 else None
        
        result = download_file(irods_file, download_dir)
        
        if result:
            print(f"\n🎉 File downloaded successfully to: {result}")
        else:
            print("\n❌ Download failed!") 