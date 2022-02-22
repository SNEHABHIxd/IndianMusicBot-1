from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("⏸", callback_data="pause"),
            InlineKeyboardButton("▶️", callback_data="resume"),
            InlineKeyboardButton("⏭", callback_data="skip"),
            InlineKeyboardButton("⏹", callback_data="stop"),
            InlineKeyboardButton("🔇", callback_data="mute"),
            InlineKeyboardButton("🔊", callback_data="unmute")
        ],
        [
            InlineKeyboardButton("🗑 Close Menu", callback_data="close")
        ]
    ]
)
