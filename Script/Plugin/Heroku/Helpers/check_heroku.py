#FOR USE THIS FEATURE U FILL HEROKU_APP_NAME AND HEROKU_API_KEY
import os
import re
import heroku3
from functools import wraps
import asyncio
from pyrogram import Client
from pyrogram.types import Message
from Script.Config import (
    HEROKU_API_KEY,
    HEROKU_APP_NAME,
)

heroku_client = None
if HEROKU_API_KEY:
    heroku_client = heroku3.from_key(HEROKU_API_KEY)
    
    
def _check_heroku(func):
    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text("`Please Add Heroku API Key To Use This Feature!`")
        elif not HEROKU_APP_NAME:
            await edit_or_reply(message, "`Please Add Heroku APP Name To Use This Feature!`")
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except:
                await message.reply_text(message, "`Heroku Api Key And App Name Doesn't Match! Check it again`")
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli
