# import asyncio
import logging
import keyboard as kb

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
# from aiogram.types.message import ContentType
# from aiogram.utils.markdown import text, bold, italic, code, pre
# from aiogram.utils.markdown import text
# from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions
# from aiogram.types import ParseMode

from config import TOKEN, PROXY, PROXY_AUTH
from temperature import weather_now as wn

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO)

# Start BOT
bot = Bot(token=TOKEN, proxy=PROXY, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code_button = callback_query.data[-1]
    if code_button.isdigit():
        code_button = int(code_button)

    if code_button == 1:
        temp_now = wn.get_temperature('celsius')['temp']
        wind = wn.get_wind()['speed']
        detail = wn.get_detailed_status()
        humidity = wn.get_humidity()
        if detail == 'пасмурно':
            detail = detail.title() + emojize(' ☁️')

        weather = f'За окном: {detail}\n' \
                  f'Температура: {temp_now} C\n' \
                  f'Скорость ветер: {wind} м/с\n' \
                  f'Влажность: {humidity} %'
        await bot.answer_callback_query(
            callback_query.id, text=weather, show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, f'Данная кнопка пока не настроена! code={code_button}')


# @dp.message_handler(commands=['start'])
# async def process_start_command(msg: types.Message):
#     await msg.reply('Привет!', reply_markup=kb.greet_kb)
#
#
# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     msg = text(
#         'Если нужно узнать погоду:',
#         '/weather и выбери день',
#         sep="\n"
#     )
#
#     await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
#

@dp.message_handler(commands=['weather'])
async def get_weather_now(message: types.Message):
    await message.reply('Хочешь узнать погоду?', reply_markup=kb.weather_button)


# @dp.message_handler(commands=['rm'])
# async def process_start_command(msg: types.Message):
#     await msg.reply('Пока!', reply_markup=kb.del_kb)

#
# @dp.message_handler(content_types=ContentType.PHOTO)
# async def photo_message(msg: types.Message):
#     try:
#         await bot.send_message(msg.chat.id, text('1\n1\n1\n1\n1\n' * 5))
#     except:
#         print('I can`n send message')
#     print(f'{msg}')
#     file_id = msg.photo[0]['file_id']
#     await bot.download_file_by_id(file_id=file_id, destination=f'demo-media/pics/{file_id}.jpg')
#
#
#
# @dp.message_handler()
# async def echo_message(msg: types.Message):
#     await bot.send_message(msg.from_user.id, msg.text)
#
#
# @dp.message_handler(content_types=ContentType.ANY)
# async def unknown_message(msg: types.Message):
#     message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
#                         italic('\nЯ просто напомню,'), 'что есть',
#                         code('команда'), '/help')
#     await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
#     print(f'{msg}')

if __name__ == '__main__':
    executor.start_polling(dp)
