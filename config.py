import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24612695"))
    API_HASH = os.environ.get("API_HASH", "ba3159de9587c4364111fc40fe5ec6c8")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6837952381:AAFfYrM4qosgqEfr_dX5YyJq0C9VPf1hcEI")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "2052687693"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "http://t.me/Sandeepshekhawatbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
