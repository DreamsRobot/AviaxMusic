from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app


# Main Help Menu
def help_main_menu(_):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton(text=_["B_S_1"], callback_data="help_section music")],
            [InlineKeyboardButton(text=_["B_S_2"], callback_data="help_section settings")],
            [InlineKeyboardButton(text=_["B_S_3"], callback_data="help_section advanced")],
            [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]
    )


# Music Help Submenu (B_S_1)
def help_music_menu(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["B_H_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(text=_["B_H_2"], callback_data="help_callback hb2"),
                InlineKeyboardButton(text=_["B_H_3"], callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(text=_["B_H_4"], callback_data="help_callback hb4"),
                InlineKeyboardButton(text=_["B_H_5"], callback_data="help_callback hb5"),
                InlineKeyboardButton(text=_["B_H_6"], callback_data="help_callback hb6"),
            ],
            [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="help_main")],
        ]
    )


# Advanced Help Submenu (B_S_3)
def help_advanced_menu(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["B_H_7"], callback_data="help_callback hb7"),
                InlineKeyboardButton(text=_["B_H_8"], callback_data="help_callback hb8"),
                InlineKeyboardButton(text=_["B_H_9"], callback_data="help_callback hb9"),
            ],
            [
                InlineKeyboardButton(text=_["B_H_10"], callback_data="help_callback hb10"),
                InlineKeyboardButton(text=_["B_H_11"], callback_data="help_callback hb11"),
                InlineKeyboardButton(text=_["B_H_12"], callback_data="help_callback hb12"),
            ],
            [
                InlineKeyboardButton(text=_["B_H_13"], callback_data="help_callback hb13"),
                InlineKeyboardButton(text=_["B_H_14"], callback_data="help_callback hb14"),
                InlineKeyboardButton(text=_["B_H_15"], callback_data="help_callback hb15"),
            ],
            [
                InlineKeyboardButton(text=_["B_H_16"], callback_data="help_callback hb16"),
                InlineKeyboardButton(text=_["B_H_17"], callback_data="help_callback hb17"),
                InlineKeyboardButton(text=_["B_H_18"], callback_data="help_callback hb18"),
            ],
            [
                InlineKeyboardButton(text=_["B_H_19"], callback_data="help_callback hb19"),
                InlineKeyboardButton(text=_["B_H_20"], callback_data="help_callback hb20"),
                InlineKeyboardButton(text=_["B_H_21"], callback_data="help_callback hb21"),
            ],
            [InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="help_main")],
        ]
    )

def support_menu(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["B_S_2_BTN1"], url="https://t.me/CFCBots"),
            InlineKeyboardButton(text=_["B_S_2_BTN2"], url="https://t.me/CloseFriendsCommunity"),
        ],
        [
            InlineKeyboardButton(text=_["B_S_2_BTN3"], url="https://t.me/emixlove"),
        ],
        [
            InlineKeyboardButton(text=_["B_S_2_BTN4"], callback_data="help_callback hb22"),
        ],
        [
            InlineKeyboardButton(text="🔙 Back", callback_data="help_callback back"),
        ],
    ]
    return InlineKeyboardMarkup(buttons)
