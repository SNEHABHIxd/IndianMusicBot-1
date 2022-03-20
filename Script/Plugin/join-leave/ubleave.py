from pyrogram import filters, Client
from pyrogram.types import Message
from Script.assistant.TgCalls.Clients import abhi
from Script.Cache.admin_check import *
import asyncio
from Script.Config import OWNER_ID


@Client.on_message(command(["userbotleave", "ubleave"]) & filters.group & ~filters.edited & filters.user(OWNER_ID))
@is_admin
async def rem(client, message):
    try:
        await abhi.send_sticker(message.chat.id, "CAACAgUAAx0CYPNCJwACA0RhbkLHaItFAAFFSUQZW3YhLiqJb2MAAgYFAAIclOFWYPPBpmhRMYUhBA")
        await abhi.send_message(message.chat.id, "✅ I'm leaving your group, bye bye!")
        await abhi.leave_chat(message.chat.id)
    except:
        await message.reply_text("<b>user couldn't leave your group, may be floodwaits.\n\nor manually kick me from your group</b>")
        return
