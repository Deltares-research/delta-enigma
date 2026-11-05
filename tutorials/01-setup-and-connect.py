# %% [markdown]
# # 1. Set up and connect to Yoda
#
# Connects to the Delta Enigma Yoda environment and checks your settings in `config.py`.
#
# The first time you run this, you are asked for:
# 1. your Yoda username: the e-mail address you log in to Yoda with;
# 2. your Data Access Password: create one in the Yoda portal (see the README).
#
# Both are remembered on your computer. You only need to enter a new Data Access Password when the old one expires.
#
# More information: https://ibridges.readthedocs.io/en/latest/

# %%
from config import RESEARCH_GROUP, connect, target_collection

session = connect()

# %% [markdown]
# ### Check the session

# %%
print("Username:        ", session.username)
print("Zone:            ", session.zone)
print("Default resource:", session.default_resc)  # the resource to which data will be uploaded
print("Server version:  ", session.server_version)

user_type, groups = session.get_user_info()
print("Research groups you have access to:")
for group in sorted(groups):
    if group.startswith("research-"):
        print("  ", group)

# %% [markdown]
# ### Check your research group and folder
# If `RESEARCH_GROUP` in `config.py` is not correct, this stops and lists the groups you can choose from.

# %%
collection = target_collection(session)
print(f"Research group '{RESEARCH_GROUP}' found.")
print("Scripts 02-04 will upload to and download from:", collection)

session.close()

# %% [markdown]
# You are connected. Next: upload data with 02-upload-data.py.
