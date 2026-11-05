

# %%
from ibridges.interactive import interactive_auth
session = interactive_auth() 
# Note that at this point we are still using local machine, not Yoda (yet)
# make sure that you have a correct 'irods_environment.json' file in the .irods folder of your home directory


# %% [markdown]
# ### Check the session parameters

# %%
print(session.username)
print(session.default_resc) # the resource to which data will be uploaded
print(session.zone)
print(session.server_version)
print(session.get_user_info()) # lists user type and groups
print(session.home) # 

# %%
from ibridges import IrodsPath
from pathlib import Path

# project variables (same as in 02-upload-data.py)
research_folder = 'research-test'
folder = 'Test-folder'
location_name = 'zandmotor'

home = IrodsPath(session, f'~/{research_folder}/{folder}/{location_name}/')

# the data collection uploaded in 02-upload-data.py
data_quality = 'raw-data'
sensor_type = 'camera'
sensor_id = 'camera1'
year = '2024'

irods_path = IrodsPath(session, home, f'{data_quality}/{sensor_type}/{sensor_id}/{year}/May')
print(home)
print(irods_path, "exists: ", irods_path.collection_exists())

# %% [markdown]
# # Download file

# %%
# more info: https://ibridges.readthedocs.io/en/latest/data_transfers.html#download
from ibridges import download
local_download_path = Path('downloads/')
download(session, irods_path, local_download_path, overwrite=True)

# %%
