from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28243586")
    API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6586622392:AAEZhdqa_0KifRh4kx9nZh5PyIzGHAuIknE") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://MADARA-UCHIHA:shubhamgaming33@madara-uchiha.ya7m1.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6827783925').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
