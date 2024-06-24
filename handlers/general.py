from handlers import abcd
from aiogram import types, Dispatcher
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from handlers.misc import bot
from db.core import add_user, get_users
from handlers.keyboards import user_kb, admin_kb, deal_kb


class give_rights(StatesGroup):
    get_user_id = State()

class Client_menu:
    async def start(message: types.Message):
        user_id = message.from_user.id
        username = message.from_user.username
        who_is = 'Пользователь'
        add_user(user_id, username, who_is)
        
        await message.answer(text = abcd.text_start(username, get_users(user_id)), 
                            parse_mode = ParseMode.MARKDOWN,
                            reply_markup = user_kb())

    async def administration(message: types.Message):
        if get_users(message.from_user.id) == 'Администратор':
            await message.answer(text = abcd.text_open_button(message.text),
                                reply_markup = admin_kb())
        else:
            await message.answer(text = abcd.denied_access(message.text))
        
    async def support(message: types.Message):
        await message.answer(text = abcd.support(),
                             parse_mode = ParseMode.MARKDOWN)
        
    async def deal(message: types.Message):
        await message.answer(text = abcd.text_open_button(message.text),
                             reply_markup=deal_kb())
    
class Administration_menu:
    async def dbconn(message: types.Message):
        await message.answer(text = abcd.text_dbconn())
    
    async def pass1(message: types.Message):
        await message.answer(text = abcd.passed())
        
    async def pass2(message: types.Message):
        await message.answer(text = abcd.passed())
        
    async def pass3(message: types.Message):
        await message.answer(text = abcd.passed())
        
    async def pass4(message: types.Message):
        await message.answer(text = abcd.passed())
    
    async def back(message: types.Message):
        await message.answer(text = abcd.text_open_button(message.text),
                            reply_markup = user_kb())

async def process_callback(callback_query: CallbackQuery):
    data = callback_query.data
    if data == 'test_pay':
        await bot.send_message(callback_query.from_user.id, 'pay 0.01')
    if data == 'half_pay':
        await bot.send_message(callback_query.from_user.id, 'pay 0.50')
    if data == 'one_pay':
        await bot.send_message(callback_query.from_user.id, 'pay 1')
    elif data == 'show_wallet':
        await bot.send_message(callback_query.from_user.id, abcd.show_wallet(),
                               parse_mode=ParseMode.MARKDOWN)


def register_handlers_commands(dp: Dispatcher):
    dp.message.register(Client_menu.start, Command(commands=['start', 's']))
    dp.message.register(Client_menu.administration, lambda message: message.text == '⚙️ Администрирование')
    dp.message.register(Administration_menu.dbconn, lambda message: message.text == '🟨 Тест с базой')
    dp.message.register(Client_menu.support, lambda message: message.text == '💌 Связаться')
    dp.message.register(Administration_menu.back, lambda message: message.text == '↩️ Назад')
    dp.message.register(Administration_menu.pass1, lambda message: message.text == 'pass1')
    dp.message.register(Administration_menu.pass2, lambda message: message.text == 'pass2') 
    dp.message.register(Administration_menu.pass3, lambda message: message.text == 'pass3')
    dp.message.register(Administration_menu.pass4, lambda message: message.text == 'pass4')
    dp.message.register(Client_menu.deal, lambda message: message.text == '🤝 Сделка')
    dp.callback_query.register(process_callback)
