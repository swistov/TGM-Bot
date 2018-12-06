from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

weather_button = InlineKeyboardMarkup(row_width=2)
weather_now = InlineKeyboardButton('Weather', callback_data='btn1')
weather_tomorrow = InlineKeyboardButton('Weather tomorrow', callback_data='btn2')
weather_button.add(weather_now, weather_tomorrow)
