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

from config import TOKEN, PROXY, LOGFILE
from temperature import weather_now as wn

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=LOGFILE)

# Start BOT
bot = Bot(token=TOKEN, proxy=PROXY)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code_button = callback_query.data[-1]

    if code_button.isdigit():
        code_button = int(code_button)

    if code_button == 1:
        def emo_but(weather_detail):
            if weather_detail == 'пасмурно':
                weather_emo = emojize(' ☁️')
            elif weather_detail == 'ясно':
                weather_emo = emojize(' ☀️')
            elif weather_detail == 'слегка облачно':
                weather_detail = 'переменная облачность'
                weather_emo = emojize(' ⛅')
            elif weather_detail == 'облачно':
                weather_emo = emojize(' ☁️')
            else:
                weather_emo = ''

            if len(weather_detail.split()) == 1:
                weather_detail = weather_detail.title()
            elif len(weather_detail.split()) == 2:
                weather_detail = weather_detail.split()[0].title() + ' ' + weather_detail.split()[1]

            return weather_detail + weather_emo

        reference_time = wn.get_reference_time(timeformat='date')
        temp_now = wn.get_temperature('celsius')['temp']
        wind = wn.get_wind()['speed']
        detail = emo_but(wn.get_detailed_status())
        humidity = wn.get_humidity()

        weather = f'Состояние на: {reference_time.strftime("%X %a %d-%m")}\n'\
                  f'За окном: {detail}\n' \
                  f'Температура: {temp_now} ℃\n' \
                  f'Скорость ветер: {wind} м/с\n' \
                  f'Влажность: {humidity} %'

        await bot.answer_callback_query(
            callback_query.id, text=weather, show_alert=True)
    elif code_button == 2:
        weather = 'Погоды не будет'
        await bot.answer_callback_query(callback_query.id, text=weather, show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, f'Данная кнопка пока не настроена! code={code_button}')


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
