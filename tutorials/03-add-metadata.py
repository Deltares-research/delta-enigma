# %% [markdown]
# # 3. Add metadata
#
# In Yoda, the metadata of a folder is stored in a file called `yoda-metadata.json` inside that folder.
# This is the same file that the metadata form in the Yoda portal creates, and Yoda reads it automatically.
# So adding metadata from a script means uploading a `yoda-metadata.json` file.
#
# This script adds `METADATA_FILE` (set in `config.py`) to the folder uploaded with 02-upload-data.py.
# The example file contains placeholder values: fill in the metadata of your own data in the Yoda portal,
# or edit a copy of the example file. See the handbook for the metadata standards:
# https://deltares-research.github.io/delta-enigma/01_data_guidelines/02_metadata_standards.html

# %%
from ibridges import upload

from config import METADATA_FILE, UPLOAD_FOLDER, connect, target_collection

session = connect()

dataset = target_collection(session) / UPLOAD_FOLDER.name
if not dataset.collection_exists():
    raise SystemExit(f"{dataset} does not exist. Run 02-upload-data.py first.")

# %% [markdown]
# ### Upload the Yoda metadata file

# %%
upload(session, METADATA_FILE, dataset / "yoda-metadata.json", overwrite=True)
print("Added metadata to", dataset)

# %% [markdown]
# ### Check the metadata
# Yoda stores the contents of `yoda-metadata.json` as key-value metadata on the folder.

# %%
print(dataset.meta)

# %% [markdown]
# ### Optional: add your own key-value metadata
# You can also attach your own key-value pairs (with optional units) to folders and files.
# These are not shown in the Yoda metadata form.
# More information: https://ibridges.readthedocs.io/en/latest/metadata.html

# %%
meta = dataset.meta
if "example_key" in meta:  # remove the old value, so the script can be run more than once
    meta.delete("example_key")
meta.add("example_key", "example value")
print(meta["example_key"])

session.close()

# %% [markdown]
# Next: download data with 04-download-data.py.
