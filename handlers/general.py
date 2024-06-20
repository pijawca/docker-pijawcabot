import abcd
from aiogram import types, Dispatcher
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from handlers.misc import dp, bot
from db.core import add_user, get_user_data


async def start(message: types.Message):
    user_id = message.from_user.id
    nickname = message.from_user.username
    who_is = 'user'
    add_user(user_id=user_id, nickname=nickname, who_is=who_is)
    
    get_user = get_user_data(user_id)
    
    await message.answer(text=abcd.text_start(username = nickname, who_is=get_user), 
                         parse_mode=ParseMode.MARKDOWN)
    

#adminka
async def dbconn(message: types.Message):
    await message.answer(text = abcd.text_dbconn())

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(start, Command('start'))
    dp.message.register(dbconn, Command('dbconn'))