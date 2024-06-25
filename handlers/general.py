from handlers import abcd
from aiogram import types, Dispatcher
from aiogram.filters.command import Command
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from handlers.misc import bot
from db.core import add_user, get_users
from handlers.keyboards import user_kb, admin_kb, deal_kb, bots_kb, feedback


class give_rights(StatesGroup):
    get_user_id = State()

class Client_menu:
    async def start(message: types.Message):
        user_id=message.from_user.id
        username=message.from_user.username
        add_user(user_id, username)
        
        await message.answer(
            text=abcd.start(username, get_users(user_id)), 
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=user_kb())
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker=r'CAACAgIAAxkBAAEMXdJmeuKTXS0gm-oOfLoXcTc_kmENCQACKkcAAmHaaEirAAENkFgUrmg1BA')

    async def administration(message: types.Message):
        if get_users(message.from_user.id) == 'Администратор':
            await message.answer(
                text=abcd.text_open_button(message.text),
                reply_markup=admin_kb())
        else:
            await message.answer(
                text=abcd.denied_access(message.text))
            await bot.send_sticker(
                chat_id=message.chat.id,
                sticker=r'CAACAgIAAxkBAAEJtMtks8sbeOwMwVjhgqs7oqsyn3oyQQACbBQAAqhl2Unugzno4GtRUy8E')

        
    async def support(message: types.Message):
        await message.answer(text=abcd.text_open_button(message.text),
                             reply_markup=feedback())
        await bot.send_video(
            chat_id=message.chat.id,
            video=r'https://s9.gifyu.com/images/animation042e91e4ca542b38.gif')
        
    async def deal(message: types.Message):
        await message.answer(text=abcd.text_open_button(message.text),
                             reply_markup=deal_kb())
        
    async def bots(message: types.Message):
        await message.answer(text=abcd.text_open_button(message.text),
                             reply_markup=bots_kb())
    
class Administration_menu:
    async def dbconn(message: types.Message):
        await message.answer(text=abcd.text_dbconn())
    
    async def crypto(message: types.Message):
        await message.answer(text=abcd.crypto(),
                             parse_mode=ParseMode.MARKDOWN)
        
    async def pass2(message: types.Message):
        await message.answer(text=abcd.passed())
        
    async def pass3(message: types.Message):
        await message.answer(text=abcd.passed())
        
    async def pass4(message: types.Message):
        await message.answer(text=abcd.passed())
    
    async def back(message: types.Message):
        await message.answer(text=abcd.text_open_button(message.text),
                            reply_markup=user_kb())

async def process_callback(callback_query: CallbackQuery):
    data = callback_query.data
    if data == 'test_pay':
        await bot.send_message(callback_query.from_user.id, 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet')
    elif data == 'half_pay':
        await bot.send_message(callback_query.from_user.id, 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet')
    elif data == 'one_pay':
        await bot.send_message(callback_query.from_user.id, 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet')
    elif data == 'show_wallet':
        await bot.send_message(callback_query.from_user.id, abcd.show_wallet(),
                               parse_mode=ParseMode.MARKDOWN)
    elif data == 'strojstavbot':
        await bot.send_message(callback_query.from_user.id)
    elif data == 'coder_link':
        await bot.send_message(callback_query.from_user.id)
    elif data == 'support':
        await bot.send_message(callback_query.from_user.id)
    elif data == 'support0':
        await bot.send_message(callback_query.from_user.id)
    elif data == 'channel':
        await bot.send_message(callback_query.from_user.id)

def register_handlers_commands(dp: Dispatcher):
    dp.message.register(Client_menu.start, Command(commands=['start', 's']))
    dp.message.register(Client_menu.administration, lambda message: message.text in ['⚙️ Администрирование', '/a', '/admin'])
    dp.message.register(Client_menu.deal, lambda message: message.text in ['🤝 Сделка', '/d', '/deal'])
    dp.message.register(Client_menu.bots, lambda message: message.text in ['🔩 Список ботов', '/l', '/listbots'])
    dp.message.register(Client_menu.support, lambda message: message.text in ['💌 Связаться', '/f', '/feedback'])
    dp.message.register(Administration_menu.dbconn, lambda message: message.text == '🟨 Тест с базой')
    dp.message.register(Administration_menu.back, lambda message: message.text == '↩️ Назад')
    dp.message.register(Administration_menu.crypto, lambda message: message.text == 'Чек кошелька')
    dp.message.register(Administration_menu.pass2, lambda message: message.text == 'pass2') 
    dp.message.register(Administration_menu.pass3, lambda message: message.text == 'pass3')
    dp.message.register(Administration_menu.pass4, lambda message: message.text == 'pass4')
    dp.callback_query.register(process_callback)
