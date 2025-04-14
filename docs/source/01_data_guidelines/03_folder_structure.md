# Folder Structure 

## Overview
This document outlines the standardized folder structure for sensor data storage within the iRODS data platform. The structure is designed to organize research data hierarchically, from institutional level down to individual data files, ensuring consistent and clear organization across all research projects.

## Interactive Path Generator

Use our interactive tool to generate standardized file paths and folder structures for your data:

```{raw} html
<div style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif; line-height: 1.6;">
    <h2>Delta Enigma Path Generator</h2>
    <p>Use this tool to generate standardized file paths and folder structures for your data.</p>

    <form id="pathForm" style="margin-bottom: 20px;">
        <div style="margin-bottom: 15px;">
            <label for="institution" style="display: block; margin-bottom: 5px; font-weight: bold;">Institution code:</label>
            <input type="text" id="institution" value="uu" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="workPackage" style="display: block; margin-bottom: 5px; font-weight: bold;">Work package:</label>
            <input type="text" id="workPackage" value="WP3" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="project" style="display: block; margin-bottom: 5px; font-weight: bold;">Project name:</label>
            <input type="text" id="project" value="project-x" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="location" style="display: block; margin-bottom: 5px; font-weight: bold;">Location:</label>
            <input type="text" id="location" value="zandmotor" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="sensorType" style="display: block; margin-bottom: 5px; font-weight: bold;">Sensor type:</label>
            <input type="text" id="sensorType" value="camera" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="sensorNumber" style="display: block; margin-bottom: 5px; font-weight: bold;">Sensor number:</label>
            <input type="number" id="sensorNumber" value="1" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="dataType" style="display: block; margin-bottom: 5px; font-weight: bold;">Data type:</label>
            <select id="dataType" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
                <option value="raw-data">raw-data</option>
                <option value="processed-data">processed-data</option>
                <option value="published-data">published-data</option>
            </select>
        </div>

        <div style="margin-bottom: 15px;">
            <label for="extension" style="display: block; margin-bottom: 5px; font-weight: bold;">File extension:</label>
            <input type="text" id="extension" value="jpg" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <div style="margin-bottom: 15px;">
            <label for="date" style="display: block; margin-bottom: 5px; font-weight: bold;">Date:</label>
            <input type="date" id="date" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
        </div>

        <button type="submit" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; font-size: 16px;">Generate Path</button>
    </form>

    <div id="result" style="margin-top: 20px; padding: 15px; background-color: #f5f5f5; border-radius: 4px; white-space: pre-wrap; display: none;">
        <h3>Generated Path Information</h3>
        <div id="pathOutput"></div>
    </div>

    <script>
        // Set default date to today
        document.getElementById('date').valueAsDate = new Date();

        document.getElementById('pathForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const institution = document.getElementById('institution').value;
            const workPackage = document.getElementById('workPackage').value;
            const project = document.getElementById('project').value;
            const location = document.getElementById('location').value;
            const sensorType = document.getElementById('sensorType').value;
            const sensorNumber = document.getElementById('sensorNumber').value;
            const dataType = document.getElementById('dataType').value;
            const extension = document.getElementById('extension').value;
            const date = new Date(document.getElementById('date').value);

            // Format date components
            const month = date.toLocaleString('default', { month: 'short' });
            const day = date.getDate();
            const year = date.getFullYear();

            // Generate path components
            const pathParts = [
                'Research',
                `research-${institution}`,
                workPackage,
                project,
                location,
                dataType,
                sensorType,
                `${sensorType}${sensorNumber}`,
                year.toString(),
                `${month}.${day}`
            ];

            // Generate filename components
            const filenameParts = [
                `${month}.${day}.${year}`,
                location,
                `${sensorType}${sensorNumber}`,
                dataType,
                extension
            ];

            // Create full path and filename
            const filepath = pathParts.join('/');
            const filename = filenameParts.join('.');
            const completePath = `${filepath}/${filename}`;

            // Display results
            const resultDiv = document.getElementById('result');
            const pathOutput = document.getElementById('pathOutput');
            pathOutput.innerHTML = `Full path: ${filepath}\nFilename: ${filename}\nComplete path: ${completePath}`;
            resultDiv.style.display = 'block';
        });
    </script>
</div>
```

## Folder Structure Details

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

### Hierarchy Levels

1. **Root Level**
   - `Research/`: Top-level directory for all research data

2. **Institution Level**
   - `research-uu/`: Institution-specific directory
   - Format: `research-{institution-code}`

3. **Work Package Level**
   - `WP3/`: Work package identifier
   - Format: `WP{number}`

4. **Project Level**
   - `project-x/`: Specific project directory
   - Format: `{project-name}`

5. **Location Level**
   - `zandmotor/`: Geographic or site-specific location
   - Format: `{location-name}`

6. **Data Classification**
   - Distinguishes between different data processing stages
   - Available categories:
     - `raw-data/`: Unprocessed data directly from sensors
     - `processed-data/`: Data that has undergone processing or analysis
     - `published-data/`: Final, published versions of datasets

7. **Sensor Type**
   - `camera/`: Type of sensor or data collection device
   - Format: `{sensor-type}`

8. **Device Instance**
   - `camera1/`: Specific device identifier
   - Format: `{sensor-type}{number}`

9. **Temporal Organization**
   - `2024/`: Year
   - `147_May.26/`: Day folder
   - Format: `{day_of_year}_{month}.{day}`

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

## Implementation Options

### Web Tool
The interactive web tool (shown above) provides the easiest way to generate paths and filenames. It's ideal for:
- Quick path generation
- Interactive exploration of the structure
- Immediate feedback on generated paths

### Python Script
For programmatic or command-line usage, a Python script is available:

1. Download: [generate_path.py](generate_path.py)
2. Run in interactive mode:
   ```bash
   python3 generate_path.py --interactive
   ```
3. Follow the prompts to enter your data

Features:
- Interactive prompts with sensible defaults
- Date validation
- Option to create directory structure
- Both interactive and non-interactive modes
- Clear output of generated paths and filenames

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