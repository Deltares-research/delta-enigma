# Metadata Standard

## Overview

Delta Enigma uses a custom metadata schema based on (Geo)DCAT principles for describing research datasets. This choice ensures compatibility with European data initiatives while providing comprehensive coverage for our diverse data types.

## Our Metadata Standard

### Core Metadata Elements

The following elements are required for all datasets:

#### Basic Information
- Title
- Description
- Documentation
- Domain 
- Topic Category 
- Version
- Language
- Resource Type (Dataset, Series, or Service)

#### Temporal and Spatial Coverage
- Temporal Coverage (start and end dates)
- Geographical Coverage (bounding box coordinates)
- Reference System (WGS84, Rijksdriehoekstelsel, or ETRS89)

#### Data Collection
- Acquisition Sensor (from standardized list)
- Keywords
- Related Resources
- Creation Date
- Release Date

#### Responsible Parties
- Creator(s) - including:
  - Name
  - Affiliation
  - Person Identifier (e.g., ORCID)
- Contact Point
  - Name
  - Affiliation
  - Contact Details

#### Rights and Access
- License Document (e.g., CC-BY, CC-BY-SA)
- Access Rights (Publicly accessible, Has access restrictions, Not public)

### Optional Elements

Additional metadata elements that can be included:
- Work Package
- Expedition/Collection Information
- Funding Reference
- Applicable Legislation
- Contributors
- Rights Statement
- Additional Documentation Links

### Controlled Vocabularies

The metadata schema uses controlled vocabularies for several fields:
- Domain categories
- Topic categories (based on ISO 19115)
- Acquisition sensors
- License types
- Reference systems
- Work packages
- Language codes (ISO 639-1)

### Creating Metadata Records

For detailed instructions on creating metadata records, see [Add Metadata](../02_actions/02_add_metadata).

## Additional Resources

- [(Geo)DCAT Documentation](https://www.w3.org/TR/vocab-dcat/)

