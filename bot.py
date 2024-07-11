import asyncio
import logging 
import logging.config
from database import db 
from config import Config  
from pyrogram import Client, __version__
from pyrogram.raw.all import layer 
from pyrogram.enums import ParseMode
from pyrogram.errors import FloodWait 

# logging.config.fileConfig('logging.conf')
# logging.getLogger().setLevel(logging.INFO)
# logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

class Bot(Client): 
    def __init__(self):
        super().__init__(
            Config.BOT_SESSION,
            api_hash=Config.API_HASH,
            api_id=Config.API_ID,
            plugins={
                "root": "plugins"
            },
            workers=50,
            bot_token=Config.BOT_TOKEN
        )
        self.log = logging

    # async def start(self):
    #     await super().start()
    #     me = await self.get_me()
    #     logging.info(f"{me.first_name} with for pyrogram v{__version__} (Layer {layer}) started on @{me.username}.")
    #     self.id = me.id
    #     self.username = me.username
    #     self.first_name = me.first_name
    #     self.set_parse_mode(ParseMode.DEFAULT)
    #     text = "**๏[-ิ_•ิ]๏ bot restarted !**"
    #     logging.info(text)
    #     success = failed = 0
    #     users = await db.get_all_frwd()
    #     async for user in users:
    #        chat_id = user['user_id']
    #        try:
    #           await self.send_message(chat_id, text)
    #           success += 1
    #        except FloodWait as e:
    #           await asyncio.sleep(e.value + 1)
    #           await self.send_message(chat_id, text)
    #           success += 1
    #        except Exception:
    #           failed += 1 
    # #    await self.send_message("venombotsupport", text)
    #     if (success + failed) != 0:
    #        await db.rmve_frwd(all=True)
    #        logging.info(f"Restart message status"
    #              f"success: {success}"
    #              f"failed: {failed}")

    # async def stop(self, *args):
    #     msg = f"@{self.username} stopped. Bye."
    #     await super().stop()
    #     logging.info(msg)

    def run(self):
            try:
                logger.info("Bot is starting...")
                super().run()
                logger.info("Bot is up and running.")
            except Exception as e:
                logger.error(f"An error occurred during bot execution: {e}")
            finally:
                logger.info("Bot is shutting down.")
     

if __name__ == "__main__":
    Bot().run()
