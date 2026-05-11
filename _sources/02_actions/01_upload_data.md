# Uploading Data to Yoda (SURF)

## Overview

This guide explains how to upload and organize your data in Yoda for the Delta Enigma project. Our Yoda environment is hosted by SURF, the Dutch national research infrastructure.

## Prerequisites

- SURF account
- Access to [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/) (request via [Data Steward](../03_general_info/02_data_stewards))

## Data Structure

Your data must follow the Delta Enigma folder structure:

```
Research/
└── research-uu/
    └── raw-data/
        └── WP3/
            └── zandmotor/
                └── camera/
                    └── camera1/
                        └── 2025/
                            └── 147_may.26/
                                └── 1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera1.raw-data.jpg
```
More information can be found [here](../01_data_guidelines/03_folder_structure).

## Upload Methods

There are two primary methods for uploading data to Yoda. Choose the most appropriate method based on your needs:

### Method 1: Web Portal (Recommended for small files)

Best for:
- Small files (<1GB)
- Occasional uploads
- Quick access needs
- Users who prefer graphical interfaces

#### Steps:
1. Access the Portal
   - Navigate to [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/)
   - Login with your SURF account
   - Select "Delta Enigma" research group

2. Upload Files
   - Navigate to your target directory
   - Click "Upload" or use drag-and-drop
   - Wait for completion
   - Verify upload success

3. Add Metadata
   - Select uploaded files
   - Click "Add Metadata"
   - Fill required fields

### Method 2: WebDAV (Recommended for large files)

Best for:
- Large files (>1GB)
- Bulk uploads
- Automated transfers
- Integration with scripts

#### Steps:
1. Generate Data Access Password
   - Log into the [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/)
   - Go to your user settings
   - Create a data access password
   - Save this password securely - you'll need it for WebDAV access

2. WebDAV Connection Setup
   ```
   URL: https://deltaenigma-data.irods.surfsara.nl/
   Username: Your SURF username
   Password: Your data access password (NOT your SURF password)
   ```

2. Choose Your WebDAV Client:

   a. File Explorer (Windows)
   - Open File Explorer
   - Right-click "This PC"
   - Select "Map network drive"
   - Enter WebDAV URL
   - Check "Connect using different credentials"
   - Enter SURF credentials

   b. Finder (macOS)
   - Click "Go" in menu bar
   - Select "Connect to Server"
   - Enter WebDAV URL
   - Enter SURF credentials

3. Upload Files
   - Navigate to target directory
   - Copy/paste or drag-and-drop files
 