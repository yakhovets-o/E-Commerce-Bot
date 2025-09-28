from enum import Enum
from dataclasses import dataclass


@dataclass
class UserCommandData:
    """Model user command"""

    command: str
    description: str


class UserCommands(Enum):
    """User commands"""

    START = UserCommandData("start", "ᯓ ✈︎ ⋆°•☁︎ Запуск бота")
    HELP = UserCommandData("help", "🆘 Список команд")
    CONTACTS = UserCommandData("contacts", "Контакты для связи")

    @property
    def command(self) -> str:
        return self.value.command

    @property
    def description(self) -> str:
        return self.value.description
