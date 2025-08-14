#!/usr/bin/env python3
"""
Simple iRODS connection for Delta-Enigma
"""

import getpass
from irods.session import iRODSSession

def connect_to_delta_enigma():
    """Connect to Delta-Enigma iRODS server"""
    
    # Server configuration
    host = "deltaenigma-data.irods.surfsara.nl"
    port = 1247
    zone = "deltaenigma"
    
    # Get credentials
    user = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    
    print(f"\n🔗 Connecting to {host}:{port}")
    print(f"   User: {user}")
    print(f"   Zone: {zone}")
    
    try:
        # Create session
        session = iRODSSession(
            host=host,
            port=port,
            user=user,
            password=password,
            zone=zone
        )
        
        print("✅ Successfully connected!")
        
        # Test connection by accessing home directory
        home_path = f"/{zone}/home/{user}"
        try:
            home_collection = session.collections.get(home_path)
            print(f"   Home directory: {home_path}")
            
            # List contents
            files = list(home_collection.data_objects)
            collections = list(home_collection.subcollections)
            
            print(f"   Files: {len(files)}")
            print(f"   Collections: {len(collections)}")
            
            if files:
                print("   Sample files:")
                for f in files[:3]:
                    print(f"     - {f.name} ({f.size} bytes)")
                    
        except Exception as e:
            print(f"   Warning: Could not access home directory: {e}")
        
        return session
        
    except Exception as e:
        print(f"❌ Connection failed: {e}")
        return None

if __name__ == "__main__":
    print("🚀 Delta-Enigma iRODS Connection")
    print("=" * 40)
    
    session = connect_to_delta_enigma()
    
    if session:
        print("\n🎉 Connection successful!")
        print("You can now use the session object.")
    else:
        print("\n❌ Connection failed.") 