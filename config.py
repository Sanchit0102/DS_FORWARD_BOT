import re
import os
from os import environ 

id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = environ.get("API_ID", "25570025")
    API_HASH = environ.get("API_HASH", "62c95df09ad28778f17035b76abb3b22")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7201333775:AAHMuLKX4AHuP-YtMnjyquNqy153Kmf3GXE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "publicforward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1562935405').split()]
    FORCE_SUB_ID = environ.get('FORCE_SUB_ID', '-1002224312828')
    FORCE_SUB = environ.get('FORCE_UPDATES_CHANNEL', True)
    FORCE_SUB = True if str(FORCE_SUB).lower() == "true" else False
    VERIFY_PIC = environ.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
