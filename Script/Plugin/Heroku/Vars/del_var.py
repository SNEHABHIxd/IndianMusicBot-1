from pyrogram import Client, filters
from pyrogram.types import Message
from Script.Plugin.Helpers.Heroku import check_heroku
import heroku3
from Script.Config import OWNER_ID

@Client.on_message(command("setvar") & filters.user(OWNER_ID))
@_check_heroku
async def delvar(client: Client, message: Message, app_):
    msg = await message.reply_text("`please wait...!`")
    heroku_var = app_.config()
    _var = get_text(message)
    if not _var:
        await msg.edit("`give a var name to delete!`")
        return
    if _var not in heroku_var:
        await msg.edit("`this var doesn't exists!`")
        return
    await msg.edit(f"sucessfully deleted var `{_var}`")
    del heroku_var[_var]
