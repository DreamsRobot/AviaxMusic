HELP_1 = """<b>Play & Music Controls</b>

❍ /play [song/link] - Play a song in group VC
❍ /playforce [song/link] - Force play (clears queue first)
❍ /playlist - Show group playlist
❍ /video [song name] - Play video in VC
❍ /stream [url] - Stream live URL
❍ /seek [seconds] - Seek forward in track
❍ /seekback [seconds] - Seek backward in track
❍ /loop [1-10] - Loop the current song
❍ /loop disable - Disable loop
❍ /speed [0.5x/1.0x/1.5x/2.0x] - Change playback speed
❍ /shuffle - Shuffle the playlist queue
❍ /queue - Show current queue

"""

HELP_2 = """
<b>Admin Controls</b>

❍ /pause - Pause music
❍ /resume - Resume paused music
❍ /skip - Skip to next track
❍ /stop - Stop playback & clear queue
❍ /end - End the current voice chat
❍ /restart - Restart bot in group
❍ /player - Get interactive player panel
❍ /queue - Show queued tracks

"""

HELP_3 = """<b>User & Auth Management</b>

❍ /auth [username or reply] - Authorize user in group
❍ /unauth [username or reply] - Remove user from auth list
❍ /authusers - Show authorized users
❍ /block [username or reply] - Block user from using bot
❍ /unblock [username or reply] - Unblock blocked user
❍ /blockedusers - Show blocked users
❍ /gban [username or reply] - Globally ban user (all groups)
❍ /ungban [username or reply] - Unban globally banned user
❍ /gbannedusers - Show list of globally banned users

"""

HELP_4 = """<b>Broadcast & Chat Controls</b>

❍ /broadcast [message or reply] - Broadcast message to all served chats
❍ /broadcast_pin - Broadcast with pin option
❍ /broadcast_pin_loud - Broadcast with pin + notification
❍ /blacklistchat [chat_id] - Blacklist a chat from using bot
❍ /whitelistchat [chat_id] - Remove a chat from blacklist
❍ /blacklisted - Show list of blacklisted chats

"""

HELP_5 = """<b>System, Stats & Maintenance</b>

❍ /ping - Show bot’s ping
❍ /stats - Show bot statistics
❍ /sysstats - Show system usage (CPU, RAM, Disk)
❍ /maintenance [enable/disable] - Turn maintenance mode on/off
❍ /logger [enable/disable] - Enable or disable logging
❍ /clean - Clean cache & temp files

"""

HELP_6 = """<b>Channel & Extra Commands</b>

❍ /cplay [song name] - Play music in linked channel VC
❍ /cstop - Stop channel playback
❍ /cpause - Pause channel playback
❍ /cresume - Resume channel playback
❍ /cskip - Skip in channel VC
❍ /song [song name] - Download song from YouTube
❍ /video [song name] - Download video from YouTube
❍ /privacy - Show privacy info
❍ /privacy on - Enable strict privacy
❍ /privacy off - Disable strict privacy

"""

# help menu

HELP_7 = """<b>Help - Admin</b>
❍ /ban - Ban A User
❍ /dban - Delete the replied message banning its sender
❍ /tban - Ban A User For Specific Time
❍ /unban - Unban A User
❍ /listban - Ban a user from groups listed in a message
❍ /listunban - Unban a user from groups listed in a message
❍ /warn - Warn A User
❍ /dwarn - Delete the replied message warning its sender
❍ /rmwarns - Remove All Warning of A User
❍ /warns - Show Warning Of A User
❍ /kick - Kick A User
❍ /dkick - Delete the replied message kicking its sender
❍ /purge - Purge Messages
❍ /purge [n] - Purge "n" number of messages from replied message
❍ /del - Delete Replied Message
❍ /promote - Promote A Member
❍ /fullpromote - Promote A Member With All Rights
❍ /demote - Demote A Member
❍ /pin - Pin A Message
❍ /mute - Mute A User
❍ /tmute - Mute A User For Specific Time
❍ /unmute - Unmute A User
❍ /ban_ghosts - Ban Deleted Accounts
❍ /report | @admins | @admin - Report A Message To Admins.
❍ /invite - Send Group/SuperGroup Invite Link."""

HELP_8 = """ <b>Help - Admin Miscs</b>

❍ /set_chat_title - Change The Name Of A Group/Channel.
❍ /set_chat_photo - Change The PFP Of A Group/Channel.
❍ /set_user_title - Change The Administrator Title Of An Admin
❍ /antiservice [enable|disable]. 

"""

HELP_9 = """<b>⬇️Help - Autoapprove</b>

❍ command: /autoapprove

❍ This module helps to automatically accept chat join request send by a user through invitation link of your group

Modes:
❍ Automatic - Automatically accepts chat join request.
❍ Manual - A message will be send to the chat by tagging the admins. The admins can accept or decline the requests.

Use: /clear_pending Command to remove all pending user ID from DB. This will allow the user to send request again.
 """

HELP_10 = """<b>📶 Help - Blacklist</b>

❍ /blacklisted - Get All The Blacklisted Words In The Chat.
❍ /blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
❍ /whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
❍ /blacklist_chat [CHAT_ID] - Blacklist a chat.
❍ /whitelist_chat [CHAT_ID] - Whitelist a chat.
❍ /blacklisted - Show blacklisted chats.
"""

HELP_11 = """<b>🚮 Help - ChatBot</b>

❍ /chatbot [ENABLE|DISABLE] To Enable Or Disable ChatBot In Your Chat.
❍ /crypto [currency] Get Real Time value from currency given.
❍ /dice - Roll a dice.
"""

HELP_12 = """ <b>FEDRATION </b>
<b>👑 Fed Owner Only</b>
❍ /newfed <fed_name>: Creates a Federation, One allowed per user
❍ /renamefed <fed_id> <new_fed_name>: Renames the fed id to a new name
❍ /delfed <fed_id>: Delete a Federation, and any information related to it. Will not cancel blocked users
❍ /myfeds: To list the federations that you have created
❍ /fedtransfer <new_owner> <fed_id>:To transfer fed ownership to another person
❍ /fpromote <user>: Assigns the user as a federation admin. Enables all commands for the user under Fed Admins
❍ /fdemote <user>: Drops the User from the admin Federation to a normal User
❍ /setfedlog <fed_id>: Sets the group as a fed log report base for the federation
❍ /unsetfedlog <fed_id>: Removed the group as a fed log report base for the federation
❍ /fbroadcast : Broadcasts a messages to all groups that have joined your fed 

<b> 🔱 Fed Admins</b>
❍ /fban <user> <reason>: Fed bans a user
❍ /sfban: Fban a user without sending notification to chats
❍ /unfban <user> <reason>: Removes a user from a fed ban
❍ /sunfban: Unfban a user without sending a notification
❍ /fedadmins: Show Federation admin
❍ /fedchats <Fed_ID>: Get all the chats that are connected in the Federation

<b>User Commands</b>
❍ /fedinfo <Fed_ID>: Information about a federation.
❍ /fedadmins <Fed_ID>: List the admins in a federation.
❍ /joinfed <Fed_ID>: Join the current chat to a federation. A chat can only join one federation. Chat owners only.
❍ /leavefed: Leave the current federation. Only chat owners can do this.
❍ /fedstat: List all the federations that you have been banned in.
❍ /fedstat <user_ID>: List all the federations that a user has been banned in.
❍ /fedstat <Fed_ID>: Gives information about your ban in a federation.
❍ /fedstat <user_ID> <FedID>: Gives information about a user's ban in a federation.
❍ /chatfed: Information about the federation the current chat is in.

"""


HELP_13 = """<b>⏹️ Help - Filters</b>

❍ /filters To Get All The Filters In The Chat.
❍ /filter [FILTER_NAME] To Save A Filter(reply to a message).
❍ /stop [FILTER_NAME] To Stop A Filter.
❍ /stopall To delete all the filters in a chat (permanently).

<b>Checkout /markdownhelp to know more about formattings and other syntax.</b>
"""

HELP_14 = """<b>🔁 Help - Flood</b>

❍ /flood [ENABLE|DISABLE] - Turn flood detection on or off

"""

HELP_15 = """<b>🛜 Help - Greetings</b>

❍ /captcha [ENABLE|DISABLE] - Enable/Disable captcha.
❍ /set_welcome - Reply this to a message.
❍ /del_welcome - Delete the welcome message.
❍ /get_welcome - Get the welcome message.

<b>SET_WELCOME -></b>
The format should be something like below.
**Hi** {name} [{id}] Welcome to {chat}
button=[Duck, https://duckduckgo.com]
button2=[Github, https://github.com]
"""


HELP_16 = """<b>❇️ Help - Info - Inline </b>

❍ /info [USERNAME|ID] - Get info about a user.
❍ /chat_info [USERNAME|ID] - Get info about a chat.
❍ Send /inline for help related to inline.

<b>Example Usage</b>
@DreamSongRobot google github
"""

HELP_17 = """<b>🔔 Help - Karma</b>

❍ /karma_toggle [ENABLE|DISABLE] - Enable or Disable Karma System In Your Chat.
"""

HELP_18 = """<b>⏺️Help - Locks</b>

❍ Commands: /lock | /unlock | /locks [No Parameters Required]
❍ Parameters: messages | stickers | gifs | media | games | polls | inline  | url | group_info | user_add | pin
❍ Example : /lock all
"""

HELP_19 = """<b>❗️Help -  Misc</b>

❍ /asq - Ask a question
❍ /commit - Generate Funny Commit Messages
❍ /runs - Idk Test Yourself 
❍ /id - Get Chat_ID or User_ID
❍ /random - Generate Random Complex Passwords
❍ /cheat - Get Programming Related Help
❍ /tr - Translate A Message Ex: /tr en
❍ /json - Get parsed JSON response from a rest API.
❍ /arq - Statistics Of ARQ API.
❍ /webss - Take A Screenshot Of A Webpage
❍ /reverse - Reverse search an image.
❍ /carbon - Make Carbon from code.
❍ /tts - Convert Text To Speech.
❍ /autocorrect - Autocorrects the text.
❍ /pdf - Convert images to PDF.
❍ /markdownhelp - Sends mark down.
❍ /backup - Backup database
❍ /ping - Check ping of all 5 DCs.
"""

HELP_20 = """📝 Help - Notes:

❍ /notes To Get All The Notes In The Chat.
❍ /save [NOTE_NAME] To Save A Note.
❍ /delete [NOTE_NAME] To Delete A Note.
❍ /deleteall To delete all the notes in a chat (permanently).

<b>Checkout /markdownhelp to know more about formattings and other syntax.</b>

<b>🪈 Help - Pipes</b>

❍ /activate_pipe [FROM_CHAT_ID] [TO_CHAT_ID] [BOT|USERBOT]
❍ /deactivate_pipe [FROM_CHAT_ID] Deactivete a pipe.
❍ /show_pipes - Show all the active pipes.

<b>Here is the help for Quotly:</b>

❍ /q - To quote a message.
❍ /q [INTEGER] - To quote more than 1 messages.
❍ /q r - to quote a message with it's reply
"""

HELP_21 = """<b>📝 Rules for group</b>

❍ /rules: get the rules for this chat.
❍ /setrules: Reply to a message to set the rules for the chat.
❍ /clearrules: clear the rules for this chat.
 
<b>Here is the help for Shippering </b>
 
❍ /detect_gay - To Choose Couple Of The Day

<b>Here is the help for Stickers</b>

❍ /sticker_id - To get FileID of a Sticker.
❍ /get_sticker - get sticker as a photo and document.
❍ /kang - To kang a Sticker or an Image.

<b>Here is the help for Telegraph</b>
❍ /telegraph [Page name]: Paste styled text on telegraph.
❍ /iplookup [ip address] to get the details about that ip


<b>⚙️ Help - RSS</b>

❍ /add_feed [URL] - Add a feed to chat
❍ /rm_feed - Remove feed from chat

<b>Note: </b>
    - This will check for updates every 5 minutes.
    - You can only add one feed per chat.
    - Currently RSS and ATOM feeds are supported
"""

HELP_22 = """⎯⎯⎯⎯⎯⎯ ✦ 𝗔𝗟𝗜𝗩𝗘 ✦ ⎯⎯⎯⎯⎯⎯
🎶 DreamSong | MistiMusic 🎶

💠 24/7 High Quality Music  
💠 Lightning Fast Controls  
💠 Premium Group Management  

➥ @DreamSongRobot - ALIVE
➥ @MistiMusicRobot - ALIVE
⎯⎯⎯⎯⎯⎯ ✦ 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 ✦ ⎯⎯⎯⎯⎯⎯
"""


