from aiogram import types


def get_day_period(message: types.Message) -> str:
    """Returns a greeting depending on the time of day
    :param message: tg message obj
    :return: greeting
    """
    message_time_hour = (message.date.time().hour + 3) % 24
    match message_time_hour:
        case mess if mess in range(4, 12):
            return "Доброе утро"
        case mess if mess in range(12, 17):
            return "Добрый день"
        case mess if mess in range(17, 24):
            return "Добрый вечер"
        case _:
            return "Доброй ночи"
