from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ForceReply)
from pyrogram import filters
from config import Config

##############
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from bot import bot

from config import Config
from code import app,plyer
import pytgcalls
from pytgcalls.types.input_stream import (
        AudioVideoPiped, 
        AudioPiped,
        AudioImagePiped
    )
from pyrogram.raw.functions.phone import (
        EditGroupCallTitle, 
        CreateGroupCall,
        ToggleGroupCallRecord,
        StartScheduledGroupCall 
    )
################################################
from .ffmpeg_status import get_width_height

from players import (
    check_if_active,
    create_call,
    join_call,
    chang_stream,
    )
#############
from bot import bot

@bot.on_message(filters.command(["stream"])& filters.private)
async def stream(c,m):
    if " " in m.text:
        spl = m.text.split(' ',2)
        try:
            link = '\'{}\''.format(spl[1])
            option = spl[2]
        except:
            link = '\'{}\''.format(spl[1])
            option = None

        chat_id = m.chat.id

        referer = 'Noref'
        user_agent = 'NoU-agnt'

        print(option)
        if option == None:
            pass
        elif option.startswith('user_agent - '):
            user_agent = option.split(' - ',1)[1]
        elif option.startswith('referer - '):
            referer =  option.split(' - ',1)[1]
        


        print(user_agent,referer)
        


        try:
            width,height = await get_width_height(link,user_agent,referer)
            print(width,height)
            if not width:
                await c.send_message(text="NO SOURCE FOUND",chat_id=chat_id,reply_to_message_id=m.message_id)
                return
            await c.send_message(text=f"Started streaming [Link]({link})",chat_id=chat_id,reply_to_message_id=m.message_id)
            if width and height:
                active,playing = await check_if_active()
                print(active,playing)
                ###############################################
                if active and playing:
                    await chang_stream(link,width,height,referer,user_agent)
                elif active and not playing:
                    await join_call(link,width,height,referer,user_agent)
                elif not active and not playing:
                    cr = await create_call()

                    print(cr)
                    if cr:
                        await join_call(link,width,height,referer,user_agent)
                    else:
                        print("Can't create a call")
                
        except Exception as e:
            print(e)


        


@bot.on_callback_query(filters.regex('Close'))
async def close(c,m):
    chat_id = m.from_user.id
    await c.delete_messages(chat_id=chat_id,message_ids=m.message.message_id)


@bot.on_callback_query(filters.regex('__YES__') or filters.regex('__NO__'))
async def yes_or_no(c,m):
    chat_id = m.from_user.id
    if m.data == "__YES__":
        pass
    else:
        pass


@bot.on_callback_query(filters.regex('help_in_need'))
async def help(c,m):


    #print(m)
    chat_id = m.from_user.id

    await c.send_message(
        chat_id=chat_id,
        text=Config.HELP,
        reply_markup=InlineKeyboardMarkup(Config.HELP_BUTTON)
        )

    

@bot.on_message(filters.command("start")& filters.private)
async def start(c,m):
    chat_id = m.chat.id
    reply_to = m.message_id
    await c.send_message(
        chat_id=chat_id,
        text=Config.START,
        reply_markup=InlineKeyboardMarkup(Config.START_BUTTON),
        reply_to_message_id=reply_to
        )
