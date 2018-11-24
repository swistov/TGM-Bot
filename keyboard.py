from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

weather_button = InlineKeyboardMarkup(row_width=2)
weather_now = InlineKeyboardButton('Погода сейчас', callback_data='btn1')
weather_tomorrow = InlineKeyboardButton('Погода завтра', callback_data='btn2')
weather_button.add(weather_now, weather_tomorrow)
