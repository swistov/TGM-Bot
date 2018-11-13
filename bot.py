import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN, PROXY, PROXY_AUTH
from temperature import w


logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)


bot = Bot(token=TOKEN, proxy=PROXY, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.reply('Привет!\nИспользуй /help, '
#                         'чтобы узнать список доступных команд!')
#
#
# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     msg = text(bold('Я могу ответить на следующие команды:'),
#                '/voice', '/photo', '/group', '/note', '/file, /testpre', sep='\n')
#     await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
#
#

@dp.message_handler(commands=['weather'])
async def get_weather_now(msg: types.Message):
    temp = w.get_temperature('celsius')['temp']
    temp_max = w.get_temperature('celsius')['temp_max']
    temp_min = w.get_temperature('celsius')['temp_min']
    message = f'Сейчас:\t{temp}\nМаксимальная:\t{temp_max}\nМинимальная:\t{temp_min}'

    await msg.reply(message)


@dp.message_handler(content_types=ContentType.PHOTO)
async def photo_message(msg: types.Message):
    try:
        await bot.send_message(msg.chat.id, text('1\n1\n1\n1\n1\n' * 5))
    except:
        print('I can`n send message')
    # print(f'{msg}')
    # file_id = msg.photo[0]['file_id']
    # await bot.download_file_by_id(file_id=file_id, destination=f'demo-media/pics/{file_id}.jpg')


# @dp.message_handler(content_types=ContentType.ANY)
# async def unknown_message(msg: types.Message):
#     message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
#                         italic('\nЯ просто напомню,'), 'что есть',
#                         code('команда'), '/help')
#     await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
#     print(f'{msg}')

if __name__ == '__main__':
    executor.start_polling(dp)
