# Processing Data

## Overview

This guide explains how to process and transform your data for the Delta Enigma project. It's important to understand that the Yoda platform serves as a data storage and management solution, not a computational environment.

## Key Principles

### Yoda Platform Limitations

The Yoda platform **does not provide computational resources** for data processing, transformation, or analysis. Yoda is designed for:
- Data storage and archival
- Metadata management  
- Data sharing and collaboration

### Processing Requirements

All data cleaning, transformation, and processing must be performed **outside** of the Yoda environment using:

- **Local computing resources** (your personal computer or workstation)
- **Institutional computing infrastructure** (university clusters, high-performance computing facilities)
- **Cloud computing platforms** (public clouds like AWS, Azure, Google Cloud, or private institutional clouds)

## Data Processing Workflow

### 1. Download Raw Data

- Access your raw data through the [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/)
- Download to your local or institutional computing environment
- Ensure you have adequate storage space for both raw and processed data

### 2. Process Data Locally or in the Cloud

Perform your data processing using appropriate tools and environments:

- **Data cleaning**: Remove outliers, handle missing values, quality control
- **Data transformation**: Format conversion, unit standardization, coordinate transformations

### 3. Prepare Refined Data for Publication

Only upload **refined but unaggregated data** back to Yoda for publication:

- Cleaned and quality-controlled datasets
- Standardized formats and units
- Well-documented processing steps
- Preserved spatial and temporal resolution where scientifically relevant

## Data Lifecycle Management

### Raw Data Handling

The Data Governance Board is currently developing policies regarding raw data retention. Until these policies are finalized, we recommend:

- **Temporarily retain raw data** in secure storage (institutional or personal backup systems)
- **Consult with your Data Steward** before removing any raw data from Yoda
- **Document the processing workflow** to ensure reproducibility

## Getting Help

For questions about:
- **Data processing best practices**: Contact your [Data Steward](../03_general_info/02_data_stewards.md)
- **Computing infrastructure**: Contact your institutional IT support
- **Yoda data management**: See [Uploading Data](01_upload_data.md) and [Adding Metadata](02_add_metadata.md)

## Additional Resources

- [Data Collection Guidelines](../01_data_guidelines/01_data_collection.md)
- [Metadata Standards](../01_data_guidelines/02_metadata_standards.md)
- [Folder Structure](../01_data_guidelines/03_folder_structure.md)
- [Publishing Data](03_publish_data.md) 