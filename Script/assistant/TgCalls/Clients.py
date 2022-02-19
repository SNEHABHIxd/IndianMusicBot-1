from pyrogram import Client
from Script.Config import API_ID, API_HASH, BOT_TOKEN


user = Client(
    "Indian Music Bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Script.Plugin"),
)

user.start()
