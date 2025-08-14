#!/usr/bin/env python3
"""
iBridges file upload example
Based on the iBridges documentation
"""

from pathlib import Path
from ibridges.interactive import interactive_auth
from ibridges import IrodsPath, upload
from ibridges.util import obj_replicas

def create_test_file():
    """Create a test file to upload"""
    local_path = Path.home().joinpath("demofile.txt")
    
    # Create the file with some content
    with open(local_path, "w") as f:
        f.write("My content! Super important\n")
        f.write("This is a test file for Delta-Enigma upload.\n")
        f.write("Created with iBridges Python client.\n")
    
    print(f"✅ Created test file: {local_path}")
    return local_path

def upload_file_example():
    """Demonstrate file upload using iBridges"""
    
    # Step 1: Create iRODS session
    print("🔗 Creating iRODS session...")
    session = interactive_auth()
    
    print(f"   Username: {session.username}")
    print(f"   Zone: {session.zone}")
    print(f"   Home: {session.home}")
    print(f"   Server version: {session.server_version}")
    
    # Step 2: Create a test file
    print("\n📁 Creating test file...")
    local_path = create_test_file()
    
    # Step 3: Determine iRODS path for upload
    print("\n🎯 Setting up upload path...")
    irods_path = IrodsPath(session, session.home, "upload_test")
    
    # Create collection if it doesn't exist
    if not irods_path.collection_exists():
        print(f"   Creating collection: {irods_path}")
        coll = IrodsPath.create_collection(session, irods_path)
    else:
        print(f"   Collection already exists: {irods_path}")
    
    # Step 4: Dry run to see what would be uploaded
    print("\n🔍 Performing dry run...")
    from pprint import pprint
    ops = upload(session, local_path, irods_path, dry_run=True, overwrite=True)
    ops.print_summary()
    
    # Step 5: Actually upload the file
    print("\n📤 Uploading file...")
    changes = upload(session, local_path, irods_path, overwrite=True)
    changes.print_summary()
    
    # Step 6: Verify the upload
    print("\n✅ Verifying upload...")
    obj_path = irods_path.joinpath("demofile.txt")
    
    if obj_path.exists():
        print(f"   File uploaded successfully!")
        print(f"   Name: {obj_path.name}")
        print(f"   Path: {obj_path}")
        print(f"   Size: {obj_path.size} bytes")
        print(f"   Checksum: {obj_path.checksum}")
        
        # Show replicas
        obj = obj_path.dataobject
        replicas = obj_replicas(obj)
        print(f"   Replicas: {replicas}")
        
        # Read the content
        stream = obj.open('r')
        content = stream.read().decode()
        stream.close()
        print(f"   Content preview: {content[:100]}...")
        
    else:
        print("   ❌ Upload verification failed!")
    
    return session, obj_path

def add_metadata_example(session, obj_path):
    """Demonstrate adding metadata to the uploaded file"""
    print("\n🏷️  Adding metadata...")
    
    # Add some metadata
    obj_path.meta.add('Author', 'Delta-Enigma Team')
    obj_path.meta.add('Project', 'Delta-Enigma')
    obj_path.meta.add('UploadDate', '2024-01-15')
    obj_path.meta.add('FileType', 'text')
    
    print("   Added metadata:")
    for md in obj_path.meta:
        print(f"     {md.name}: {md.value}")
    
    # Set a specific metadata value (replaces existing)
    obj_path.meta.set("Status", "Uploaded")
    print(f"   Set Status to: {obj_path.meta.get('Status')}")

def search_example(session):
    """Demonstrate searching for files"""
    print("\n🔍 Searching for files...")
    
    from ibridges.search import search_data, MetaSearch
    
    # Search by metadata
    result = search_data(session, metadata=MetaSearch(key="Project", value="Delta-Enigma"))
    print(f"   Files with Project=Delta-Enigma: {len(result)}")
    for item in result:
        print(f"     - {item}")
    
    # Search by path pattern
    result = search_data(session, session.home, path_pattern="upload_test/%")
    print(f"   Files in upload_test collection: {len(result)}")
    for item in result:
        print(f"     - {item}")

if __name__ == "__main__":
    print("🚀 iBridges File Upload Example")
    print("=" * 50)
    
    try:
        # Upload the file
        session, obj_path = upload_file_example()
        
        # Add metadata
        add_metadata_example(session, obj_path)
        
        # Search for files
        search_example(session)
        
        print("\n🎉 Upload example completed successfully!")
        print(f"   File uploaded to: {obj_path}")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("Please check your iRODS connection and credentials.") 