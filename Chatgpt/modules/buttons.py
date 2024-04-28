# CREDITS
# TELEGRAM : @Mr_Sukkun
#  GITHUB : NOOB-MUKESH

from pyrogram.types import InlineKeyboardButton as IKB, InlineKeyboardMarkup as IKM
from config import *
from random import choice
from .. import Mukesh

import requests,base64

def send():
    x=base64.b64decode('aHR0cHM6Ly9naXRodWIuY29tL05vb2ItbXVrZXNoL0NoYXRncHQtYm90').decode("utf-8")
    return x

xy=send()  

START = f"""⋄ مرحبا بك انا

↢ يمكنك طرح علي عدد لا نهائي من الاسئله

↢ انا شات جي بي تي ، اي انني نموذج لغوي آلي كبير تم تدريبه باستخدام تقنية الذكاء الاصطناعي لتوفير الإجابات والمحادثات للمستخدمين في مختلف المواضيع والمجالات. فهل يمكنني مساعدتك في شيء معين؟"""
SOURCE_TEXT = f"""<b>
๏ ʜᴇʏ, ɪ ᴀᴍ <a href="https://t.me/{Mukesh.username}"> {Mukesh.name} </a>
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ</b>
"""
HELP = f"""<b>➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ  {Mukesh.mention}
/chatgpt <prompt> ᴇxᴀᴍᴘʟᴇ: `/chatgpt write shorts notes of electricity`
/bard <prompt> ᴇxᴀᴍᴘʟᴇ: `/bard write a simple flask app in python.`
/blackbox <prompt> ᴇxᴀᴍᴘʟᴇ: `/blackbox write a simple website using python.`
/ping ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.
/source Tᴏ ɢᴇᴛ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ,
/help Tᴏ ɢᴇᴛ ʜᴇʟᴘ   
/start Tᴏ sᴛᴀʀᴛ ʙᴏᴛ
/stats Tᴏ ɢᴇᴛ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ


"""

x = ["❤️", "🎉", "✨", "🪸", " 🎉 ", " 🎈 ", "🎯"]
g = choice(x)


MAIN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB(text="ʜᴇʟᴘs", callback_data="HELP"),
    ],
    [
        IKB(text="sᴏᴜʀᴄᴇ ", callback_data="HELP_source"),
        
        IKB(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID),
]
]

PNG_BTN = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),
    ],
    [
        IKB("sᴜᴘᴘᴏʀᴛ",
            url=f"https://t.me/{SUPPORT_GRP}",
        ),
    ],
]

gpt_button = [
    [
        IKB(
            text="ᴀᴅᴅ ᴍᴇ",
            url=f"https://t.me/{Mukesh.username}?startgroup=true",
        ),

        IKB("ᴅᴇᴠᴇʟᴏᴘᴇʀ", user_id=OWNER_ID)
    ],
]



HELP_BACK = [

    [
        IKB("ʙᴀᴄᴋ", callback_data="HELP_BACK"),
    ],
]

SOURCE_BUTTONS = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ", callback_data="HELP_hurr")],
        [
            IKB(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
            IKB(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK")
        ]
    ]
)
SOURCE_BUTTON = IKM(
    [
        [IKB("sᴏᴜʀᴄᴇ" ,url=xy)
        ]
    ]
)
