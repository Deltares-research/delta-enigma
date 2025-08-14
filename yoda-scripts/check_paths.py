#!/usr/bin/env python3
"""
Helper script to check iRODS paths and find files
"""

from ibridges.interactive import interactive_auth
from ibridges import IrodsPath
from ibridges.search import search_data

def check_session_info():
    """Show session information and available paths"""
    print("🔗 Connecting to iRODS...")
    session = interactive_auth()
    
    print("\n📋 Session Information:")
    print(f"   Username: {session.username}")
    print(f"   Zone: {session.zone}")
    print(f"   Home: {session.home}")
    print(f"   Server version: {session.server_version}")
    
    # Show home directory contents
    home_path = IrodsPath(session, session.home)
    print(f"\n📁 Contents of home directory ({session.home}):")
    
    try:
        # List files and collections using the collection object
        collection = home_path.collection
        files = list(collection.data_objects)
        if files:
            print("   Files:")
            for f in files[:10]:  # Show first 10 files
                print(f"     📄 {f.name} ({f.size} bytes)")
        else:
            print("   No files found")
        
        # List collections
        collections = list(collection.subcollections)
        if collections:
            print("   Collections:")
            for c in collections[:10]:  # Show first 10 collections
                print(f"     📁 {c.name}")
        else:
            print("   No collections found")
            
    except Exception as e:
        print(f"   Error listing contents: {e}")
    
    return session

def search_files(session, pattern=None):
    """Search for files with optional pattern"""
    print(f"\n🔍 Searching for files...")
    
    try:
        if pattern:
            print(f"   Pattern: {pattern}")
            # Use a simpler search approach
            results = search_data(session, session.home)
        else:
            results = search_data(session, session.home)
        
        print(f"   Found {len(results)} items")
        
        if results:
            print("   Files/Collections found:")
            for item in results[:20]:  # Show first 20 results
                try:
                    # Handle different return types from search_data
                    if isinstance(item, dict):
                        # If it's a dictionary, extract the path
                        if 'COLL_NAME' in item:
                            print(f"     📁 {item['COLL_NAME']}")
                        elif 'DATA_NAME' in item:
                            print(f"     📄 {item['DATA_NAME']} ({item.get('DATA_SIZE', 'unknown')} bytes)")
                        else:
                            print(f"     ❓ {item}")
                    elif hasattr(item, 'dataobject_exists'):
                        # If it's an IrodsPath object
                        if item.dataobject_exists():
                            print(f"     📄 {item} ({item.size} bytes)")
                        else:
                            print(f"     📁 {item}")
                    else:
                        print(f"     ❓ {item}")
                except Exception as e:
                    print(f"     ❓ {item} (error: {e})")
        
        return results
        
    except Exception as e:
        print(f"   Search error: {e}")
        return []

if __name__ == "__main__":
    print("🚀 iRODS Path Helper")
    print("=" * 30)
    
    session = check_session_info()
    
    # Search for all files
    print("\n🔍 Searching for files...")
    results = search_files(session)
    
    if results:
        # Count file types
        file_types = {}
        for item in results:
            try:
                if isinstance(item, dict) and 'DATA_NAME' in item:
                    name = str(item['DATA_NAME']).lower()
                    if name.endswith('.csv'):
                        file_types['CSV'] = file_types.get('CSV', 0) + 1
                    elif name.endswith('.txt'):
                        file_types['TXT'] = file_types.get('TXT', 0) + 1
                    elif name.endswith('.json'):
                        file_types['JSON'] = file_types.get('JSON', 0) + 1
                    elif name.endswith('.zip'):
                        file_types['ZIP'] = file_types.get('ZIP', 0) + 1
                elif hasattr(item, 'dataobject_exists') and item.dataobject_exists():
                    name = str(item.name).lower()
                    if name.endswith('.csv'):
                        file_types['CSV'] = file_types.get('CSV', 0) + 1
                    elif name.endswith('.txt'):
                        file_types['TXT'] = file_types.get('TXT', 0) + 1
                    elif name.endswith('.json'):
                        file_types['JSON'] = file_types.get('JSON', 0) + 1
                    elif name.endswith('.zip'):
                        file_types['ZIP'] = file_types.get('ZIP', 0) + 1
            except Exception as e:
                continue  # Skip items that cause errors
        
        if file_types:
            print("   File types found:")
            for file_type, count in file_types.items():
                print(f"     {file_type}: {count} files")
    
    print("\n💡 Usage examples:")
    print("   # Download a specific file:")
    print("   python download_single_file.py filename.csv")
    print("   python download_single_file.py /deltaenigma/home/username/filename.csv")
    print("   python download_single_file.py uploads/myfile.txt")
    print("\n   # Search and download:")
    print("   python download_single_file.py --search uploads")
    print("   python download_single_file.py --search-metadata Project Delta-Enigma")
    print("\n   # Files will be downloaded to ./downloads/ folder") 