import os
from os import getenv


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))

