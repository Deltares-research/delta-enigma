# Yoda iRODS Data Download Scripts

This folder contains Python scripts for connecting to and downloading data from the Delta-Enigma iRODS server using the iBridges library.

## Prerequisites

### 1. Install Required Packages

```bash
pip install python-irodsclient ibridges
```

### 2. Configure iRODS Connection

You need to have a valid iRODS environment configuration. The scripts will prompt you for credentials if not configured.

## Available Scripts

### 1. `check_paths.py` - Explore Available Data

Use this script to explore what data is available in your iRODS storage.

```bash
python check_paths.py
```

**What it does:**
- Connects to iRODS server
- Shows your session information (username, zone, home directory)
- Lists files and collections in your home directory
- Searches for common file types (CSV, TXT, JSON, ZIP)
- Provides usage examples

**Example output:**
```
🚀 iRODS Path Helper
==============================
🔗 Connecting to iRODS...

📋 Session Information:
   Username: jelle.vanmiltenburg@deltares.nl
   Zone: deltaenigma
   Home: /deltaenigma/home
   Server version: (4, 2, 12)

📁 Contents of home directory (/deltaenigma/home):
   Collections:
     📁 research-deltares
     📁 research-nioz
     📁 research-tno
     📁 research-tud
     📁 research-ut
     📁 research-uu
     📁 research-wur
     📁 vault-uu
```

### 2. `download_single_file.py` - Download Data Files

Use this script to download specific files or entire collections from iRODS.

#### Download a Single File

```bash
# Download by relative path (from home directory)
python download_single_file.py research-deltares/WP2/raw-data/ADCP/ADCP1/2025/Apr.14/WP.ADCP_fast_bot.022

# Download by absolute path
python download_single_file.py /deltaenigma/home/research-deltares/WP2/raw-data/ADCP/ADCP1/2025/Apr.14/WP.ADCP_fast_bot.022

# Download to specific directory
python download_single_file.py filename.csv /path/to/custom/directory
```

#### Download Entire Collections

```bash
# Download all files from a collection
python download_single_file.py --search research-deltares/WP2

# Download all files from a subcollection
python download_single_file.py --search research-deltares/WP2/raw-data/ADCP

# Download to specific directory
python download_single_file.py --search research-deltares/WP2 /path/to/custom/directory
```

**What it does:**
- Connects to iRODS server
- Downloads files to `./downloads/` folder by default
- Shows file information (size, checksum, metadata)
- Verifies download was successful
- Handles both single files and entire collections

**Example output:**
```
🚀 Delta-Enigma File Download
========================================
🔗 Connecting to iRODS...
   Username: jelle.vanmiltenburg@deltares.nl
   Zone: deltaenigma
   Home: /deltaenigma/home
📁 Download directory: /Users/jellevanmiltenburg/git/delta-enigma/yoda-scripts/downloads
🎯 Target file: /deltaenigma/home/research-deltares/WP2/raw-data/ADCP/ADCP1/2025/Apr.14/WP.ADCP_fast_bot.022
📄 Found data object: WP.ADCP_fast_bot.022
   Size: 13964112 bytes
   Checksum: sha2:rIMPK58XiyRpmvS3XuRwP6KYN2Kqjb5CpgY1ItqQJpY=
📥 Downloading file...
100%|████████████████████████████████████████████████████████████████████| 13.3M/13.3M [00:01<00:00, 10.9MB/s]
✅ Download successful!
   Local path: /Users/jellevanmiltenburg/git/delta-enigma/yoda-scripts/downloads/WP.ADCP_fast_bot.022
   Size: 13964112 bytes
```

### 3. `upload_single_file.py` - Upload Data Files

Use this script to upload files to iRODS.

```bash
# Upload a file to default collection
python upload_single_file.py my_data.csv

# Upload to specific collection
python upload_single_file.py my_data.csv delta_enigma_data

# Upload with custom metadata
python upload_single_file.py sensor_data.txt sensor_collection
```

### 4. `upload_file_example.py` - Comprehensive Upload Example

A detailed example showing the full upload workflow including metadata and verification.

```bash
python upload_file_example.py
```

### 5. `simple_irods_connection.py` - Direct iRODS Connection

A simple script for testing direct iRODS connection without iBridges.

```bash
python simple_irods_connection.py
```

## Data Structure

The Delta-Enigma project organizes data in the following structure:

```
/deltaenigma/home/
├── research-deltares/          # Deltares research data
│   ├── WP1/                   # Work Package 1
│   ├── WP2/                   # Work Package 2
│   │   ├── raw-data/          # Raw sensor data
│   │   │   ├── ADCP/          # Acoustic Doppler Current Profiler
│   │   │   ├── CTD/           # Conductivity, Temperature, Depth
│   │   │   └── ...
│   │   └── processed-data/    # Processed data
│   └── WP3/                   # Work Package 3
├── research-nioz/             # NIOZ research data
├── research-tno/              # TNO research data
├── research-tud/              # TU Delft research data
├── research-ut/               # University of Twente data
├── research-uu/               # Utrecht University data
├── research-wur/              # Wageningen University data
└── vault-uu/                  # Utrecht University vault
```

## Common Use Cases

### 1. Download ADCP Data

```bash
# Download specific ADCP file
python download_single_file.py research-deltares/WP2/raw-data/ADCP/ADCP1/2025/Apr.14/WP.ADCP_fast_bot.022

# Download all ADCP data from a specific date
python download_single_file.py --search research-deltares/WP2/raw-data/ADCP/ADCP1/2025/Apr.14
```

### 2. Download All WP2 Data

```bash
# Download entire WP2 collection
python download_single_file.py --search research-deltares/WP2
```

### 3. Download Processed Data

```bash
# Download processed data
python download_single_file.py --search research-deltares/WP2/processed-data
```

### 4. Explore Available Data

```bash
# See what's available
python check_paths.py

# Then download specific files based on what you find
python download_single_file.py [path_to_file]
```

## File Locations

- **Downloads**: Files are downloaded to `./downloads/` folder by default
- **Uploads**: Files are uploaded to your home directory in iRODS
- **Logs**: Check terminal output for detailed information

## Troubleshooting

### Connection Issues

1. **Authentication failed**: Check your username and password
2. **Network error**: Verify you can reach the iRODS server
3. **Zone issues**: Make sure you're using the correct zone (`deltaenigma`)

### Download Issues

1. **File not found**: Use `check_paths.py` to verify the file path
2. **Permission denied**: Check if you have read access to the file
3. **Disk space**: Ensure you have enough space in the downloads folder

### Common Commands

```bash
# Check what's available
python check_paths.py

# Download a specific file
python download_single_file.py [file_path]

# Download entire collection
python download_single_file.py --search [collection_path]

# Upload a file
python upload_single_file.py [local_file] [irods_collection]
```

## Support

For issues with:
- **iRODS connection**: Contact your system administrator
- **Script functionality**: Check the error messages and try the troubleshooting steps above
- **Data access**: Contact the Delta-Enigma project team

## Version Information

- **iBridges**: Latest version
- **Python**: 3.11+
- **iRODS**: 4.2.12
- **Server**: deltaenigma-data.irods.surfsara.nl 