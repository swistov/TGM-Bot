import logging
import keyboard as kb

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher

from config import TOKEN, PROXY, LOGFILE, ACCUWEATHER_ID, ACCUWEATHER_KEY, MY_ID, HOME_CHAT, EPTA_CHAT

from accuweather.weather import Accu
from apscheduler.schedulers.asyncio import AsyncIOScheduler

logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s',
                    level=logging.INFO, filename=LOGFILE)

# Start BOT
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('btn'))
async def process_callback_kb1btn1(callback_query: types.CallbackQuery):
    code_button = callback_query.data[-1]

    if code_button.isdigit():
        code_button = int(code_button)
        aw = Accu()

    if code_button == 1:
        weather = aw.weather_now(ACCUWEATHER_KEY, ACCUWEATHER_ID)
        await bot.answer_callback_query(
            callback_query.id, text=weather, show_alert=True)
    elif code_button == 2:
        weather = aw.weather_tomorrow()
        await bot.answer_callback_query(callback_query.id, text=weather, show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, f'Данная кнопка пока не настроена! code={code_button}')


@dp.message_handler(commands=['weather'])
async def get_weather_now(message: types.Message):
    await message.reply('Хочешь узнать погоду?', reply_markup=kb.weather_button)


async def msg():
    aw = Accu()
    weather = aw.weather_now(ACCUWEATHER_KEY, ACCUWEATHER_ID)
    for chat in HOME_CHAT, EPTA_CHAT:
        await bot.send_message(chat, weather)

if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(msg, 'interval', days=1, start_date="2010-12-06 07:00:00", timezone='Europe/Moscow')
    scheduler.start()

    executor.start_polling(dp)

