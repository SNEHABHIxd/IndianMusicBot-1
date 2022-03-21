import os
from os import getenv


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
OWNER_ID = list(map(int, getenv("OWNER_ID").split()))

#soon adding new plugins
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
MONGODB_URL = os.environ.get("MONGODB_URL", None)
INDIAN_BOT = getenv("INDIAN_BOT", "")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
BROADCAST = bool(os.environ.get("BROADCAST", "False"))
