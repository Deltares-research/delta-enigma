# Publishing Data

## Overview

This guide explains how to secure your dataset in the Yoda vault and publish it with a DOI. Publishing makes your dataset findable and citable: Yoda registers a persistent identifier (DOI) with DataCite and creates a public landing page with the dataset's metadata.

Publishing happens in two steps, each reviewed by your [Data Steward](../03_general_info/02_data_stewards.md):

1. **Submit to the vault** – your folder is copied from the research space to the vault, where it is stored read-only.
2. **Request publication** – the data package in the vault gets a DOI and a public landing page.

```{mermaid} ../_static/delta-enigma-sequence-diagram_1.mermaid
```

## Prerequisites

Before you start, make sure that:

- Your data has been [processed](04_process_data.md): only **refined but unaggregated data** is published
- The folder follows the [folder structure](../01_data_guidelines/03_folder_structure.md)
- The processing steps are documented and included in the folder
- The [metadata](02_add_metadata.md) is complete and follows the [Delta Enigma metadata standard](../01_data_guidelines/02_metadata_standards.md)

Pay particular attention to these metadata fields, as they determine how your dataset is shared once published:

| Field | Options |
|-------|---------|
| License Document | CC-BY (default), CC-BY-SA, CC-BY-SA-NC, CC-0, ODC-By, Custom |
| Access Rights | Publicly accessible (default), Has access restrictions, Not public |

```{admonition} Access rights and published data
:class: info-block

The landing page and metadata of a published dataset are always public. The **Access Rights** field determines whether the data files themselves can be downloaded from the landing page. Discuss restricted or non-public datasets with your Data Steward before submitting.
```

## Step 1: Submit to the Vault

1. Log into the [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/)
2. Navigate to the folder you want to publish in your research space
3. Check that the metadata is complete; Yoda only allows submission when all required fields are filled in
4. Click **Submit** to submit the folder to the vault

While the submission is under review, the folder is locked and cannot be edited.

Your Data Steward then reviews the data and metadata:

- **Accepted** – the folder is copied to the vault as a data package. The package is stored read-only and has the status *Unpublished*.
- **Rejected** – you receive feedback, the folder is unlocked, and you can make changes and submit again.

## Step 2: Request Publication

1. In the Yoda portal, go to the **Vault** and open your data package
2. Click **Submit for publication**
3. Read and accept the terms and conditions

The data package now has the status *Submitted for publication* and your Data Steward is notified.

- **Approved** – Yoda reserves a DOI at DataCite, registers the metadata, and publishes the landing page. Once this is done, the status changes to *Published* and the dataset can be found and cited via its DOI.
- **Rejected** – the data package returns to *Unpublished* and your Data Steward tells you what needs to be fixed.

## After Publication

- **Cite your dataset** using its DOI, for example in the data availability statement of your papers
- **Published datasets cannot be changed or deleted.** To correct or extend a dataset, publish a new version through the same process and contact your Data Steward
- If a published dataset must be withdrawn, contact your Data Steward

## Getting Help

For questions about publishing, licenses or access rights, contact your [Data Steward](../03_general_info/02_data_stewards.md).

## Additional Resources

- [Full Data Workflow](../01_data_guidelines/07_full_data_workflow.md)
- [Processing Data](04_process_data.md)
- [Metadata Standards](../01_data_guidelines/02_metadata_standards.md)
- [Yoda user documentation](https://utrechtuniversity.github.io/yoda/)
