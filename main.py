import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.types.bot_command_scope_default import BotCommandScopeDefault
from aiogram.enums import ParseMode

from config import tg_config
from handlers import router as main_router
from menu_commands import user_menu


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    bot = Bot(
        token=tg_config.token.get_secret_value(),
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=user_menu(), scope=BotCommandScopeDefault())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
