# Folder Structure 

## Overview
This document outlines the standardized folder structure for sensor data storage within the iRODS data platform. The structure is designed to organize research data hierarchically, from work package level down to individual data files, ensuring consistent and clear organization across all research projects.

## Folder Structure Details

### Complete Path Example
```
Research/
└── WP3/
      └── zandmotor/
          └── raw-data/
              └── camera/
                  └── camera1/
                      └── 2024/
                          └── May.26/
                              └── May.26.2024.zandmotor.camera1.raw-data.jpg
```

### Hierarchy Levels

1. **Root Level**
   - `Research/`: Top-level directory for all research data

2. **Work Package Level**
   - `WP3/`: Work package identifier
   - Format: `WP{number}`

3. **Location Level**
   - `zandmotor/`: Geographic or site-specific location
   - Format: `{location-name}`

4. **Data Classification**
   - Distinguishes between different data processing stages
   - Available categories:
     - `raw-data/`: Unprocessed data directly from sensors
     - `processed-data/`: Data that has undergone processing or analysis
     - `published-data/`: Final, published versions of datasets

5. **Sensor Type**
   - `camera/`: Type of sensor or data collection device
   - Format: `{sensor-type}`

6. **Device Instance**
   - `camera1/`: Specific device identifier
   - Format: `{sensor-type}{number}`

7. **Temporal Organization**
   - `2024/`: Year
   - `May.26/`: Day folder
   - Format: `{month}.{day}`

## File Naming Convention

### Pattern
`{unix_timestamp}.{human_readable_datetime}.{location}.{device_id}.{data_type}.{extension}`

### Example
`1716706803.Sun.May.26_07_00_03.UTC.2024.zandmotor.camera1.raw-data.jpg`

### Components
- `1716706803`: Unix timestamp
- `Sun.May.26_07_00_03.UTC.2024`: Human readable date and time
- `zandmotor`: Location identifier (lowercase)
- `camera1`: Device identifier (sensor type + number)
- `raw-data`: Processing stage
- `jpg`: File extension (lowercase)

## Best Practices

1. **Folder Names**
   - Use lowercase letters
   - Use hyphens for spaces
   - Follow the hierarchical structure strictly

2. **File Names**
   - Include all required components
   - Use consistent formatting
   - Follow the established pattern

3. **Data Organization**
   - Keep raw data separate from processed data
   - Use appropriate data classification
   - Maintain consistent temporal organization

## Instrument-Specific Folder Structures

For some instruments, we work with a deviation from the standard folder structure described above. The instrument-specific structures are listed below.

### Metronome

For the Metronome, the folder structure has an additional experiment layer (e.g. `exp092/`) in between the location level and the data classification level. Sometimes there is also a pilot layer (e.g. `pilot2/`) in between the experiment layer and the data classification level.

Example:
```
Research/
└── research-wp5-process-studies/
    └── metronome/
        └── exp092/
            └── pilot2/
                └── processed_data/
                    └── orthophotos/
                        └── overhead_cameras/
                            └── Basemodel11/
                                └── Res25mm/
```
