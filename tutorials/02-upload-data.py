# %% [markdown]
# ### Let's start by initializing the session

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

# %% [markdown]
# 

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

# %% [markdown]
# # Make changes to the file

# %%
def transform_data(data):
    # Read the data from the file
    with open(data, 'r') as f:
        input_data = f.read()
    
    #make your transformations here
    transformed_data = input_data
    return transformed_data

def save_transformed_data(transformed_data, filename):
    # Create uploads directory if it doesn't exist
    upload_dir = Path('uploads')
    upload_dir.mkdir(exist_ok=True)
    
    # Save transformed data to uploads folder
    output_path = upload_dir / filename
    with open(output_path, 'w') as f:
        f.write(transformed_data)
    return output_path

# Transform the data
input_file = Path("downloads/test.txt")
transformed_data = transform_data(input_file)

# Save transformed data to uploads folder with same filename
output_file = save_transformed_data(transformed_data, input_file.name)

# %% [markdown]
# # Upload file

# %%
irods_path

# %%
# more info on https://ibridges.readthedocs.io/en/latest/data_transfers.html#upload

from ibridges import upload
local_upload_path = Path("uploads")
upload(session, local_upload_path, irods_path)


# %%


# %%



