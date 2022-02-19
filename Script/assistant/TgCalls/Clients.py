from pyrogram import Client
from Script.Config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME


bot = Client(
    "Indian Music Bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    )

app = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=STRING1,
    plugins=dict(root="Script.Plugins"),
    )

user = PyTgCalls(app)

user.start()
bot.run()
idle()
