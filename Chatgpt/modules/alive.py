# -----------CREDITS -----------
# telegram : @Mr_Sukkun
# github : noob-mukesh
from pyrogram import filters
import asyncio, time
from .. import Mukesh
from config import START_IMG
from ..modules.buttons import *



@Mukesh.on_message(
    filters.command(["سرعه البوت", "alive"], prefixes=["+", "/", "", "?", "$", "&", "."])
)
async def ping(_, message):
    start = time.time()
    t = "↢ انتظر جاري فحص سرعه البوت..."
    txxt = await message.reply(t)
    await asyncio.sleep(0.25)
    await txxt.edit_text("انتظر 3 ثواني 🚦")
    await asyncio.sleep(0.35)
    await txxt.delete()
    end = time.time()
    ms = str(round((end - start) * 1000, 3)) + " ᴍs"
    await message.reply_photo(
        photo=START_IMG,
        caption=f"اهلا عزيزي\n{Mukesh.mention} البوت شغال بدون اعطال حتي الان سرعتة : {ms} \n\n**صنع بواسطة  @WX_PM",
        reply_markup=IKM(PNG_BTN),
    )