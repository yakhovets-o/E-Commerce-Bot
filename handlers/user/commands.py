from aiogram import Router, types, html
from aiogram.filters import CommandStart, Command

from utils import UserCommands, get_day_period
from config import tg_config

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    text = f"{get_day_period(message)}! {(html.bold(html.quote(message.from_user.full_name)))}"
    await message.answer(text=text)


@router.message(Command(UserCommands.HELP.command))
async def cmd_help(message: types.Message) -> None:
    await message.answer(text="подмога в пути")


@router.message(Command(UserCommands.CONTACTS.command))
async def cmd_contact(message: types.Message):
    text = f"⌯⌲ tg: {html.italic(tg_config.admin)}\n\n🖂 email: {html.italic(tg_config.email)}"
    await message.answer(text=text)
