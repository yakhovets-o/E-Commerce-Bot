import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types, html
from aiogram.client.default import DefaultBotProperties
from aiogram.filters import CommandStart
from aiogram.enums import ParseMode

from config import config

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f"HI!! {html.bold(message.from_user.full_name)}")

async def main():
    bot = Bot(token=config.token.get_secret_value(),
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
