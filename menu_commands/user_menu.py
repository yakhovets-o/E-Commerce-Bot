from aiogram.types import BotCommand
from utils import UserCommands


def user_menu() -> list:
    """Create user menu"""

    menu = [
        BotCommand(
            command=user_command.value.command,
            description=user_command.value.description,
        )
        for user_command in UserCommands
    ]

    return menu
