from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25570025")
    API_HASH = environ.get("API_HASH", "62c95df09ad28778f17035b76abb3b22")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6537146254:AAEsbF-TiOwbD4-vWS19Amjgc_21VeocaPM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1562935405').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
