# AviaxMusic/plugins/playmode.py
from pyrogram import Client, filters

@Client.on_message(filters.command("playmode"))
async def playmode_command(_, message):
    await message.reply_text("Playmode feature is not yet implemented.")
