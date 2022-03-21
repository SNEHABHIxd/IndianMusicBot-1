from pyrogram import Client
from Script.Config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "Indian Music Bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="Script.Plugin"),
    )

abhi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    
    )

user = PyTgCalls(abhi)


with Client("Indian Music Bot", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    me_bot = app.get_me()
with abhi as app:
    me_abhi = app.get_me()
