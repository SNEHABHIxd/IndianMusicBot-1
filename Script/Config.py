import os
from os import getenv


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = list(map(int, getenv("SUDO_USERS").split()))

#soon adding new plugins
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
