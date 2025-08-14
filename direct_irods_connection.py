#!/usr/bin/env python3
"""
Direct iRODS connection script for Yoda
"""

import getpass
from irods.session import iRODSSession
from irods.exception import NetworkException, AuthenticationException

def connect_to_yoda():
    """Connect to Yoda iRODS server using direct iRODS client"""
    
    # Yoda server configuration
    host = "yoda.uu.nl"
    port = 1247
    
    # Get user credentials
    user = input("Enter your Yoda username: ")
    password = getpass.getpass("Enter your Yoda password: ")
    zone = input("Enter your zone (default: yoda): ") or "yoda"
    
    print(f"\n🔗 Attempting to connect to {host}:{port}")
    print(f"   User: {user}")
    print(f"   Zone: {zone}")
    
    try:
        # Create iRODS session
        session = iRODSSession(
            host=host,
            port=port,
            user=user,
            password=password,
            zone=zone
        )
        
        print("✅ Successfully connected to Yoda iRODS!")
        
        # Test the connection by accessing home directory
        home_path = f"/{zone}/home/{user}"
        try:
            home_collection = session.collections.get(home_path)
            print(f"   Home directory: {home_path}")
            
            # List contents of home directory
            data_objects = list(home_collection.data_objects)
            subcollections = list(home_collection.subcollections)
            
            print(f"   Files: {len(data_objects)}")
            print(f"   Subcollections: {len(subcollections)}")
            
            if data_objects:
                print("   Sample files:")
                for obj in data_objects[:3]:
                    print(f"     - {obj.name} ({obj.size} bytes)")
                    
            if subcollections:
                print("   Sample subcollections:")
                for coll in subcollections[:3]:
                    print(f"     - {coll.name}")
                    
        except Exception as e:
            print(f"   Warning: Could not access home directory: {e}")
        
        return session
        
    except AuthenticationException as e:
        print(f"❌ Authentication failed: {e}")
        print("   Please check your username, password, and zone")
        return None
        
    except NetworkException as e:
        print(f"❌ Network error: {e}")
        print("   This might be due to:")
        print("   - Network connectivity issues")
        print("   - Incorrect host/port settings")
        print("   - Server requiring different connection parameters")
        return None
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("   Please check your connection settings")
        return None

def test_session_operations(session):
    """Test basic session operations"""
    if not session:
        return
        
    print("\n🧪 Testing session operations...")
    
    try:
        # Get server version
        version = session.server_version
        print(f"   Server version: {version}")
        
        # List zones
        zones = session.zones
        print(f"   Available zones: {[zone.name for zone in zones]}")
        
        # Get current user info
        user = session.username
        zone = session.zone
        print(f"   Current user: {user}@{zone}")
        
    except Exception as e:
        print(f"   Warning: Could not test operations: {e}")

if __name__ == "__main__":
    print("🚀 Yoda iRODS Connection Test")
    print("=" * 40)
    
    session = connect_to_yoda()
    
    if session:
        test_session_operations(session)
        print("\n🎉 Connection test successful!")
        print("You can now use the session object for data operations.")
    else:
        print("\n❌ Connection test failed.")
        print("Please check your credentials and try again.") 