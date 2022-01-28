from pyrogram import filters
from pyrogram.handlers import MessageHandler
##############################################
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types import StreamVideoEnded
from pytgcalls import idle
from pytgcalls.types import AudioPiped,AudioVideoPiped
####################################################
import asyncio
#### Importing Only bot #########
from bot import bot
###### Importing Streamer #########
from code import app

async def main():

	##### Start bot ##########
	await bot.start()
	##### Start Player #######
	await app.start()

	await idle()

## Async Run #####

try:
	asyncio.get_event_loop().run_until_complete(main())
except:
	main.close()

