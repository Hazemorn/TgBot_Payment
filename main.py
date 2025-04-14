import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from app.handlers import router
from common import configure_logging

bot = Bot(token=TOKEN)
dp = Dispatcher() 


async def main():
    dp.include_router(router)
    await dp.start_polling(bot, skip_updates=True)

# async def cmd_bot_stop():
#     await dp.stop_polling() 
#     await message.answer("Bot has been stopped.")  
#     #await bot.close()  
#     #cmd_bot_stop() 
#     pass


if __name__ == '__main__':
    configure_logging(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:# Control + C
        print('Exit')