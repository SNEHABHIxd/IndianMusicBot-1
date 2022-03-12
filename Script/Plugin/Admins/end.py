from Script.Plugin.queues import QUEUE, clear_queue

from Script.assistant.TgCalls.Clients import bot, user

from Script.Plugin.PyTgCalls import 

from Script.Cache.admin_check import *

LIVE_CHATS = []



@bot.on_message(filters.command(["stop", "end"]) & filters.group)
@is_admin
async def end(_, message):
    await message.delete()
    chat_id = message.chat.id
    if chat_id in LIVE_CHATS:
        await user.leave_group_call(chat_id)
        LIVE_CHATS.remove(chat_id)
        return await message.reply_text("⏹ Stopped streaming.")
        
    if chat_id in QUEUE:
        await user.leave_group_call(chat_id)
        clear_queue(chat_id)
        await message.reply_text("⏹ Stopped streaming.")
    else:
        await message.reply_text("❗Nothing is playing.")
