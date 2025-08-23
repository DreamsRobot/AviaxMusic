from typing import Union
from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from AviaxMusic import app
from AviaxMusic.utils.database import get_lang
from AviaxMusic.utils.decorators.language import LanguageStart, languageCB
from AviaxMusic.utils.inline.help import help_main_menu, help_music_menu, help_advanced_menu
from config import BANNED_USERS, START_IMG_URL, SUPPORT_GROUP
from strings import get_string, helpers


# Start Help (Private)
@app.on_message(filters.command(["help"]) & filters.private & ~BANNED_USERS)
async def helper_private(client, message: types.Message):
    language = await get_lang(message.chat.id)
    _ = get_string(language)
    await message.reply_photo(
        photo=START_IMG_URL,
        caption=_["help_1"].format(SUPPORT_GROUP),
        reply_markup=help_main_menu(_),
    )


# Switch between Menus
@app.on_callback_query(filters.regex("help_section") & ~BANNED_USERS)
@languageCB
async def help_sections(client, CallbackQuery, _):
    section = CallbackQuery.data.split()[1]
    if section == "music":
        await CallbackQuery.edit_message_reply_markup(reply_markup=help_music_menu(_))
    elif section == "advanced":
        await CallbackQuery.edit_message_reply_markup(reply_markup=help_advanced_menu(_))
    else:
        await CallbackQuery.answer("⚙️ Settings not added yet", show_alert=True)


# Back to Main Menu
@app.on_callback_query(filters.regex("help_main") & ~BANNED_USERS)
@languageCB
async def back_to_main(client, CallbackQuery, _):
    await CallbackQuery.edit_message_reply_markup(reply_markup=help_main_menu(_))


# Handle Help Callback (hb1..hb21)
@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    cb = CallbackQuery.data.strip().split(None, 1)[1]
    text = getattr(helpers, f"HELP_{cb[2:]}", "ℹ️ No help available for this.")
    await CallbackQuery.edit_message_text(text, reply_markup=help_main_menu(_))



elif callback == "bs2":
    await query.message.edit_text(
        "Choose from the Support Menu below 👇",
        reply_markup=support_menu(_)
    )

elif callback == "hb22":
    await query.message.edit_text(
        HELP_22,
        reply_markup=help_back_markup(_)
    )

