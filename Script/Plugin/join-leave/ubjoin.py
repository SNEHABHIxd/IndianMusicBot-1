import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from Script.assistant.TgCalls.Clients import abhi
from Script.Config import OWNER_ID
from Script.Cache.admin_check import *


@Client.on_message(command(["userbotjoin", "ubjoin"]) & ~filters.private & ~filters.bot & filters.user(OWNER_ID)
@is_admin
async def ubjoin(client, message):
    chat_id = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chat_id)
    except:
        await message.reply_text("<b>promote me as admin first !</b>")
        await message.reply_sticker("CAACAgUAAx0CYPNCJwACJpthfoPdqrvoutRwQzk_v9bqUyOnugACRgADE_yaMj3RPONrfXfZIQQ")
        return
    try:
        user = await abhi.get_me()
    except:
        user.first_name = "indian music"
    try:
        await abhi.join_chat(invitelink)
        await abhi.send_message(message.chat.id, "🤖: i'm joined here for playing music on voice chat")
        await abhi.send_sticker(message.chat.id, "CAACAgUAAx0CYPNCJwACJpdhfoO6uBuC9b2EglpYeiNKOMtqJAACNQADE_yaMk-0JIP096z2IQQ")
    except UserAlreadyParticipant:
        await message.reply_text(f"<b>✅ userbot already joined chat</b>")
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n\n User {user.first_name} couldn't join your group due to heavy join requests for userbot."
            "\n\nor manually add assistant to your Group and try again</b>",
        )
        return
    await message.reply_text(f"<b>✅ userbot successfully joined chat</b>")
