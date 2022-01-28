import asyncio
import json

    
async def get_width_height(link,user_agent='',referer=''):

    ffprobe_cmd = ["ffprobe", "-i",link,"-v", "error", "-select_streams", "v", "-show_entries", "stream=width,height", "-of", "json","-user_agent",user_agent,"-referer",referer ]

    process = await asyncio.create_subprocess_exec(
        *ffprobe_cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    output, err = await process.communicate()
    stream = output.decode('utf-8')
    out = json.loads(stream)
    try:
        n = out.get("streams")
        if n:
            width=n[0].get("width")
            height=n[0].get("height")

            return width, height
        else:
            width, height = False, False
            
    except Exception as e:
        width, height = False, False

    return width, height
