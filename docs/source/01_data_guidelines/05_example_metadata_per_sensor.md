# Example Metadata per Sensor

## Overview

To ensure consistency and harmonization across institutes using the same types of instruments, this page provides standardized metadata examples for different sensor types. Multiple institutes often collect similar data (e.g., UAV imagery, water quality measurements) but may use different directory naming conventions and metadata field structures. The examples below establish common standards that should be followed by all institutes.

```{admonition} Harmonization Goal
:class: note

The goal of these standardized examples is to ensure that data from the same sensor types across different institutes follows consistent naming conventions, directory structures, and metadata formats. This facilitates data discovery, comparison, and integration across the Delta Enigma project.
```

## Sensor Overview

Click on any sensor type below to jump to its detailed metadata example and directory structure:

- [**UAV Imagery**](#uav-imagery) - Drone-based RGB/multispectral cameras for aerial photography and mapping
- [**Water Quality Sensors**](#water-quality-sensors) - Multi-parameter probes for continuous aquatic monitoring
- [**Acoustic Sensors (Hydrophones)**](#acoustic-sensors-hydrophones) - Underwater sound recording equipment for marine monitoring
- [**Satellite/Remote Sensing Data**](#satellite-remote-sensing-data) - Orbital imagery for large-scale environmental observation
- [**LiDAR Data**](#lidar-data) - Airborne laser scanning for high-precision topographic mapping

---

(uav-imagery)=
## UAV Imagery

### Directory Structure
```
Research/
└── research-{institution}/
    └── WP{1-5}/
        └── {location}/
            ├── raw-data/
            │   └── camera/
            │       └── camera1/
            │           └── 2024/
            │               └── May.26/
            ├── processed-data/
            │   └── camera/
            │       └── camera1/
            │           └── 2024/
            │               └── May.26/
            └── published-data/
                └── camera/
                    └── camera1/
                        └── 2024/
                            └── May.26/
```

### Metadata Example
```json
{
  "Title": "UAV RGB Imagery - [Location] - [Date]",
  "Description": [
    "High-resolution RGB imagery collected using DJI Phantom 4 Pro UAV platform for [specific research purpose].",
    "Flight parameters: altitude 50m AGL, forward overlap 80%, side overlap 60%, grid flight pattern.",
    "Camera specifications: 1-inch CMOS sensor, 20 MP resolution, 24mm equivalent focal length.",
    "Weather conditions during flight: wind speed <5 m/s, cloud cover <20%, visibility >5 km.",
    "Ground control points used with RTK GPS for georeferencing (accuracy ±5cm).",
    "Data includes raw JPEG images and processed GeoTIFF orthomosaics.",
    "File naming convention: timestamp.date.location.camera1.raw-data.jpg.",
    "Total dataset size approximately [X] GB covering [X] hectares."
  ],
  "Creator": [
    {
      "Name": {
        "Given_Name": "[First Name]",
        "Family_Name": "[Last Name]"
      },
      "Affiliation": [
        {
          "Affiliation_Name": "[Institute Name]"
        }
      ]
    }
  ],
  "Work_Package": "[WP1/WP2/WP3/WP4/WP5]",
  "Temporal_Coverage": {
    "Start_Date": "YYYY-MM-DD",
    "End_Date": "YYYY-MM-DD"
  },
  "Geographical_Coverage": [
    {
      "geoLocationBox": {
        "westBoundLongitude": 5.5000,
        "eastBoundLongitude": 5.5678,
        "southBoundLatitude": 52.1000,
        "northBoundLatitude": 52.1234
      },
      "Description_Spatial": "[Site name and description]",
      "Reference_System": "WGS84"
    }
  ],
  "Acquisition_Sensor": "UAV RGB Camera",
  "Domain": "[Select appropriate domain]",
  "Resource_Type": "Dataset",
  "Keyword": ["[relevant", "keywords]"]
}
```

### Required Fields
- **Flight parameters**: altitude, overlap percentages, flight pattern
- **Camera specifications**: model, resolution, lens specifications
- **Weather conditions**: wind speed, cloud cover, visibility
- **Ground control points**: coordinates and accuracy if used

(water-quality-sensors)=
## Water Quality Sensors

### Directory Structure
```
Research/
└── research-{institution}/
    └── WP{1-5}/
        └── {location}/
            ├── raw-data/
            │   └── water-quality-probe/
            │       └── probe1/
            │           └── 2024/
            │               └── May.26/
            ├── processed-data/
            │   └── water-quality-probe/
            │       └── probe1/
            │           └── 2024/
            │               └── May.26/
            └── published-data/
                └── water-quality-probe/
                    └── probe1/
                        └── 2024/
                            └── May.26/
```

### Metadata Example
```json
{
  "Title": "Water Quality Monitoring - [Site Name] - [Deployment Period]",
  "Description": [
    "Continuous water quality measurements collected using multi-parameter probe [Model Name] deployed at [site description] for monitoring aquatic ecosystem health.",
    "Sensor deployed at 1.0m depth in water column (total water depth 2.5m) using fixed mooring system.",
    "Parameters measured: water temperature (°C, accuracy ±0.1°C), pH (pH units, accuracy ±0.1), dissolved oxygen (mg/L, accuracy ±0.2 mg/L), turbidity (NTU, accuracy ±2% or ±0.3 NTU).",
    "Data logging interval: 15 minutes.",
    "Sensor calibrated on [date] using certified reference standards.",
    "Monthly maintenance performed including sensor cleaning and data download.",
    "Quality control includes automated flagging of out-of-range values and manual validation of suspect data.",
    "Data exported as CSV files with timestamp in UTC.",
    "File naming convention: timestamp.date.location.probe1.raw-data.csv.",
    "Total deployment duration: [X months]."
  ],
  "Creator": [
    {
      "Name": {
        "Given_Name": "[First Name]",
        "Family_Name": "[Last Name]"
      },
      "Affiliation": [
        {
          "Affiliation_Name": "[Institute Name]"
        }
      ]
    }
  ],
  "Work_Package": "[WP1/WP2/WP3/WP4/WP5]",
  "Temporal_Coverage": {
    "Start_Date": "YYYY-MM-DD",
    "End_Date": "YYYY-MM-DD"
  },
  "Geographical_Coverage": [
    {
      "geoLocationBox": {
        "westBoundLongitude": 5.5678,
        "eastBoundLongitude": 5.5678,
        "southBoundLatitude": 52.1234,
        "northBoundLatitude": 52.1234
      },
      "Description_Spatial": "[Site name and detailed location description]",
      "Reference_System": "WGS84"
    }
  ],
  "Acquisition_Sensor": "Multi-parameter Water Quality Probe",
  "Domain": "[Select appropriate domain]",
  "Resource_Type": "Dataset",
  "Keyword": ["[relevant", "keywords]"]
}
```

### Required Fields
- **Sensor specifications**: model, serial number, measurement ranges
- **Calibration information**: dates, standards used, certificates
- **Deployment details**: depth, mounting method, maintenance schedule
- **Quality control**: flags for out-of-range values, maintenance events

(acoustic-sensors-hydrophones)=
## Acoustic Sensors (Hydrophones)

### Directory Structure
```
Research/
└── research-{institution}/
    └── WP{1-5}/
        └── {location}/
            ├── raw-data/
            │   └── hydrophone/
            │       └── hydrophone1/
            │           └── 2024/
            │               └── May.26/
            ├── processed-data/
            │   └── hydrophone/
            │       └── hydrophone1/
            │           └── 2024/
            │               └── May.26/
            └── published-data/
                └── hydrophone/
                    └── hydrophone1/
                        └── 2024/
                            └── May.26/
```

### Metadata Example
```json
{
  "Title": "Underwater Acoustic Monitoring - [Site Name] - [Deployment Period]",
  "Description": [
    "Continuous underwater acoustic recordings collected using hydrophone [Model Name] for monitoring [marine life/anthropogenic noise] at [site description].",
    "Hydrophone deployed at 10m depth in 15m water column using bottom-mounted mooring system.",
    "Technical specifications: frequency range 10 Hz - 100 kHz, sensitivity -164 dB re 1V/μPa, dynamic range 120 dB.",
    "Recording parameters: sampling rate 250 kHz, duty cycle 10 minutes every hour, file duration 10 minutes per recording.",
    "Data stored as uncompressed WAV files with UTC timestamps.",
    "Deployment includes environmental data logger recording water temperature and current speed.",
    "Quality control includes spectral analysis for noise contamination and manual validation of detection events.",
    "Calibration performed using reference tone generator before and after deployment.",
    "File naming convention: timestamp.date.location.hydrophone1.raw-data.wav.",
    "Total data volume approximately [X] TB."
  ],
  "Creator": [
    {
      "Name": {
        "Given_Name": "[First Name]",
        "Family_Name": "[Last Name]"
      },
      "Affiliation": [
        {
          "Affiliation_Name": "[Institute Name]"
        }
      ]
    }
  ],
  "Work_Package": "[WP1/WP2/WP3/WP4/WP5]",
  "Temporal_Coverage": {
    "Start_Date": "YYYY-MM-DD",
    "End_Date": "YYYY-MM-DD"
  },
  "Geographical_Coverage": [
    {
      "geoLocationBox": {
        "westBoundLongitude": 5.5678,
        "eastBoundLongitude": 5.5678,
        "southBoundLatitude": 52.1234,
        "northBoundLatitude": 52.1234
      },
      "Description_Spatial": "[Site name and detailed location description including water depth]",
      "Reference_System": "WGS84"
    }
  ],
  "Acquisition_Sensor": "Underwater Hydrophone",
  "Domain": "[Select appropriate domain]",
  "Resource_Type": "Dataset",
  "Keyword": ["[relevant", "keywords]"]
}
```

### Required Fields
- **Hydrophone specifications**: sensitivity, frequency response, calibration
- **Recording parameters**: sampling rate, bit depth, duty cycle
- **Deployment configuration**: mooring type, depth, orientation
- **Environmental conditions**: water temperature, salinity, current speed

(satellite-remote-sensing-data)=
## Satellite/Remote Sensing Data

### Directory Structure
```
Research/
└── research-{institution}/
    └── WP{1-5}/
        └── {location}/
            ├── raw-data/
            │   └── satellite/
            │       └── sentinel2/
            │           └── 2024/
            │               └── May.26/
            ├── processed-data/
            │   └── satellite/
            │       └── sentinel2/
            │           └── 2024/
            │               └── May.26/
            └── published-data/
                └── satellite/
                    └── sentinel2/
                        └── 2024/
                            └── May.26/
```

### Metadata Example
```json
{
  "Title": "Satellite Imagery - [Sensor] - [Location] - [Date]",
  "Description": [
    "Satellite remote sensing data from Sentinel-2 MSI (Multi-Spectral Instrument) for [application purpose] covering [area description].",
    "Data acquired by Sentinel-2A/2B satellites, provided by ESA Copernicus program.",
    "Processing level: Level 1C (top-of-atmosphere reflectance, orthorectified).",
    "Spatial resolution: 10m (visible and NIR bands: B02-Blue 490nm, B03-Green 560nm, B04-Red 665nm, B08-NIR 842nm), 20m (red edge and SWIR bands), 60m (atmospheric correction bands).",
    "Scene quality: cloud coverage 5%, geometric accuracy <12.5m, radiometric uncertainty <5%.",
    "Data provided as GeoTIFF format in UTM/WGS84 coordinate system.",
    "File naming convention: timestamp.date.location.sentinel2.raw-data.tif.",
    "Total file size approximately [X] GB.",
    "Suitable for vegetation analysis, land cover classification, and change detection studies."
  ],
  "Creator": [
    {
      "Name": {
        "Given_Name": "[First Name]",
        "Family_Name": "[Last Name]"
      },
      "Affiliation": [
        {
          "Affiliation_Name": "[Institute Name]"
        }
      ]
    }
  ],
  "Work_Package": "[WP1/WP2/WP3/WP4/WP5]",
  "Temporal_Coverage": {
    "Start_Date": "YYYY-MM-DD",
    "End_Date": "YYYY-MM-DD"
  },
  "Geographical_Coverage": [
    {
      "geoLocationBox": {
        "westBoundLongitude": 4.0000,
        "eastBoundLongitude": 6.0000,
        "southBoundLatitude": 51.5000,
        "northBoundLatitude": 52.5000
      },
      "Description_Spatial": "[Area name and detailed geographic description]",
      "Reference_System": "WGS84"
    }
  ],
  "Acquisition_Sensor": "Sentinel-2 MSI",
  "Domain": "[Select appropriate domain]",
  "Resource_Type": "Dataset",
  "Keyword": ["[relevant", "keywords]"]
}
```

### Required Fields
- **Satellite/sensor specifications**: platform, sensor type, spectral characteristics
- **Processing level**: raw, atmospherically corrected, analysis-ready
- **Quality indicators**: cloud coverage, geometric accuracy, radiometric quality
- **Coordinate system**: projection, datum, spatial resolution

(lidar-data)=
## LiDAR Data

### Directory Structure
```
Research/
└── research-{institution}/
    └── WP{1-5}/
        └── {location}/
            ├── raw-data/
            │   └── lidar/
            │       └── lidar1/
            │           └── 2024/
            │               └── May.26/
            ├── processed-data/
            │   └── lidar/
            │       └── lidar1/
            │           └── 2024/
            │               └── May.26/
            └── published-data/
                └── lidar/
                    └── lidar1/
                        └── 2024/
                            └── May.26/
```

### Metadata Example
```json
{
  "Title": "LiDAR Point Cloud - [Area] - [Date]",
  "Description": [
    "Airborne LiDAR point cloud data collected using [Scanner Model] for [topographic mapping/vegetation analysis] at [site description].",
    "Flight parameters: altitude 1000m AGL, flight speed 75 m/s, grid flight pattern with 30% overlap between flight lines.",
    "Scanner specifications: pulse rate 400 kHz, scan frequency 100 Hz, beam divergence 0.25 mrad, wavelength 1064 nm, maximum range 3000m.",
    "Point density achieved: 10 points/m² (first and last returns).",
    "Accuracy assessment using ground control points: horizontal accuracy 0.15m (1σ), vertical accuracy 0.10m (1σ).",
    "Data processing includes noise filtering, ground classification, and vegetation height derivation.",
    "Output files in LAS 1.4 format with point classifications (ground, vegetation, buildings, water).",
    "Coordinate system: WGS84/UTM Zone 31N.",
    "File naming convention: timestamp.date.location.lidar1.raw-data.las.",
    "Total point count approximately [X] million points covering [X] km².",
    "GPS/IMU trajectory data included for quality assessment."
  ],
  "Creator": [
    {
      "Name": {
        "Given_Name": "[First Name]",
        "Family_Name": "[Last Name]"
      },
      "Affiliation": [
        {
          "Affiliation_Name": "[Institute Name]"
        }
      ]
    }
  ],
  "Work_Package": "[WP1/WP2/WP3/WP4/WP5]",
  "Temporal_Coverage": {
    "Start_Date": "YYYY-MM-DD",
    "End_Date": "YYYY-MM-DD"
  },
  "Geographical_Coverage": [
    {
      "geoLocationBox": {
        "westBoundLongitude": 5.5000,
        "eastBoundLongitude": 5.6000,
        "southBoundLatitude": 52.1000,
        "northBoundLatitude": 52.2000
      },
      "Description_Spatial": "[Area name and detailed topographic description]",
      "Reference_System": "WGS84"
    }
  ],
  "Acquisition_Sensor": "Airborne LiDAR Scanner",
  "Domain": "[Select appropriate domain]",
  "Resource_Type": "Dataset",
  "Keyword": ["[relevant", "keywords]"]
}
```

### Required Fields
- **Scanner specifications**: model, wavelength, pulse rate, accuracy
- **Flight parameters**: altitude, speed, overlap, point density
- **Coordinate system**: datum, projection, vertical reference
- **Quality metrics**: accuracy assessments, density statistics

## Implementation Guidelines

### File Naming Conventions

All sensor data files should follow these naming patterns:

- **Date format**: YYYY-MM-DD (ISO 8601)
- **Location**: Use standardized site names or coordinates
- **Sensor identifier**: Use standardized sensor codes
- **Version**: Use semantic versioning (v1.0, v1.1, etc.)

Example: `2024-03-15_ijsselmeer_uav-rgb_v1.0`

### Metadata Requirements

Each dataset must include comprehensive metadata following the Delta Enigma schema:
1. **Complete Description field**: Include all technical specifications, processing details, quality metrics, and methodological information
2. **Accurate temporal and spatial coverage**: Precise dates and geographic boundaries
3. **Proper sensor identification**: Use standardized Acquisition_Sensor values
4. **Appropriate domain classification**: Select correct Domain category for your field of study
5. **Comprehensive keywords**: Include relevant terms for discoverability

### Cross-Institute Coordination

Before deploying new sensor types:
1. Check existing examples on this page
2. Coordinate with other institutes using similar sensors
3. Propose updates to this page via your data steward
4. Ensure compliance with the [Metadata Standards](02_metadata_standards) and follow the [Add Metadata](../02_actions/02_add_metadata) procedures in Yoda

## Contributing New Examples

If you're working with a sensor type not listed here:

1. Contact your [data steward](../index) for guidance
2. Develop example following the format shown above
3. Include complete directory structure and metadata examples
4. Test the format with actual data collection
5. Submit for inclusion in this handbook

```{admonition} Need Help?
:class: tip

If you need assistance adapting these examples to your specific use case or sensor configuration, contact your designated data steward for support.
``` 