from telethon import TelegramClient
from decouple import config
import logging
import os
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

if 'API_ID' and 'API_HASH' in os.environ:
    api_id = int(os.environ.get("API_ID", 12345))
    api_hash = os.environ.get("API_HASH")
else:
    api_id = config("API_ID", cast=int)
    api_hash = config("API_HASH")

try:
    if 'BOT_TOKEN' and 'MONGO_URL' in os.environ:
        bot_token = os.environ.get("BOT_TOKEN")
        mongo = os.environ.get("MONGO_URL")
    else:
        bot_token = config("BOT_TOKEN")
        mongo = config("MONGO_URL")
except Exception as e:
    logging.warning(e)
    exit(0)


data = []
download_dir = "downloads/"
if not os.path.isdir(download_dir):
    os.makedirs(download_dir)

try:
    mongo_db = AsyncIOMotorClient(mongo)
except Exception as e:
    logging.warning(e)
    exit(0)

bot_db = mongo_db["VideoEncoder"]

try:
    BotzHub = TelegramClient("BotzHub", api_id, api_hash).start(bot_token=bot_token)
except Exception as e:
    logging.info(f"Error\n{e}")
    exit(0)
