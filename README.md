# Delta Enigma Yoda scripts

Python scripts for working with research data in the Delta Enigma Yoda environment: connecting, uploading data, adding metadata and downloading data. The scripts use [iBridges](https://ibridges.readthedocs.io/), a Python package for iRODS, the system Yoda is built on.

For the data management guidelines (folder structure, metadata standards, who to contact), see the [Delta Enigma Data Management Handbook](https://deltares-research.github.io/delta-enigma/).

## Before you start

You need:

- **Access to Yoda** for the research group of your work package. Ask the data & user manager of your work package; see [Access to Yoda](https://deltares-research.github.io/delta-enigma/01_data_guidelines/04_access_to_yoda.html) in the handbook.
- **A Data Access Password** (see [step 3](#3-create-a-data-access-password)). Scripts cannot use your normal institutional login.

## Setup

### 1. Install uv

[uv](https://docs.astral.sh/uv/) installs Python and the required packages for you.

macOS and Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Close and reopen your terminal afterwards so the `uv` command is available.

### 2. Get the scripts and install the dependencies

Clone the repository (or [download it as a ZIP](https://github.com/Deltares-research/delta-enigma/archive/refs/heads/main.zip) and unzip it):

```bash
git clone https://github.com/Deltares-research/delta-enigma.git
cd delta-enigma
uv sync
```

`uv sync` installs the right Python version and the dependencies into a `.venv` folder in the repository.

### 3. Create a Data Access Password

1. Log in to the [Delta Enigma Yoda portal](https://deltaenigma-yoda.irods.surfsara.nl/) with your institutional account.
2. Click your username in the top right and choose **Data Access Password**.
3. Generate a password and copy it. You will paste it in the next step.

A Data Access Password expires after a while. When the scripts say your password is wrong, create a new one.

### 4. Connect

```bash
uv run python tutorials/01-setup-and-connect.py
```

The first time, the script asks for:

- **Your Yoda username**: the e-mail address you log in to Yoda with. It is saved in `~/.irods/irods_environment.json` in your home folder.
- **Your Data Access Password**: nothing appears on screen while you type or paste it; just press Enter. It is saved (scrambled) in `~/.irods/.irodsA`, so you don't need to enter it again until it expires.

The script then lists the research groups you have access to.

Run the scripts in a normal terminal window. Tools that can't show an input prompt won't let you enter the password.

## Using the scripts

### Settings

All settings are in [`tutorials/config.py`](tutorials/config.py). Set `RESEARCH_GROUP` to the research group of your work package (for example `research-wp1-rivers`), and set the location, data type, sensor and year of your data. Together they make up the folder on Yoda, following the [Delta Enigma folder structure](https://deltares-research.github.io/delta-enigma/01_data_guidelines/03_folder_structure.html):

```
research-wp1-rivers/zandmotor/raw-data/adcp/adcp1/2024/
```

By default the scripts upload a small example dataset (`tutorials/example-data/`) to the `research-test` group. If you have access to `research-test`, you can try the scripts there first.

### Scripts

Run them in order:

| Script | What it does |
|---|---|
| `01-setup-and-connect.py` | Connects to Yoda, lists your research groups and checks your settings |
| `02-upload-data.py` | Creates the folder on Yoda and uploads `UPLOAD_FOLDER` into it |
| `03-add-metadata.py` | Adds a Yoda metadata file (`yoda-metadata.json`) to the uploaded folder, and shows how to add your own key-value metadata |
| `04-download-data.py` | Downloads the uploaded folder to `tutorials/downloads/` |

```bash
uv run python tutorials/02-upload-data.py
```

You can also run the scripts step by step in VS Code: open the repository, select the `.venv` environment as Python interpreter, and click **Run Cell** above each `# %%` block.

### Without uv

If you already have Python 3.12 or newer, you can also install the dependencies with pip and run the scripts with `python`:

```bash
pip install ibridges
python tutorials/01-setup-and-connect.py
```

## Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError: No module named 'ibridges'` | Run the scripts with `uv run python ...` from inside the repository, or select the `.venv` interpreter in your editor. |
| `The provided username and/or password is wrong` | Your Data Access Password has probably expired: create a new one in the Yoda portal. Also check the username in `~/.irods/irods_environment.json`. |
| The password prompt repeats without waiting for input | Run the script in a normal terminal window. |
| `Research group '...' does not exist or you do not have access to it` | Set `RESEARCH_GROUP` in `tutorials/config.py` to one of the groups listed, or ask the data & user manager of your work package for access. |

Questions? Contact the [data steward of your institute](https://deltares-research.github.io/delta-enigma/03_general_info/02_data_stewards.html).

## Other contents of this repository

- [`docs/`](docs/): source of the Data Management Handbook (Sphinx).
- [`metadata/`](metadata/): the Delta Enigma metadata schema and a metadata form app.
