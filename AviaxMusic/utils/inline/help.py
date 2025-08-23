from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AviaxMusic import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["B_M_1"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["B_M_2"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["B_M_3"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_M_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_M_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_M_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_H_1"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_H_2"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_H_3"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_H_4"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_H_5"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_H_6"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_H_7"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_H_8"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_H_9"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_H_10"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_H_11"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_H_12"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["B_H_13"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["B_H_14"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["B_H_15"],
                    callback_data="help_callback hb6",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons

