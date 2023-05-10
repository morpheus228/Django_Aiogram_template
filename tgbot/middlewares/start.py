from typing import Dict, Any

from aiogram import BaseMiddleware
from aiogram.types import Message

from tgbot.models import User


class StartMiddleware(BaseMiddleware):
    def __init__(self):
        pass

    async def __call__(self, handler, message: Message, data: Dict[str, Any]):
        if message.text == '/start' and User.objects.filter(id=message.from_user.id).first() is None:
            User.objects.create(id=message.from_user.id, username=message.from_user.username,
                                first_name=message.from_user.first_name, last_name=message.from_user.last_name)

        return await handler(message, data)
