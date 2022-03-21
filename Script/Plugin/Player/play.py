import glob
import json
import logging
import asyncio
import youtube_dl
import yt_dlp
from pytgcalls import StreamType
from pytube import YouTube
from youtube_search import YoutubeSearch
from pytgcalls.types import Update
from pyrogram.raw.base import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo
)
from pytgcalls.types.stream import StreamAudioEnded, StreamVideoEnded
from pyrogram import filters, Client
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import Message
from Script.Plugin.Helpers.Player import QUEUE, add_to_queue, get_queue, clear_queue, pop_an_item
from Script.Cache.admin_check import *
from Script.assistant.TgCalls.Clients import *
from Script.Cache.YouTubeDL import yt_audio, yt_video


    
LIVE_CHATS = []

@bot.on_message(filters.command(["play", "vplay"]) & filters.group)
async def play(c: Client, message: Message):
    await message.delete()
    user_id = message.from_user.id
    
    state = message.command[0].lower()
    try:
        query = message.text.split(None, 1)[1]
    except:
        return await message.reply_text(f"<b>Usage:</b> <code>/{state} [query]</code>")
    replied = message.reply_to_message
    chat_id = message.chat.id
    
    if message.sender_chat:
        return await message.reply_text(
            "you're an __Anonymous__ user !\n\n» revert back to your real user account to use this bot."
        )
    try:
        ubot = me_abhi.id
        blaze = await c.get_chat_member(chat_id, ubot)
        if blaze.status == "banned":
            try:
                await message.reply_text("❌ The userbot is banned in this chat, unban the userbot first to be able to play music !")
                await remove_active_chat(chat_id)
            except BaseException:
                pass
            invitelink = (await c.get_chat(chat_id)).invite_link
            if not invitelink:
                await c.export_chat_invite_link(chat_id)
                invitelink = (await c.get_chat(chat_id)).invite_link
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await abhi.join_chat(invitelink)
            await remove_active_chat(chat_id)
    except UserNotParticipant:
        try:
            invitelink = (await c.get_chat(chat_id)).invite_link
            if not invitelink:
                await c.export_chat_invite_link(chat_id)
                invitelink = (await c.get_chat(chat_id)).invite_link
            if invitelink.startswith("https://t.me/+"):
                invitelink = invitelink.replace(
                    "https://t.me/+", "https://t.me/joinchat/"
                )
            await abhi.join_chat(invitelink)
            await remove_active_chat(chat_id)
        except UserAlreadyParticipant:
            pass
        
    if chat_id in LIVE_CHATS:
        return await message.reply_text("❗️Please send <code>/stop</code> to end current live streaming before play songs or videos.")
    
    m = await message.reply_text("💫")
    if state == "play":
        damn = AudioPiped
        ded = yt_audio
        doom = "Audio"
    elif state == "vplay":
        damn = AudioVideoPiped
        ded = yt_video
        doom = "Video"
    if "low" in query:
        Q = "low"
    elif "mid" in query:
        Q = "mid"
    elif "high" in query:
        Q = "high"
    else:
        Q = "0"
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        thumb = results[0]["thumbnails"][0]
        duration = results[0]["duration"]
        yt = YouTube(link)
        cap = f"▶️ <b>Now playing:</b> [{yt.title}]({link}) | `{doom}` \n\n⏳ <b>Duration:</b> {duration}"
        try:
            ydl_opts = {"format": "bestvideo[height<=720]+bestaudio/best[height<=720]"}
            ydl = yt_dlp.YoutubeDL(ydl_opts)
            info_dict = ydl.extract_info(link, download=False)
            p = json.dumps(info_dict)
            a = json.loads(p)
            playlink = a['formats'][1]['manifest_url']
        except:
            omfo, playlink = await ded(link)
            if omfo == "0":
                return await m.edit("❗️YTDL ERROR !!!")               
    except Exception as e:
        return await m.edit(str(e))
    
    try:
        if chat_id in QUEUE:
            position = add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            caps = f"#️⃣ <b>queued at position {position}</b> \n\n[{yt.title}]({link}) \n\n⏳ <b>Duration:</b> {duration}"
            await message.reply_photo(thumb, caption=caps)
            await m.delete()
        else:            
            await user.join_group_call(
                chat_id,
                damn(playlink),
                
                stream_type=StreamType().pulse_stream
            )
            add_to_queue(chat_id, yt.title, duration, link, playlink, doom, Q, thumb)
            await message.reply_photo(thumb, caption=cap)
            await m.delete()
    except Exception as e:
        return await m.edit(str(e))
