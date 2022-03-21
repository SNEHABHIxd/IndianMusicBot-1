from pyrogram import Client
from Script.Config import API_ID, API_HASH, BOT_TOKEN, SESSION_NAME
from pytgcalls import PyTgCalls, idle

bot = Client(
    "Indian Music Bot",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    )

abhi = Client(
    api_id=API_ID,
    api_hash=API_HASH,
    session_name=SESSION_NAME,
    plugins=dict(root="Script.Plugin"),
    )

user = PyTgCalls(abhi)


with Client(":veez:", API_ID, API_HASH, bot_token=BOT_TOKEN) as app:
    indian = app.get_me()
with user as app:
    me_abhi = app.get_me()
