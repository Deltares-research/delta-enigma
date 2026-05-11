# Example Metadata per Sensor

## Overview

To ensure consistency and harmonization across institutes using the same types of instruments, this page provides standardized metadata examples for different sensor types. Multiple institutes often collect similar data (e.g., UAV imagery, water quality measurements) but may use different directory naming conventions and metadata field structures. The examples below establish common standards that should be followed by all institutes.

```{admonition} Harmonization Goal
:class: note

The goal of these standardized examples is to ensure that data from the same sensor types across different institutes follows consistent naming conventions, directory structures, and metadata formats. This facilitates data discovery, comparison, and integration across the Delta Enigma project.
```

## Sensor Overview

This page provides a standardized metadata example for UAV imagery data collection. The example below establishes common standards that should be followed by all institutes working with drone-based sensors.

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