# Working with Yoda from Python

## Overview

Besides the web portal and WebDAV (see [Uploading Data](01_upload_data.md)), you can work with Yoda from Python. This is useful when you want to automate uploads, upload many files, or download data directly into your processing workflow.

We provide ready-to-use Python scripts in the [delta-enigma repository on GitHub](https://github.com/Deltares-research/delta-enigma). The scripts use [iBridges](https://ibridges.readthedocs.io/), a Python package for iRODS, the system Yoda is built on.

```{admonition} Get the scripts
:class: note

The [README of the repository](https://github.com/Deltares-research/delta-enigma#readme) has step-by-step instructions for installing the scripts and their dependencies, connecting to Yoda and troubleshooting.
```

## What the scripts do

| Script | What it does |
|---|---|
| `01-setup-and-connect.py` | Connects to Yoda, lists the research groups you have access to and checks your settings |
| `02-upload-data.py` | Creates a folder following the [Delta Enigma folder structure](../01_data_guidelines/03_folder_structure.md) and uploads your data into it |
| `03-add-metadata.py` | Adds a Yoda metadata file (`yoda-metadata.json`) to the uploaded folder |
| `04-download-data.py` | Downloads data from Yoda to your computer |

All settings, such as your research group, location and sensor, are in one file: `tutorials/config.py`. The scripts come with a small example dataset that you can use to try them out.

## Prerequisites

- **Access to the research group of your work package.** See [Access to Yoda](../01_data_guidelines/04_access_to_yoda.md).
- **A Data Access Password.** Scripts cannot use your institutional login, so you need a separate password:
  1. Log in to the [SURF Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/).
  2. Click your username in the top right and choose **Data Access Password**.
  3. Generate a password and copy it. The scripts ask for it the first time you connect.

  Data Access Passwords expire after a while. When the scripts report that your password is wrong, generate a new one.
- **uv**, a tool that installs Python and the required packages. The README explains how to install it on Windows, macOS and Linux.

## Metadata from a script

In Yoda, the metadata of a folder is stored in a file called `yoda-metadata.json` inside that folder. The metadata form in the Yoda portal creates this file, and Yoda reads it automatically when you upload one. So you can fill in the metadata of a dataset in the portal (see [Adding Metadata](02_add_metadata.md)) or upload a `yoda-metadata.json` file with a script. Either way, follow the [Metadata Standards](../01_data_guidelines/02_metadata_standards.md).

## Getting Help

- **Problems with the scripts**: see the troubleshooting section in the [README](https://github.com/Deltares-research/delta-enigma#troubleshooting).
- **Access to a research group**: contact the data & user manager of your work package.
- **Other questions**: contact your [Data Steward](../03_general_info/02_data_stewards.md).
