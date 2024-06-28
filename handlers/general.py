from handlers import abcd
from aiogram import types, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from handlers.misc import bot
from db.core import add_user, get_users
from handlers.keyboards import user_kb, admin_kb, deal_kb, bots_kb, feedback, pijawcatoday_kb


class MessagetopijawcaToday(StatesGroup):
    waiting_for_message = State()

class ClientMenu:
    async def start(message: types.Message):
        user_id = message.from_user.id
        username = message.from_user.username
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

class AdministrationMenu:
    async def dbconn(message: types.Message):
        await message.answer(text=abcd.text_dbconn())

    async def crypto(message: types.Message):
        await message.answer(text=abcd.crypto(),
                             parse_mode=ParseMode.MARKDOWN)

    async def pijawca_today(message: types.Message, state: FSMContext):
        await bot.send_message(chat_id=message.from_user.id, text=abcd.pijawcatoday())
        await state.set_state(MessagetopijawcaToday.waiting_for_message)
        
    async def handler_pijawca_today(message: types.Message):
        admin_message = message.text
        await message.reply(text=f'{admin_message}\n\nВсе верно?',
                            reply_markup=pijawcatoday_kb())

    async def pass3(message: types.Message):
        await message.answer(text=abcd.passed())

    async def pass4(message: types.Message):
        await message.answer(text=abcd.passed())

    async def back(message: types.Message):
        await message.answer(text=abcd.text_open_button(message.text),
                             reply_markup=user_kb())

async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data
    user_id = callback_query.from_user.id

    responses = {
        'test_pay': 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet',
        'half_pay': 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet',
        'one_pay': 'К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet',
        'show_wallet': abcd.show_wallet()
    }

    if data in responses:
        await bot.send_message(user_id, responses[data], parse_mode=ParseMode.MARKDOWN)
    elif data == 'strojstavbot':
        await bot.send_message(user_id)
    elif data == 'coder_link':
        await bot.send_message(user_id)
    elif data == 'support':
        await bot.send_message(user_id)
    elif data == 'support0':
        await bot.send_message(user_id)
    elif data == 'channel':
        await bot.send_message(user_id)
    elif data == 'yes':
        state_data = await state.get_data()
        print(state_data)
        admin_message = state_data.get('admin_message', '')
        await bot.send_message(chat_id='-1002193353022', text=admin_message)
        await bot.answer_callback_query(callback_query.id, text='Сообщение отправлено в группу!')
    elif data == 'no':
        await bot.answer_callback_query(callback_query.id, text='Сообщение было очищенно!')
        
    else:
        await bot.answer_callback_query(callback_query.id, text='Неизвестная команда')


def register_handlers_commands(dp: Dispatcher):
    dp.message.register(ClientMenu.start, Command(commands=['start', 's']))
    dp.message.register(ClientMenu.administration, lambda message: message.text in ['⚙️ Администрирование', '/a', '/admin'])
    dp.message.register(ClientMenu.deal, lambda message: message.text in ['🤝 Сделка', '/d', '/deal'])
    dp.message.register(ClientMenu.bots, lambda message: message.text in ['🔩 Список ботов', '/l', '/listbots'])
    dp.message.register(ClientMenu.support, lambda message: message.text in ['💌 Связаться', '/f', '/feedback'])
    dp.message.register(AdministrationMenu.dbconn, lambda message: message.text == '🟨 Тест с базой')
    dp.message.register(AdministrationMenu.back, lambda message: message.text == '↩️ Назад')
    dp.message.register(AdministrationMenu.crypto, lambda message: message.text == 'Чек кошелька')
    dp.message.register(AdministrationMenu.pijawca_today, lambda message: message.text == '📨 @pijawcatoday') 
    dp.message.register(AdministrationMenu.handler_pijawca_today, StateFilter(MessagetopijawcaToday.waiting_for_message)) 
    dp.message.register(AdministrationMenu.pass3, lambda message: message.text == 'pass3')
    dp.message.register(AdministrationMenu.pass4, lambda message: message.text == 'pass4')
    dp.callback_query.register(process_callback)
