from pyrogram import filters

from pytgcalls import StreamType

from pytgcalls.types import AudioPiped, AudioVideoPiped

import asyncio

from Script.Cache.admin_check import *

from Script.assistant.TgCalls.Clients import bot, user

from Script.Plugin.Helpers.queues import QUEUE

LIVE_CHATS = []


@bot.on_message(filters.command(["stream", "vstream"]) & filters.group)
@is_admin
async def stream_func(_, message):
    await message.delete()
    state = message.command[0].lower()
    try:
        link = message.text.split(None, 1)[1]
    except:
        return await message.reply_text(f"<b>Usage:</b> <code>/{state} [link]</code>")
    chat_id = message.chat.id
    
    if state == "stream":
        damn = AudioPiped
        emj = "🎵"
    elif state == "vstream":
        damn = AudioVideoPiped
        emj = "🎬"
    m = await message.reply_text("💫")
    try:
        if chat_id in QUEUE:
            return await m.edit("❗️Please send <code>/stop</code> to end voice chat before live streaming.")
        elif chat_id in LIVE_CHATS:
            await user.change_stream(
                chat_id,
                damn(link)
            )
            await m.edit(f"{emj} Started streaming: [Link]({link})", disable_web_page_preview=True)
        else:    
            await user.join_group_call(
                chat_id,
                damn(link),
                stream_type=StreamType().pulse_stream)
            await m.edit(f"{emj} Started streaming: [Link]({link})", disable_web_page_preview=True)
            LIVE_CHATS.append(chat_id)
    except Exception as e:
        return await m.edit(str(e))

    
