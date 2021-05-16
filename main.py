from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

import os
import sys
import requests

from controllers.logger import Logger
from controllers.keyboard import Keyboard

logger = Logger()


def getToken():
    if 'BOT_TOKEN' in os.environ:
        return os.environ['BOT_TOKEN']
    else:
        logger.error('Token does not exist')
        sys.exit(1)


def getUrl():
    if 'API_URL' in os.environ:
        return os.environ['API_URL']
    else:
        logger.error('URL does not exist')
        sys.exit(1)


url = f"http://{getUrl()}/api"

# bot = Bot(token=getToken())
bot = Bot(token="1787537307:AAFOKVKTGeleb0PoeD6NduT0wVPz1XYTPCM")
dp = Dispatcher(bot)


def isUserExist(message):
    r = requests.get(f"{url}/user/exist?tg_id={message['from']['id']}")
    if r.json()['data']:
        return True
    else:
        return False


async def sendHello(message, func):
    reply = f'Привет!\nНапиши мне что-нибудь!'''
    await message.reply(reply,  reply_markup=func)
    logger.botMessage(reply.replace("\n", " "))


async def sendGoobye(message, func):
    reply = f'Привет!\nПройдите регистрацию!'
    await message.reply(reply, reply_markup=func)
    logger.botMessage(reply.replace("\n", " "))


@dp.message_handler(commands=["start"])
async def botStart(message):
    logger.userMessage(message)
    if isUserExist(message):
        await sendHello(message, Keyboard.inline_option_picker())
    else:
        await sendGoobye(message, Keyboard.inline_option_picker())


@dp.message_handler(commands=["income"])
async def botIncome(message):
    logger.userMessage(message)
    if isUserExist(message):
        r = requests.get(f"{url}/income?user_id={message['from']['id']}")


@dp.message_handler(commands=["outcome"])
async def botOutcome(message):
    logger.userMessage(message)
    if isUserExist(message):
        r = requests.get(f"{url}/outcome?user_id={message['from']['id']}")


@dp.message_handler(commands=["unread"])
async def botUnread(message):
    logger.userMessage(message)
    if isUserExist(message):
        r = requests.get(f"{url}/unread?user_id={message['from']['id']}")


@dp.message_handler()
async def botMessageReciever(message):
    logger.userMessage(message)
    if message["text"] in ['income', 'outcome', 'unread']:
        r = requests.get(f"{url}/{message['text']}?user_id=2")
        if len(r.json()['data']) != 0:
            await message.reply(' '.join(str(x) for x in r.json()['data']))
        else:
            await message.reply('Сообщений нет')

    else:
        botAnswer = f'Привет, {message["from"]["first_name"]}!\nХочешь пообщаться?'
        await message.reply(botAnswer)
        logger.botMessage(botAnswer)


if __name__ == '__main__':
    logger.info("Polling started")
    executor.start_polling(dp)
    logger.info("Polling over")
