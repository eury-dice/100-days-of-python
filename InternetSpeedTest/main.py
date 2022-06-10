from internetspeedbot import InternetSpeedBot
from os import environ

UPLOAD_MIN = float(environ["UPLOAD_MIN"])
DOWNLOAD_MIN = float(environ["DOWNLOAD_MIN"])

bot = InternetSpeedBot(UPLOAD_MIN, DOWNLOAD_MIN)
bot.get_internet_speed()
