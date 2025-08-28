# %% [markdown]
# ### Let's start by initializing the session
# %%
from ibridges.interactive import interactive_auth
session = interactive_auth() # %%
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