import asyncio
import os
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)
import traceback

BROADCAST = bool(os.environ.get("BROADCAST", "False"))

# IF YOU FILL BROADCAST VALUE TRUE THEN YOUR BOT COPY MSG AND SEND TO ALL GROUPS
#IF YOU FILL BROADCAST VALUE FALSE THEN YOUR BOT FORWARD MSG TO ALL GROUPS
async def send_msg(user_id, message):
    try:
        if BROADCAST is False:
            await message.forward(chat_id=user_id)
        elif BROADCAST is True:
            await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(int(e.x))
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : blocked the bot\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
