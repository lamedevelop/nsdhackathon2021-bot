from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import os
import sys

from controllers.logger import Logger

def getToken():
    if 'BOT_TOKEN' in os.environ:
        return os.environ['BOT_TOKEN']
    else:
        Logger.error('Token does not exist')
        sys.exit(1)

bot = Bot(token=getToken())
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def chooseUniversity(message):
    pass

@dp.message_handler(commands=["income"])
async def chooseUniversity(message):
    pass

@dp.message_handler(commands=["outcome"])
async def chooseUniversity(message):
    pass

@dp.message_handler(commands=["new"])
async def chooseUniversity(message):
    pass

if __name__ == '__main__':
    Logger.info("Polling started")
    executor.start_polling(dp)
    Logger.info("Polling over")