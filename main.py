import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router


async def main():
    bot = Bot(token='7840065320:AAF5vd8rIAMLg8SMdsjyL-71XW1oK_8cs2Y')
    dp = Dispatcher()
    dp.include_routers(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
