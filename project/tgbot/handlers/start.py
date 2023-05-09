from aiogram import Router
from aiogram.types import Message

start_router = Router()


@start_router.message()
async def echo(message: Message):
    await message.answer(message.text)
