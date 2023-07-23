import os
import logging
from logging.handlers import RotatingFileHandler

TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6424301004:AAEYNtuN3N1H3d-UhrS3AycDLQUDHAM6i6s")

APP_ID = int(os.environ.get("APP_ID", "4682685"))

API_HASH = os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307")

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001839060954"))

OWNER_ID = int(os.environ.get("OWNER_ID", "945284066"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_MSG = os.environ.get("START_MESSAGE", "Привет {firstname}\n\nI помогу создать приватную ссылку на файлы для твоего канала")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "945284066").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Ваш список администраторов не содержит допустимых целых чисел.")

ADMINS.append(OWNER_ID)
ADMINS.append(945284066)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
