import re
from os import environ 

id_pattern = re.compile(r'^.\d+$') 

class Config:
    API_ID = environ.get("API_ID", "21701469")
    API_HASH = environ.get("API_HASH", "ae456165cc04a86ee38bd8ced7dae0e3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7017050619:AAE99kOJhQcbcsLAJNuWgHnJNsLZG4h72hM") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://rasy46765:uxDpwzp7DDHIKnCj@cluster0.rakmbj7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-2bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1562935405').split()]
    ADMIN = BOT_OWNER_ID
    FORCE_SUB = environ.get('FORCE_SUB', '-1002158291506') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
