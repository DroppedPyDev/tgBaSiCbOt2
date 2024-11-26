
import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler
from time import time

#Your API ID from my.telegram.org
API_ID = os.environ.get("API_ID", "2195622")

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fe9031812730b93d59b43a33b1db17ca")

#Your Telegram Bot's API Token from @BotFather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7024917939:AAH1F9VhBNfWBvJV73NLumA3CbzYGpO9xLs")

#Get your Telegram ID from @tgBaSiCbOt using "/id" command.
OWNER_ID = os.environ.get("OWNER_ID", "1981831553")

#No Need to Change This 
PORT = os.environ.get("PORT", "8080")

#No need to Change This 
BOT_WORKERS = int(os.environ.get("BOT_WORKERS", "4"))

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
  
