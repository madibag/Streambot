from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot import bot
import random
from config import Config
from code import app,plyer
from pytgcalls import StreamType
from pytgcalls.types import Browsers
from math import gcd
import pytgcalls
from pytgcalls.types.input_stream import (
        AudioVideoPiped, 
        AudioPiped,
        AudioImagePiped
    )
from pytgcalls.types.input_stream import (
        AudioParameters,
        VideoParameters
    )
from pyrogram.raw.functions.phone import (
        EditGroupCallTitle, 
        CreateGroupCall,
        ToggleGroupCallRecord,
        StartScheduledGroupCall 
    )

from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.base import InputChannel
################################################



async def check_if_active():
    try:
        peer = await bot.resolve_peer(Config.CHAT)

        pu = GetFullChannel(channel=peer)
        print(pu)
        call = await bot.send(data=pu)

        if call.full_chat.call:
            
            print("###############",call)

            return True , True
    except Exception as e:
        print(e,"here")
        return False , False

async def create_call():
    a = await plyer.resolve_peer(Config.CHAT)
    print(a)
    try:
        crete = await plyer.send(CreateGroupCall(
                        peer=(await plyer.resolve_peer(Config.CHAT)),
                        random_id=random.randint(10000, 999999999),
                        title = "Live Stream"
                        ))
        #print(crete,'created')
        return True
    except Exception as e:
        print(e,2)
        return False


async def join_call(link,width,height,referer='https://google.com',user_agent=Browsers().chrome_windows):
    try:
        
        if width and height:
            cwidth,cheight = resize_ratio(width,height,100)
            #print(user_agent)
            a = await app.join_group_call(
                            int(Config.CHAT),
                            AudioVideoPiped(
                                link,
                                video_parameters=VideoParameters(
                                    cwidth,
                                    cheight,
                                    Config.FPS,
                                ),
                                audio_parameters=AudioParameters(
                                    Config.BITRATE
                                ),
                                headers={
                                "User-Agent": ""+user_agent
                                }
                                ),
                            stream_type=StreamType().pulse_stream,
                        )

    except Exception as e:
        print(e,'joincall')
        #await create_call()

async def chang_stream(link,width,height,referer='',user_agent=Browsers().chrome_windows):

    if width and height:
            
            cwidth,cheight = resize_ratio(width,height,100)
            await app.change_stream(
                            int(Config.CHAT),
                            AudioVideoPiped(
                                link,
                                video_parameters=VideoParameters(
                                    cwidth,
                                    cheight,
                                    Config.FPS,
                                ),
                                audio_parameters=AudioParameters(
                                    Config.BITRATE
                                ),
                                headers={
                                    'User-Agent':user_agent,
                                    'Referer':referer,
                                    },
                                ),
                            stream_type=StreamType().pulse_stream,
                        )



def resize_ratio(w, h, factor):
    if w > h:
        rescaling = ((1280 if w > 1280 else w) * 100) / w
    else:
        rescaling = ((720 if h > 720 else h) * 100) / h
    h = round((h * rescaling) / 100)
    w = round((w * rescaling) / 100)
    divisor = gcd(w, h)
    ratio_w = w / divisor
    ratio_h = h / divisor
    factor = (divisor * factor) / 100
    width = round(ratio_w * factor)
    height = round(ratio_h * factor)
    return width - 1 if width % 2 else width, height - 1 if height % 2 else height #https://github.com/pytgcalls/pytgcalls/issues/118
