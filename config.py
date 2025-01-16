from os import environ

API_ID = int(environ.get("API_ID", "22904772"))
API_HASH = environ.get("API_HASH", "ab5c7644dad9ab3ecd6a60c2da229d6b")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Make Bot Admin In Log Channel With Full Rights
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1001662168594"))
ADMINS = int(environ.get("ADMINS", "2077682354"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "mongodb+srv://pahduhshkkop:TDS_MAN_09@cluster0.zitsd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = environ.get("DB_NAME", "vjjoinrequetbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
