from pyrogram.types import InlineKeyboardButton
import config
from AviaxMusic import app


# Start Panel for adding bot to groups
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], 
                url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], 
                url=config.SUPPORT_GROUP
            ),
        ],
    ]
    return buttons


# Private Panel for /start in private chat
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["B_S_1"], 
                callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text=_["B_S_2"], 
                url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["B_S_2"], 
                url=config.SUPPORT_GROUP
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["B_S_4"],
                url=f"https://t.me/{app.username}?startgroup=true"
            )
        ],
    ]
    return buttons
