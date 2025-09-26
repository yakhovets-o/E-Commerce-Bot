from aiogram import Router, types, html
from aiogram.filters import CommandStart

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: types.Message) -> None:
    await message.answer(f"HI!! {html.bold(message.from_user.full_name)}")
