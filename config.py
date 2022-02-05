import os
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ForceReply)

class Config(object):
	
	API_HASH = os.environ.get("API_HASH",'')
	API_ID = int(os.environ.get("API_ID",'')) 



	BOT_TOKEN = os.environ.get("BOT_TOKEN",'')

	CHAT = int(os.environ.get("CHAT",''))
	
	SESSION_STRING = os.environ.get("SESSION_STRING",'')
	################ Frame Per Second

	FPS = int(os.environ.get("FPS",'30'))#30
	BITRATE = int(os.environ.get("BITRATE",'36000'))
	########################### Help section###########################

	START = "Hi this is LiveStream bot please support us by DONATING to keep it alive"
	START_BUTTON = [[InlineKeyboardButton(text="⚙️ Update Channel ⚙️",url="https://t.me/Afconlive"),InlineKeyboardButton(text="ℹ️ Discussion Group",url="https://t.me/+KPgOj2yBBDE1ZTg0")],
		[InlineKeyboardButton(text="🆘 Help",callback_data="help_in_need"),InlineKeyboardButton(text="🗑 Close",callback_data="Close")]]

	HELP = "Just Send the stream link after /stream command and follow along\n/stream [link]"
	HELP_BUTTON = [[InlineKeyboardButton(text="🗑 Close",callback_data="Close")]]

	YES_NO = [[InlineKeyboardButton(text="✅ YES",callback_data="__YES__"),InlineKeyboardButton(text="✅ NO",callback_data="__NO__")]]

	CALL_STATUS=False
	CALL_ACTIVE = False
	CURRENT_CALL=None

