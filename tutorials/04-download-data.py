

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

home = IrodsPath(session, '~/research-deltares/WP1/test')
irods_path = IrodsPath(session, home, 'new_research')
print(home)
print(irods_path)

# %% [markdown]
# # Download file

# %%
# more info: https://ibridges.readthedocs.io/en/latest/data_transfers.html#download
from ibridges import download
local_download_path = Path('downloads/')
download(session, irods_path, local_download_path, overwrite=True)

# %%
