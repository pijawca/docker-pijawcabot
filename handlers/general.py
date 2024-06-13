from handlers.abc import text_start
from aiogram import types, Dispatcher
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from misc import dp, bot


async def start(message: types.Message):
    await message.answer(text = text_start(username = message.from_user.username), 
                         parse_mode = ParseMode.MARKDOWN)

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(start, Command("start"))