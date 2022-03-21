import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from Script.assistant.TgCalls.Clients import bot
from Script.Config import OWNER_ID

@Client.on_message(filters.command(["broadcast"]) & filters.user(OWNER_ID))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in OWNER_ID:
        return
    else:
        wtf = await message.reply("' broadcast started..`")
        if not message.reply_to_message:
            await wtf.edit("**__Ƥɭɘɑsɘ Ʀɘƥɭy Ƭø ɑ Mɘssɑʛɘ Ƭø Stɑɤt Ɓɤøɑɗƈɑst ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in bot.iter_dialogs():
            try:
                await bot.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`Broadcasting` \n\n**Total success:** `{sent}` chats \n**Total failed:** {failed} chats")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`Broadcasting completed!` \n\n**Total done:** `{sent}` chats \n**Total failed:** {failed} chats")
