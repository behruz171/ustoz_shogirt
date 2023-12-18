from aiogram import types, Dispatcher, executor, Bot
from dotenv import load_dotenv
import os
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)

dp = Dispatcher(bot)

async def on_startup(_):
    print("Bot ishladi")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)