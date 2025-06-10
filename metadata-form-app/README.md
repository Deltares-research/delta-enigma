# Delta Enigma Metadata Generator

A web application for generating compliant metadata JSON files for the Delta Enigma project.

## Overview

This application provides a user-friendly interface for creating metadata JSON files that conform to the Delta Enigma metadata schema. It allows users to fill out a form with the required metadata fields and generates a properly formatted JSON file that can be downloaded and used with Delta Enigma datasets.

## Features

- Form-based interface for entering metadata
- Support for all required fields in the Delta Enigma metadata schema
- Dynamic array fields for multiple values
- JSON generation and validation
- Download functionality for the generated JSON

## How to Use

### Option 1: Open Directly in Browser

1. Open the `index.html` file in a web browser
2. Fill out the form with your dataset metadata
3. Click the "Generate JSON" button to create the JSON
4. Review the generated JSON in the output area
5. Click the "Download JSON" button to save the file
6. Use the "Reset Form" button to clear the form and start over

### Option 2: Run with Node.js Server

If you have Node.js installed, you can run the application using the included server:

#### Using Node directly:

1. Open a terminal in the project directory
2. Run `node server.js`
3. Open your browser and navigate to `http://localhost:3000`
4. The application will be served from the local server

#### Using npm:

1. Open a terminal in the project directory
2. Run `npm install` (first time only)
3. Run `npm start`
4. Open your browser and navigate to `http://localhost:3000`
5. The application will be served from the local server

## Required Fields

The following fields are required by the Delta Enigma metadata schema:

- Title
- Description
- Documentation
- Domain
- Topic Category
- Version
- Language
- Temporal Coverage (Start and End Dates)
- Geographical Coverage
- Acquisition Sensor
- Related Resource
- Creation Date
- Release Date
- Resource Type
- Creator
- Contact Point
- License Document
- Access Rights

## Development

This application is built with vanilla JavaScript, HTML, and CSS. The metadata schema is defined in `schema.js`.

To modify or extend the application:

1. Edit `schema.js` to update the metadata schema
2. Modify `script.js` to change the form generation or JSON creation logic
3. Update `styles.css` to change the appearance of the application

## Project Structure

```
metadata-form-app/
├── index.html         # Main HTML file
├── styles.css         # CSS styles
├── script.js          # Form generation and JSON creation logic
├── schema.js          # Metadata schema definition
├── server.js          # Simple Node.js server
├── 404.html           # 404 error page
├── package.json       # npm package configuration
└── README.md          # This file
```

## License

This project is licensed under the MIT License. 