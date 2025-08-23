from typing import Union
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from AviaxMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data="settingsback_helper",
        ),
    ]
    mark = second if START else first

    upl = InlineKeyboardMarkup(
        [
            # Row 1
            [
                InlineKeyboardButton(text=_["B_H_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(text=_["B_H_2"], callback_data="help_callback hb2"),
                InlineKeyboardButton(text=_["B_H_3"], callback_data="help_callback hb3"),
            ],
            # Row 2
            [
                InlineKeyboardButton(text=_["B_H_4"], callback_data="help_callback hb4"),
                InlineKeyboardButton(text=_["B_H_5"], callback_data="help_callback hb5"),
                InlineKeyboardButton(text=_["B_H_6"], callback_data="help_callback hb6"),
            ],
            # Row 3
            [
                InlineKeyboardButton(text=_["B_H_7"], callback_data="help_callback hb7"),
                InlineKeyboardButton(text=_["B_H_8"], callback_data="help_callback hb8"),
                InlineKeyboardButton(text=_["B_H_9"], callback_data="help_callback hb9"),
            ],
            # Row 4
            [
                InlineKeyboardButton(text=_["B_H_10"], callback_data="help_callback hb10"),
                InlineKeyboardButton(text=_["B_H_11"], callback_data="help_callback hb11"),
                InlineKeyboardButton(text=_["B_H_12"], callback_data="help_callback hb12"),
            ],
            # Row 5
            [
                InlineKeyboardButton(text=_["B_H_13"], callback_data="help_callback hb13"),
                InlineKeyboardButton(text=_["B_H_14"], callback_data="help_callback hb14"),
                InlineKeyboardButton(text=_["B_H_15"], callback_data="help_callback hb15"),
            ],
            # Row 6
            [
                InlineKeyboardButton(text=_["B_H_16"], callback_data="help_callback hb16"),
                InlineKeyboardButton(text=_["B_H_17"], callback_data="help_callback hb17"),
                InlineKeyboardButton(text=_["B_H_18"], callback_data="help_callback hb18"),
            ],
            # Row 7
            [
                InlineKeyboardButton(text=_["B_H_19"], callback_data="help_callback hb19"),
                InlineKeyboardButton(text=_["B_H_20"], callback_data="help_callback hb20"),
                InlineKeyboardButton(text=_["B_H_21"], callback_data="help_callback hb21"),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton(text=_["BACK_BUTTON"], callback_data="settings_back_helper")]]
    )


def private_help_panel(_):
    return [[InlineKeyboardButton(text=_["S_B_4"], url=f"https://t.me/{app.username}?start=help")]]
