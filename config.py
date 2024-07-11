import re
from os import environ 

id_pattern = re.compile(r'^.\d+$')

class Config:
    API_ID = environ.get("API_ID", "25570025")
    API_HASH = environ.get("API_HASH", "62c95df09ad28778f17035b76abb3b22")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7201333775:AAHMuLKX4AHuP-YtMnjyquNqy153Kmf3GXE") 
    BOT_SESSION = environ.get("BOT_SESSION", "public") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "publicforward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1562935405').split()]
    AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002224312828').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')
    FORCE_SUB = environ.get("FORCE_SUB", "Silent_Bots")

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
