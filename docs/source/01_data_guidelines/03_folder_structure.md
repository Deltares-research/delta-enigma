# Folder Structure Delta Enigma Data Platform

# iRODS Data Platform Folder Structure Documentation

## Overview
This document outlines the standardized folder structure for sensor data storage within the iRODS data platform. The structure is designed to organize research data hierarchically, from institutional level down to individual data files.

### Complete Path Example
```
Research/
└── research-uu/
    └── WP3/
        └── project-x/
            └── zandmotor/
                └── raw-data/
                    └── camera/
                        └── camera1/
                            └── 2024/
                                └── 147_May.26/
                                    └── 1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera1.raw-data.jpg
```

## Hierarchy Levels

### 1. Root Level
- `Research/`: Top-level directory for all research data

### 2. Institution Level
- `research-uu/`: Institution-specific directory
  - Format: `research-{institution-code}`

### 3. Work Package Level
- `WP3/`: Work package identifier
  - Format: `WP{number}`

### 4. Project Level
- `project-x/`: Specific project directory
  - Format: `project-{project-name}`

### 5. Location Level
- `zandmotor/`: Geographic or site-specific location
  - Format: `{location-name}`

### 6. Data Classification
- Distinguishes between different data processing stages
- Available categories:
  - `raw-data/`: Unprocessed data directly from sensors
  - `processed-data/`: Data that has undergone processing or analysis
  - `published-data/`: Final, published versions of datasets

### 7. Sensor Type
- `camera/`: Type of sensor or data collection device
  - Format: `{sensor-type}`

### 8. Device Instance
- `camera1/`: Specific device identifier
  - Format: `{sensor-type}{number}`

### 9. Temporal Organization
- `2025/`: Year
- `147_may.26/`: Day folder
  - Format: `{day-of-year}_{month}.{day}`

## File Naming Convention

Pattern: `{unix_timestamp}.{human_readable_datetime}.{location}.{device_id}.{data_type}.{extension}`

Example: `1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera1.raw-data.jpg`

Components:
- `1716706803`: Unix timestamp for unique identification and sorting
- `Sun.May.26_07_00_03.UTC.2024`: Human-readable date/time (DayOfWeek.Month.Day_Hour_Minute_Second.UTC.Year)
- `zandmotor`: Location identifier (lowercase)
- `camera1`: Device identifier (sensor type + number)
- `raw-data`: Processing stage (options: raw-data, processed-data, published-data)
- `jpg`: File extension (lowercase)

## Notes

- All folder names should use lowercase letters and hyphens for spaces
- Date folders should include both numerical day of year and calendar date
- File names should be descriptive while following the established pattern
- Each level of the hierarchy serves a specific organizational purpose

## Python Implementation

Below is a Python script that generates standardized file paths following this structure:

```python
import datetime
import os

def metadata2filepath(
    timestamp: int,
    institution: str,
    work_package: str,
    project: str,
    location: str,
    sensor_type: str,
    sensor_number: int,
    data_type: str
):
    """
    Generate a standardized filepath from metadata.
    
    Args:
        timestamp (int): Unix timestamp
        institution (str): Institution code (e.g., 'uu')
        work_package (str): Work package identifier (e.g., 'WP3')
        project (str): Project name (e.g., 'project-x')
        location (str): Location name (e.g., 'zandmotor')
        sensor_type (str): Type of sensor (e.g., 'camera')
        sensor_number (int): Sensor identifier number (e.g., 1)
        data_type (str): Type of data (e.g., 'raw-data')
    
    Returns:
        str: Complete filepath
    """
    # Convert timestamp to datetime
    dt = datetime.datetime.fromtimestamp(timestamp)
    
    # Generate filename components
    filename_parts = [
        str(timestamp),
        dt.strftime('%a.%b.%d_%H_%M_%S.UTC.%Y'),
        location,
        f'{sensor_type}{sensor_number}',
        data_type,
        'jpg'
    ]
    filename = '.'.join(filename_parts)
    
    # Generate path components
    path_parts = [
        'Research',
        f'research-{institution}',
        work_package,
        project,
        location,
        data_type,
        sensor_type,
        f'{sensor_type}{sensor_number}',
        dt.strftime('%Y'),
        dt.strftime('%j_%b.%d')
    ]
    
    # Join path and filename
    return os.path.join(*path_parts, filename)

# Example usage
if __name__ == "__main__":
    # Example: Generate path for a specific timestamp
    filepath = metadata2filepath(
        timestamp=1716706803,  # May 26, 2024 07:00:03 UTC
        institution='uu',
        work_package='WP3',
        project='project-x',
        location='zandmotor',
        sensor_type='camera',
        sensor_number=1,
        data_type='raw-data'
    )
    print(f"Generated filepath:\n{filepath}")
```