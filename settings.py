from dotenv import load_dotenv 
import os


load_dotenv()  

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "NONE")    

ADMINS_IDS = os.getenv("ADMIN_IDS", "").split(",")

ROLES = ["user", "seller", "admin"]

#aerich init -t settings.TORTOISE_ORM  
#aerich init-db 
#aerich migrate
#aeroch upgrade
TORTOISE_ORM = {
    "connections": {
        "default": "sqlite://db.sqlite3"
    },
    "apps": {
        "models": {
            "models": ["databases.models", "aerich.models"],
            "default_connection": "default"
        }
    }
}