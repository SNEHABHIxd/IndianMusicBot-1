import os
import asyncio
import string
from Script.Plugin.Helpers.Broadcast import send_msg
from Script.Plugin.Database import db
import time
import datetime
import random
import aiofiles
from pyrogram import Client, filters
from pyrogram.types import Message
from Script.Config import OWNER_ID

broadcast_ids = {}

Client.on_message(filters.command("broadcast") & filters.private & filters.user(OWNER_ID) & filters.reply)
async def broadcast(_, m: Message):
    await main_broadcast_handler(m, db)



async def bot_broadcast(m, db):
    all_users = await db.get_all_users()
    broadcast_msg = m.reply_to_messasyncage
    while True:
        broadcast_id = "".join(random.choice(string.ascii_letters) for i in range(3))
        if not broadcast_ids.get(broadcast_id):
            break
    out = await m.reply_text(
        text="**💡 broadcast started...**\n\n**» when it's done, you'll be notified here !**"
    )

    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0
    broadcast_ids[broadcast_id] = dict(
        total=total_users, current=done, failed=failed, success=success
    )
    async with aiofiles.open("broadcast-logs.txt", "w") as broadcast_log_file:
        async for user in all_users:
            sts, msg = await send_msg(user_id=int(user["id"]), message=broadcast_msg)
            if msg is not None:
                await broadcast_log_file.write(msg)
            if sts == 200:
                success += 1
            else:
                failed += 1
            if sts == 400:
                await db.delete_user(user["id"])
            done += 1
            if broadcast_ids.get(broadcast_id) is None:
                break
            else:
                broadcast_ids[broadcast_id].update(
                    dict(current=done, failed=failed, success=success)
                )
    if broadcast_ids.get(broadcast_id):
        broadcast_ids.pop(broadcast_id)
    completed_in = datetime.timedelta(seconds=int(time.time() - start_time))
    await asyncio.sleep(3)
    await out.delete()
    if failed == 0:
        await m.reply_text(
            text=f"✅ Broadcasting completed! \n**Completed in:** `{completed_in}` \n\n**Total users:** `{total_users}` \n**Total done:** `{done}` \n**Total success:** `{success}` \n**Total failed:** `{failed}`",
            quote=True,
        )
    else:
        await m.reply_document(
            document="broadcast-logs.txt",
            caption=f"✅ Broadcasting completed! \n**Completed in:** `{completed_in}`\n\n**Total users:** `{total_users}` \n**Total done:** `{done}` \n**Total success:** `{success}` \n**Total failed:** `{failed}`",
            quote=True,
        )
    os.remove("broadcast-logs.txt")

