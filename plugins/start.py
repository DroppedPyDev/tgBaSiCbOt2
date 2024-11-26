# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🪐

import os
import re
import asyncio
from pyrogram import Client, enums, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from bot import Bot
from config import OWNER_ID
from script import USER_START_TXT , OWNER_START_TXT

CMD = [ "/" , "!" , "." ]

user_start_btn = [
    [
        InlineKeyboardButton(text = 'Developer 💤', url = 'https://github.com/DroppedPyDev')
    ],
    [
        InlineKeyboardButton(text = 'Updates ♻️', url = 'https://t.me/DPDHubServer')
    ]
]

owner_start_btn = [
    [
        InlineKeyboardButton(text = 'Click >', callback_data = "next")
    ]
]

@Bot.on_message(filters.command("start", CMD) & filters.private)
async def start_msg(client: Client, message: Message):
    if message.from_user.id == OWNER_ID:
        await message.reply(
            text=OWNER_START_TXT,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(owner_start_btn)
        )
    else:
        await message.reply(
            text=USER_START_TXT,
            quote=True,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(user_start_btn)
        )
