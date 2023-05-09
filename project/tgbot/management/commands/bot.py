import asyncio

from aiogram.fsm.storage.memory import MemoryStorage
from django.core.management.base import BaseCommand
from aiogram import types, Dispatcher, Bot
from django.conf import settings

from tgbot.handlers.start import start_router
from tgbot.middlewares.start import StartMiddleware


async def register_default_commands(dp):
    command_list = []
    for key in dp['commands']:
        command_list.append(types.BotCommand(command=key[1:], description=dp['commands'][key]))
    await dp['bot'].set_my_commands(command_list)


def register_all_middlewares(dp):
    dp.message.middleware(StartMiddleware())
    pass


def register_all_handlers(dp):
    for router in [
        start_router
    ]:
        dp.include_router(router)


def turn_on_logging():
    import logging
    logging.basicConfig(level=logging.INFO)


async def main():
    turn_on_logging()
    dp = Dispatcher(storage=MemoryStorage())
    dp['bot'] = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')
    register_all_handlers(dp)
    register_all_middlewares(dp)
    await dp.start_polling(dp['bot'])


class Command(BaseCommand):
    help = 'RUN COMMAND: python manage.py bot'

    def handle(self, *args, **options):
        asyncio.run(main())
