import os
import logging
import pyrogram
from decouple import config

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# vars
APP_ID = 7939198
API_HASH = "eb8a70c3ced65165a42a20c549ee704a"
BOT_TOKEN = "2083760091:AAEglAfYNzzEOIIL6bk6dEe5Jl0IblJS-4I"

if __name__ == "__main__" :
    print("Starting Bot...")
    plugins = dict(root="PyroBot/plugins")
    app = pyrogram.Client(
        "BotzHub",
        bot_token=BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        plugins=plugins
    )
    app.run()
    
print("started mrunals bot")
