# %% [markdown]
# # 4. Download data
#
# Downloads the folder uploaded with 02-upload-data.py to `DOWNLOAD_FOLDER` (set in `config.py`).
#
# More information: https://ibridges.readthedocs.io/en/latest/data_transfers.html#download

# %%
from ibridges import download

from config import DOWNLOAD_FOLDER, UPLOAD_FOLDER, connect, target_collection

session = connect()

dataset = target_collection(session) / UPLOAD_FOLDER.name
# To download other data, use its path on Yoda instead, for example:
# from ibridges import IrodsPath
# dataset = IrodsPath(session, "~/research-wp1-rivers/zandmotor/raw-data/camera/camera1/2024")
print(dataset, "exists:", dataset.collection_exists())

# %% [markdown]
# ### Download

# %%
DOWNLOAD_FOLDER.mkdir(exist_ok=True)
download(session, dataset, DOWNLOAD_FOLDER, overwrite=True)  # overwrite=True replaces local files with the same name
print(f"Downloaded {dataset} to {DOWNLOAD_FOLDER / dataset.name}")

session.close()
