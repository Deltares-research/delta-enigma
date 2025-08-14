#!/usr/bin/env python3
"""
Simple file upload script for Delta-Enigma
"""

from pathlib import Path
from ibridges.interactive import interactive_auth
from ibridges import IrodsPath, upload

def upload_file(local_file_path, irods_collection="uploads", metadata=None):
    """
    Upload a single file to iRODS
    
    Args:
        local_file_path (str): Path to the local file to upload
        irods_collection (str): Collection name in iRODS (default: "uploads")
        metadata (dict): Optional metadata to add to the file
    """
    
    # Convert to Path object
    local_path = Path(local_file_path)
    
    if not local_path.exists():
        print(f"❌ File not found: {local_path}")
        return None
    
    print(f"📁 Uploading: {local_path}")
    print(f"   Size: {local_path.stat().st_size} bytes")
    
    # Create iRODS session
    print("🔗 Connecting to iRODS...")
    session = interactive_auth()
    
    # Set up iRODS path
    irods_path = IrodsPath(session, session.home, irods_collection)
    
    # Create collection if it doesn't exist
    if not irods_path.collection_exists():
        print(f"   Creating collection: {irods_path}")
        IrodsPath.create_collection(session, irods_path)
    
    # Upload the file
    print("📤 Uploading file...")
    changes = upload(session, local_path, irods_path, overwrite=True)
    
    # Handle the changes object properly
    if hasattr(changes, 'print_summary'):
        changes.print_summary()
    else:
        print(f"   Upload completed")
        if isinstance(changes, dict):
            print(f"   Files processed: {len(changes)}")
    
    # Get the uploaded file path
    uploaded_file = irods_path.joinpath(local_path.name)
    
    if uploaded_file.exists():
        print(f"✅ Upload successful!")
        print(f"   iRODS path: {uploaded_file}")
        print(f"   Size: {uploaded_file.size} bytes")
        print(f"   Checksum: {uploaded_file.checksum}")
        
        # Add metadata if provided
        if metadata:
            print("🏷️  Adding metadata...")
            try:
                for key, value in metadata.items():
                    uploaded_file.meta.add(key, value)
                    print(f"   {key}: {value}")
            except Exception as e:
                print(f"   Warning: Could not add metadata: {e}")
        
        return uploaded_file
    else:
        print("❌ Upload failed!")
        return None

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python upload_single_file.py <local_file_path> [collection_name]")
        print("Example: python upload_single_file.py my_data.csv delta_enigma_data")
        sys.exit(1)
    
    local_file = sys.argv[1]
    collection = sys.argv[2] if len(sys.argv) > 2 else "uploads"
    
    # Example metadata
    metadata = {
        "Project": "Delta-Enigma",
        "UploadDate": "2024-01-15",
        "UploadMethod": "iBridges Python"
    }
    
    print("🚀 Delta-Enigma File Upload")
    print("=" * 40)
    
    result = upload_file(local_file, collection, metadata)
    
    if result:
        print(f"\n🎉 File uploaded successfully to: {result}")
    else:
        print("\n❌ Upload failed!") 