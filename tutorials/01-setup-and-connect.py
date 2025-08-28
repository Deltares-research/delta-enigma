# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ibridges>=1.5.1",
# ]
# ///
# %% [markdown]
# More information on how to connect to the iRODS server can be found [here](https://github.com/iBridges-for-iRODS/iBridges/blob/3ef9ed82133f76fd66add222dfb8f407a3d31681/tutorials/01-Setup-and-connect.ipynb). 
#
# There is a environments file in the .irods folder that you can use to connect to the iRODS server.
# Go to the .irods folder and rename the file 'irods_environment[template].json' to 'irods_environment.json' and fill in your username.
# Then we are ready to connect to the iRODS server.

# %%
from ibridges.interactive import interactive_auth
session = interactive_auth() 
# Note that at this point we are still using local machine, not Yoda (yet)
# make sure that you have a correct 'irods_environment.json' file in the .irods folder of your home directory

# %%
# ### Check the session parameters
print(session.username)
print(session.default_resc) # the resource to which data will be uploaded
print(session.zone)
print(session.server_version)
print(session.get_user_info()) # lists user type and groups
print(session.home) # 

# %% [markdown]
# I you are connected, find the folder of your project, and make this your home directory
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
print("Demo collection name:", irods_col_path, "exists: ", irods_path.collection_exists())
if irods_path.collection_exists() == False: # if the collection does not exist, create it
    IrodsPath.create_collection(session, irods_path)

# %% [markdown]
# Now we are ready to upload data. (see 02-upload-data.py)
# %%
