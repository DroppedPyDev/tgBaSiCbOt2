# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿

from aiohttp import web
from route import routes
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, API_ID, LOGGER, BOT_WORKERS, PORT, BOT_TOKEN
    
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=API_ID,
            bot_token=BOT_TOKEN,
            plugins={
                "root": "plugins"
            },
            workers=BOT_WORKERS
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        print("Now, go to telegram and start your Bot\nA suprise is waiting for you there 😍")
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()
        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"DroppedPyDev 🕊️")
       
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
