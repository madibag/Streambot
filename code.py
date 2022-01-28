from pytgcalls import PyTgCalls
import asyncio
from pytgcalls import idle
from pytgcalls.types import AudioPiped,AudioVideoPiped
from pyrogram import Client
################# MY CODE ###############################
from config import Config
from bot import bot

plyer = Client(Config.SESSION_STRING,
			 Config.API_ID, 
			 Config.API_HASH,
   	 		 plugins=dict(root="players"))

app = PyTgCalls(plyer)

