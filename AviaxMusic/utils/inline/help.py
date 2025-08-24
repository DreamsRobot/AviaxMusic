from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


# Main Help Menu with 21 Buttons
def help_main_menu(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text=_["B_M_1"], callback_data="help_callback hb1"),
                InlineKeyboardButton(text=_["B_M_2"], callback_data="help_callback hb2"),
                InlineKeyboardButton(text=_["B_M_3"], callback_data="help_callback hb3"),
            ],
            [
                InlineKeyboardButton(text=_["B_M_4"], callback_data="help_callback hb4"),
                InlineKeyboardButton(text=_["B_M_5"], callback_data="help_callback hb5"),
                InlineKeyboardButton(text=_["B_M_6"], callback_data="help_callback hb6"),
            ],
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
            [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
        ]
    )


# Back Button
def help_back_markup(_):
    return InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("⬅️ Back", callback_data="help_main")]
        ]
    )
