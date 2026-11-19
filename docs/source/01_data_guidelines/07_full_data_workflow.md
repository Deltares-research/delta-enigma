# Full Data Workflow

## Overview

This page shows the full life cycle of a Delta Enigma dataset in Yoda, from the first upload of raw sensor data to a published dataset with a DOI. Use it as a map: each phase links to the page with detailed instructions.

## Workflow diagram

```{mermaid} ../_static/delta-enigma-sequence-diagram_1.mermaid
```

## Phases

1. **Collect and upload** – Upload your raw sensor data to the Yoda research space following the [folder structure](03_folder_structure.md), and add metadata according to the [Delta Enigma metadata standard](02_metadata_standards.md). See [Uploading Data](../02_actions/01_upload_data.md) and [Adding Metadata](../02_actions/02_add_metadata.md).
2. **Process outside Yoda** – Yoda stores data but does not run computations. Download the raw data, clean and transform it in your own environment (local, HPC or cloud), and upload the refined dataset together with documentation of the processing steps. See [Processing Data](../02_actions/04_process_data.md).
3. **Secure in the vault** – Submit the folder to the vault. Your [data steward](../03_general_info/02_data_stewards.md) checks the data and metadata and either accepts the submission or sends it back with feedback.
4. **Publish** – Request publication of the data package in the vault. After approval by the data steward, Yoda registers a DOI with DataCite and creates a public landing page, making the dataset findable and citable. See [Publishing Data](../02_actions/03_publish_data.md).

```{admonition} Questions?
:class: info-block

If anything in this workflow is unclear, contact your [data steward](../03_general_info/02_data_stewards.md).
```
