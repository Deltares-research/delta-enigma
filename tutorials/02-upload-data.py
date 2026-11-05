# %% [markdown]
# # 2. Upload data
#
# Uploads the local folder `UPLOAD_FOLDER` (set in `config.py`) to your research group on Yoda,
# following the Delta Enigma folder structure. By default this is the example dataset in `example-data/May.26`.
#
# More information: https://ibridges.readthedocs.io/en/latest/data_transfers.html#upload

# %%
from ibridges import IrodsPath, upload

from config import UPLOAD_FOLDER, connect, target_collection

session = connect()

# %% [markdown]
# ### Create the destination folder on Yoda

# %%
collection = target_collection(session)
if not collection.collection_exists():
    IrodsPath.create_collection(session, collection)  # also creates missing parent folders
    print("Created folder:", collection)
else:
    print("Folder already exists:", collection)

# %% [markdown]
# ### Upload

# %%
upload(session, UPLOAD_FOLDER, collection, overwrite=True)  # overwrite=True replaces files that are already on Yoda
print(f"Uploaded {UPLOAD_FOLDER} to {collection / UPLOAD_FOLDER.name}")

session.close()

# %% [markdown]
# You can check the result in the Yoda portal: https://deltaenigma-yoda.irods.surfsara.nl/
#
# Next: add metadata with 03-add-metadata.py.
