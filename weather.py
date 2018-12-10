import asyncio
import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler

#from accuweather.weather import Accu
from bot import bot
from config import ACCUWEATHER_KEY, ACCUWEATHER_ID, MY_ID


async def msg():
    #aw = Accu()
    await bot.send_message(MY_ID, '123')


if __name__ == '__main__':
    scheduler = AsyncIOScheduler()
    scheduler.add_job(msg, 'interval', start_date='2010-12-06 08:43:00', seconds=5)
    scheduler.start()
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    # Execution will block here until Ctrl+C (Ctrl+Break on Windows) is pressed.
    try:
        asyncio.get_event_loop().run_forever()
    except (KeyboardInterrupt, SystemExit):
        pass
