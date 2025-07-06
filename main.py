#import moduls
import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

#The main function checks the bot for unread messages from the user.
async def main():
    bot = Bot(token='your bots token')
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)

#we check whether the file main is startup, if so, we run the main function, if not, we do nothing.
if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
