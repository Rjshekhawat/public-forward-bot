from pyrogram import Client, __version__

from config import Config
from config import LOGGER

from user import User
import pyromod.listen


class Bot(Client):
    USER: User = "Pppp0080"
    USER_ID: int = 
1247783606
    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH "ba3159de9587c4364111fc40fe5ec6c8"
            api_id=Config.API_ID "24612695"
            plugins={
                "root": "plugins"
            },
            workers=10,
            bot_token=Config.BOT_TOKEN, "6837952381:AAFfYrM4qosgqEfr_dX5YyJq0C9VPf1hcEI"
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{usr_bot_me.username}  started! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped. Bye.")
