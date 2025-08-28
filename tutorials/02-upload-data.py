# %% [markdown]
# ### Let's start by initializing the session

# %%
from ibridges.interactive import interactive_auth
session = interactive_auth() #

# %%
from ibridges.path import IrodsPath
from pathlib import Path
# project variables
research_folder = 'research-deltares'
work_package = 'WP1'
location_name = 'zandmotor'

home = IrodsPath(session, f'~/{research_folder}/{work_package}/{location_name}/')

# new data collection variables
data_quality = 'raw-data'
sensor_type = 'camera'
sensor_id = 'camera1'
year = '2024'

irods_path = IrodsPath(session, home, f'{data_quality}/{sensor_type}/{sensor_id}/{year}')
print("Current working location:", irods_path)
print("Demo collection name:", irods_path, "exists: ", irods_path.collection_exists())
if irods_path.collection_exists() == False: # if the collection does not exist, create it
    IrodsPath.create_collection(session, irods_path)#link to the file you want to upload


# %%
# more info on https://ibridges.readthedocs.io/en/latest/data_transfers.html#upload

from ibridges import upload
upload_file_path = Path("May") 
upload(session, upload_file_path, irods_path, overwrite=True)

# The folder or file is now uploaded to the iRODS server.
# You can check this by going to the Yoda website and navigating to the folder or file.
# %%

