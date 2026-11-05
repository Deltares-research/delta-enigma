"""Settings shared by the tutorial scripts.

Edit the values under "Your settings" before running the scripts.
"""

import json
from pathlib import Path

from ibridges import IrodsPath
from ibridges.interactive import interactive_auth

# ---------------------------------------------------------------------------
# Your settings
# ---------------------------------------------------------------------------

# The Yoda research group of your work package, for example 'research-wp1-rivers'.
# Run 01-setup-and-connect.py to see which research groups you have access to.
RESEARCH_GROUP = "research-test"

# Where your data goes within the research group, following the Delta Enigma folder structure:
# https://deltares-research.github.io/delta-enigma/01_data_guidelines/03_folder_structure.html
LOCATION = "zandmotor"
DATA_TYPE = "raw-data"  # raw-data, processed-data or published-data
SENSOR_TYPE = "adcp"
SENSOR_ID = "adcp1"
YEAR = "2024"

TUTORIAL_DIR = Path(__file__).parent

# Local folder to upload (02-upload-data.py). By default a small example dataset.
UPLOAD_FOLDER = TUTORIAL_DIR / "example-data" / "May.26"

# Yoda metadata file to add to the uploaded folder (03-add-metadata.py).
METADATA_FILE = TUTORIAL_DIR / "example-data" / "yoda-metadata.json"

# Local folder to download data to (04-download-data.py).
DOWNLOAD_FOLDER = TUTORIAL_DIR / "downloads"

# ---------------------------------------------------------------------------
# Helpers used by the scripts (no need to edit below this line)
# ---------------------------------------------------------------------------

IRODS_ENV_FILE = Path.home() / ".irods" / "irods_environment.json"
IRODS_ENV_TEMPLATE = TUTORIAL_DIR / "irods_environment_template.json"
USERNAME_PLACEHOLDER = "[YOUR USERNAME]"


def create_irods_environment():
    """Create ~/.irods/irods_environment.json from the template if it does not exist yet."""
    if IRODS_ENV_FILE.exists():
        env = json.loads(IRODS_ENV_FILE.read_text())
        if env.get("irods_user_name") not in (None, "", USERNAME_PLACEHOLDER):
            return
    else:
        env = json.loads(IRODS_ENV_TEMPLATE.read_text())

    print(f"Setting up your connection settings in {IRODS_ENV_FILE}")
    env["irods_user_name"] = input("Your Yoda username (the e-mail address you log in to Yoda with): ").strip()
    IRODS_ENV_FILE.parent.mkdir(exist_ok=True)
    IRODS_ENV_FILE.write_text(json.dumps(env, indent=4))


def connect():
    """Connect to Yoda. Asks for your Data Access Password if no valid one is cached."""
    create_irods_environment()
    return interactive_auth(irods_env_path=IRODS_ENV_FILE)


def research_group_path(session):
    """Path of RESEARCH_GROUP on Yoda. Stops with a list of options if it is not accessible."""
    path = IrodsPath(session, "~", RESEARCH_GROUP)
    if not path.collection_exists():
        available = [p.name for p in IrodsPath(session, "~").walk(depth=1) if p.name.startswith("research-")]
        raise SystemExit(
            f"Research group '{RESEARCH_GROUP}' does not exist or you do not have access to it.\n"
            f"Set RESEARCH_GROUP in config.py to one of: {', '.join(available) or '(none)'}\n"
            "No access to the group you need? Ask the data & user manager of your work package."
        )
    return path


def target_collection(session):
    """Yoda folder that the scripts upload to and download from, based on the settings above."""
    return IrodsPath(session, research_group_path(session), LOCATION, DATA_TYPE, SENSOR_TYPE, SENSOR_ID, YEAR)
