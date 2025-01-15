# Folder Structure Delta Enigma Data Platform

## Overview
This document describes the standardized folder structure implemented in the iRODS data platform for organizing research sensor data. The structure is designed to facilitate efficient data management, easy retrieval, and clear organization of sensor data from various sources.

## Base Structure
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

## Hierarchy Explanation

### Level 1: Research
- Top-level directory containing all research-related data
- Separates research data from other potential platform contents

### Level 2: Institution Identifier
- Format: `research-[institution-code]`
- Example: `research-uu` (University Utrecht)
- Enables multi-institutional collaboration while maintaining data separation
- Facilitates access control and data ownership

### Level 3: Data Category
- Example: `raw-data`
- Distinguishes between different data processing stages
- Available categories:
  - raw-data
  - processed-data
  - published-data

### Level 4: Work Package
- Format: `WP[number]`
- Example: `WP3`
- Organizes data by project components or research phases
- Enables clear separation of different project aspects

### Level 5: Location
- Example: `Zandmotor`
- Identifies specific research sites or study areas
- Allows for geographical organization of data

### Level 6: Sensor Type
- Example: `camera`
- Categorizes data by measurement instrument
- Facilitates organization of different data collection methods

### Level 7: Specific Sensor
- Format: `[sensor-type][number]`
- Example: `camera1`
- Identifies individual sensors within a sensor type
- Enables tracking of data provenance

### Level 8: Year
- Format: `YYYY`
- Example: `2025`
- Organizes data chronologically
- Facilitates temporal data management

### Level 9: Date
- Format: `[day-of-year]_[month].[day]`
- Example: `147_may.26`
- Provides detailed temporal information
- Enables precise data retrieval

## Naming Conventions

### General Rules
1. Use lowercase for all folder names except where specified
2. Avoid spaces in folder names where possible
3. Use hyphens (-) instead of underscores (_) for word separation
4. Use consistent date formatting throughout

### Date Formatting
- Year: Four-digit format (YYYY)
- Day of year: Three-digit format (001-365)
- Month: Lowercase three-letter abbreviation
- Day: Two-digit format with period separator

### Data Type Options
The platform recognizes three specific data type categories:
- `raw-data`: Original, unprocessed data directly from sensors
- `processed-data`: Data that has undergone cleaning, calibration, or other processing steps
- `published-data`: Final, validated data ready for publication or sharing

### File Naming Convention
Files follow a standardized naming pattern that includes temporal and spatial metadata:

```
[timestamp].[day].[month].[day]_[HH]_[MM]_[SS].UTC.[YYYY].[location].[sensor_type][number].[data_type].[extension]
```

Components explanation:
- `timestamp`: Unix timestamp (e.g., 1716706803)
- `day`: Three-letter day abbreviation (e.g., Sun)
- `month`: Three-letter month abbreviation (e.g., May)
- `day`: Two-digit day of month (e.g., 26)
- `HH_MM_SS`: Time in 24-hour format with underscores
- `UTC`: Timezone indicator (always UTC)
- `YYYY`: Four-digit year
- `location`: Site identifier (e.g., zandmotor)
- `sensor_type[number]`: Sensor identifier (e.g., camera12)
- `data_type`: One of: raw, processed, published
- `extension`: File extension (e.g., jpg)

Example filename:
```
1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera12.raw.jpg
```

## Best Practices

### Adding New Data
1. Verify the correct work package designation
2. Use existing sensor type folders when available
3. Create new sensor type folders only when necessary
4. Maintain consistent naming conventions
5. Verify date formatting before creating new folders

### Folder Management
1. Don't create empty folders
2. Document any deviations from the standard structure
3. Maintain consistent capitalization
4. Use standard date formats
5. Include necessary metadata at each level

## Example Use Cases

### Adding New Sensor Data
```
Research/
└── research-uu/
    └── Raw data/
        └── WP3/
            └── Zandmotor/
                ├── camera/
                │   └── camera1/
                │       └── 2025/
                │           └── 147_may.26/
                └── lidar/
                    └── lidar1/
                        └── 2025/
                            └── 147_may.26/
```

### Multiple Institutions
```
Research/
├── research-uu/
└── research-tudelft/
```

## Automated Path Generation

### Python Script
The following Python script can be used to automatically generate paths and filenames according to this folder structure:

```python
import datetime
import os

def generate_irods_path(
    timestamp: int,
    institution: str = 'uu',
    work_package: int = 3,
    location: str = 'zandmotor',
    sensor_type: str = 'camera',
    sensor_number: int = 1,
    data_type: str = 'raw-data'
) -> str:
    """
    Generate an iRODS file path based on metadata.
    
    Args:
        timestamp (int): Unix timestamp for the data
        institution (str): Institution code (default: 'uu')
        work_package (int): Work package number (default: 3)
        location (str): Location name (default: 'zandmotor')
        sensor_type (str): Type of sensor (default: 'camera')
        sensor_number (int): Sensor identifier (default: 1)
        data_type (str): Type of data (default: 'raw')
    
    Returns:
        str: Complete file path following iRODS structure
    """
    # Convert timestamp to datetime
    dt = datetime.datetime.fromtimestamp(timestamp)
    
    # Format the date components
    year = dt.strftime('%Y')
    day_of_year = dt.strftime('%j')
    month_day = dt.strftime('%b.%d').lower()
    date_folder = f'{day_of_year}_{month_day}'
    
    # Construct path components
    path_components = [
        'Research',
        f'research-{institution}',
        f'{data_type}',  # Using hyphenated format
        f'WP{work_package}',
        location.lower(),
        sensor_type.lower(),
        f'{sensor_type.lower()}{sensor_number}',
        year,
        date_folder
    ]
    
    # Join path components
    return os.path.join(*path_components)

def generate_irods_filename(
    timestamp: int,
    location: str = 'zandmotor',
    sensor_type: str = 'camera',
    sensor_number: int = 1,
    data_type: str = 'raw',
    file_extension: str = 'jpg'
) -> str:
    """
    Generate a filename for iRODS data following the convention.
    """
    dt = datetime.datetime.fromtimestamp(timestamp)
    
    # Format datetime components
    timestamp_str = str(timestamp)
    datetime_str = dt.strftime('%a.%b.%d_%H_%M_%S.UTC.%Y')
    
    # Construct filename components
    filename_components = [
        timestamp_str,
        datetime_str,
        location.lower(),
        f'{sensor_type.lower()}{sensor_number}',
        data_type.lower(),
        file_extension
    ]
    
    # Join with dots
    return '.'.join(filename_components)

def generate_full_path(
    timestamp: int,
    institution: str = 'uu',
    work_package: int = 3,
    location: str = 'zandmotor',
    sensor_type: str = 'camera',
    sensor_number: int = 1,
    data_type: str = 'raw',
    file_extension: str = 'jpg'
) -> str:
    """
    Generate complete path including filename.
    """
    path = generate_irods_path(
        timestamp=timestamp,
        institution=institution,
        work_package=work_package,
        location=location,
        sensor_type=sensor_type,
        sensor_number=sensor_number,
        data_type=data_type
    )
    
    filename = generate_irods_filename(
        timestamp=timestamp,
        location=location,
        sensor_type=sensor_type,
        sensor_number=sensor_number,
        data_type=data_type,
        file_extension=file_extension
    )
    
    return os.path.join(path, filename)

```

### Example Usage
```python
# Example timestamp (May 26, 2024 07:00:03 UTC)
timestamp = 1716706803

# Generate full path
full_path = generate_full_path(
    timestamp=timestamp,
    sensor_number=12,
    data_type='raw'
)

print(f"Generated path:\n{full_path}")
```

This will generate a path like:
```
Research/research-uu/Raw data/WP3/zandmotor/camera/camera12/2024/147_may.26/1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera12.raw.jpg
```

## Notes
- This structure is designed to be scalable
- Additional levels can be added as needed
- Maintain consistency across all new additions
- Document any structural changes