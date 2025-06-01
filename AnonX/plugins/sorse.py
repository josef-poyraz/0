import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint




import requests

async def check_subscription(user_id):
    channel_username = "KU_KX"  # معرف القناة الفعلي

    bot_token = "6046893597:AAE3zOhlKW3gferXfWXgc0aH6LSy5HJk4z4"  # رمز معرف البوت الخاص بك
    api_url = f"https://api.telegram.org/bot{bot_token}/getChatMember?chat_id=@{channel_username}&user_id={user_id}"
    
    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200 and data["ok"]:
        status = data["result"]["status"]
        if status == "left":
            return False
        else:
            return True

    return False

@app.on_message(
    command(["السورس", "سورس"])
    & ~filters.edited
    & filters.group
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/pvK757Rc/image.jpg",
        caption=f"""╭──── • ✭ • ────╮
✭ [على شُرفَةِ الانْتِظار](https://t.me/KU_KX)
✭ [جـوزيـّـف ϟ ¹](https://t.me/KU_LX)
╰──── • ✭ • ────╯
✭ ᴛʜᴇ ʙᴇѕᴛ ѕᴏᴜʀᴄᴇ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ جـوزيـّـف ϟ ¹ ›", url=f"https://t.me/KU_LX"), 
                ],[
                    InlineKeyboardButton(
                        "‹ على شُرفَةِ الانْتِظار ›", url=f"https://t.me/KU_KX"),
                ],[
                    InlineKeyboardButton(
                        "‹ للتنصيب راسلني ›", url=f"https://t.me/KU_LX"),
                ],

            ]

        ),

    )


@app.on_message(
    command(["غنيلي", "غني", "غ", "هولي غـنيلي"])
    & ~filters.edited
    & ~filters.channel
    & filters.group
)
async def ihd(client: Client, message: Message):
    user_id = message.from_user.id

    # التحقق من اشتراك المتخدم في القناة
    is_subscribed = await check_subscription(user_id)
    if not is_subscribed:
        channel_name = "على شُرفَةِ الانْتِظار"
        channel_url = "https://t.me/KU_KX"
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(channel_name, url=channel_url)]]
        )
        return await message.reply_text(
            "⚠️︙عذراً، عليك الانضمام الى قناة البوت أولاً :",
            reply_markup=keyboard
        )

    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ على شُرفَةِ الانْتِظار ›", url=f"https://t.me/KU_KX")
                ],
            ]
        )
    )





@app.on_message(
    command(["غنيلي", "غني", "غ", "هولي غـنيـلي"])
    & ~filters.edited
    & ~filters.channel
    & filters.group
)
async def ihd(client: Client, message: Message):
    user_id = message.from_user.id

    # التحقق من اشتراك المتخدم في القناة
    is_subscribed = await check_subscription(user_id)
    if not is_subscribed:
        channel_name = "على شُرفَةِ الانْتِظار"
        channel_url = "https://t.me/KU_KX"
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(channel_name, url=channel_url)]]
        )
        return await message.reply_text(
            "⚠️︙عذراً، عليك الانضمام الى قناة البوت أولاً :",
            reply_markup=keyboard
        )

    rs = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rs}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغنية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ على شُرفَةِ الانْتِظار ›", url=f"https://t.me/KU_KX")
                ],
            ]
        )
    )


@app.on_message(
    command(["رمزيات", f"ر", f"منشور", f"صوره", f"رمزيه"])
    & ~filters.edited
    & ~filters.channel
    & filters.group
)
async def ihd(client: Client, message: Message):
    user_id = message.from_user.id

    # التحقق من اشتراك المتخدم في القناة
    is_subscribed = await check_subscription(user_id)
    if not is_subscribed:
        channel_name = "على شُرفَةِ الانْتِظار"
        channel_url = "https://t.me/KU_KX"
        keyboard = InlineKeyboardMarkup(
            [[InlineKeyboardButton(channel_name, url=channel_url)]]
        )
        return await message.reply_text(
            "⚠️︙عذراً، عليك الانضمام الى قناة البوت أولاً :",
            reply_markup=keyboard
        )

    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار المنشور لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "‹ جـوزيـّـف ϟ ¹ ›", url=f"https://t.me/KU_LX")
                ],
            ]
        )
    )
