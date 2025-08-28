# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ibridges>=1.5.1",
# ]
# ///
#%%

from ibridges.interactive import interactive_auth
session = interactive_auth() 
import warnings
warnings.filterwarnings('ignore')
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


# %%
from ibridges.path import IrodsPath
from pathlib import Path

home = IrodsPath(session, '~/research-deltares/WP1/test')
irods_path = IrodsPath(session, home, 'new_research')
irods_col_path = irods_path / 'uploads'
irods_obj_path = irods_col_path / 'test.txt'
print("Current working location:", irods_path)
print("Demo collection name:", irods_col_path, "exists: ", irods_col_path.collection_exists())
print("Demo object name:", irods_obj_path, "exists: ", irods_obj_path.dataobject_exists())


# %% [markdown]
# ### What is the current metadata associated with the data object?

# %%
irods_obj_path.meta

# %%
print(irods_obj_path.meta)
obj_meta = irods_obj_path.meta
obj_meta.add('Key', 'Value', 'Units')
print(type(obj_meta))
# %%
print(irods_col_path.meta)
# %%
