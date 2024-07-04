from handlers import text
from aiogram import types, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import InputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from handlers.misc import bot
from db.core import add_user, get_users
from handlers.keyboards import user_kb, admin_kb, deal_kb, bots_kb, feedback_kb, send_to_kb
from listgroups import groups


class groups(StatesGroup):
    waiting_for_message = State()


class ClientMenu:
    async def start(message: types.Message):
        user_id = message.from_user.id
        username = message.from_user.username
        add_user(user_id, username)

        await message.answer(
            text=text.start(username, get_users(user_id)),
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=user_kb()
        )
        await bot.send_sticker(
            chat_id=message.chat.id,
            sticker=r'CAACAgIAAxkBAAEMXdJmeuKTXS0gm-oOfLoXcTc_kmENCQACKkcAAmHaaEirAAENkFgUrmg1BA'
        )

    async def administration(message: types.Message):
        if get_users(message.from_user.id) == 'Администратор':
            await message.answer(
                text=text.default_message(message.text),
                reply_markup=admin_kb()
            )
        else:
            await message.answer(
                text=text.denied_access(message.text)
            )
            await bot.send_sticker(
                chat_id=message.chat.id,
                sticker=r'CAACAgIAAxkBAAEJtMtks8sbeOwMwVjhgqs7oqsyn3oyQQACbBQAAqhl2Unugzno4GtRUy8E'
            )

    async def support(message: types.Message):
        await message.answer(
            text=text.default_message(message.text),
            reply_markup=feedback_kb()
        )
        await bot.send_video(
            chat_id=message.chat.id,
            video=r'https://s9.gifyu.com/images/animation042e91e4ca542b38.gif'
        )

    async def deal(message: types.Message):
        await message.answer(
            text=text.default_message(message.text),
            reply_markup=deal_kb()
        )

    async def bots(message: types.Message):
        await message.answer(
            text=text.default_message(message.text),
            reply_markup=bots_kb()
        )


class AdministrationMenu:
    async def dbconn(message: types.Message):
        await message.answer(text=text.test_dbconn())

    async def crypto(message: types.Message):
        await message.answer(
            text=text.crypto(),
            parse_mode=ParseMode.MARKDOWN
        )

    async def msg(message: types.Message, state: FSMContext):
        await bot.send_message(
            chat_id=message.from_user.id,
            text=text.send_to()
        )
        await state.set_state(groups.waiting_for_message)

    async def choice_group(message: types.Message, state: FSMContext):
        _message = message.text
        await state.update_data({"message": _message})
        await message.reply(
            text='Выберите канал куда отправить сообщение',
            reply_markup=send_to_kb()
        )

    async def back(message: types.Message):
        await message.answer(
            text=text.default_message(message.text),
            reply_markup=user_kb()
        )


async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    data = callback_query.data
    user_id = callback_query.from_user.id

    responses = {
        'test_pay': text.tons(),
        'half_pay': text.tons(),
        'one_pay': text.tons(),
        'coder_link': None,
        'support': None,
        'channel': None,
    }
    if data == 'show_wallet':
        await bot.send_photo(chat_id=user_id,
                             photo=types.FSInputFile('img/qrton.png'))
        await bot.send_message(chat_id=user_id, 
                            text=text.show_wallet(),
                            parse_mode=ParseMode.MARKDOWN
        )
    elif data in responses:
        await bot.send_message(user_id, responses[data], parse_mode=ParseMode.MARKDOWN)
    elif data in groups:
        state_data = await state.get_data()
        admin_message = state_data.get('message', '')
        await bot.send_message(chat_id=groups[data], text=admin_message)
        await bot.answer_callback_query(callback_query.id, text='Сообщение отправлено в группу!')
    else:
        await bot.answer_callback_query(callback_query.id, text='Неизвестная команда')


def register_handlers_commands(dp: Dispatcher):
    dp.message.register(ClientMenu.start, Command(commands=['start', 's']))
    dp.message.register(
        ClientMenu.administration,
        lambda message: message.text in ['⚙️ Администрирование', '/a', '/admin']
    )
    dp.message.register(
        ClientMenu.deal,
        lambda message: message.text in ['🤝 Сделка', '/d', '/deal']
    )
    dp.message.register(
        ClientMenu.bots,
        lambda message: message.text in ['🔩 Список ботов', '/l', '/listbots']
    )
    dp.message.register(
        ClientMenu.support,
        lambda message: message.text in ['💌 Связаться', '/f', '/feedback']
    )
    dp.message.register(
        AdministrationMenu.dbconn,
        lambda message: message.text == '🟨 Тест с базой'
    )
    dp.message.register(
        AdministrationMenu.back,
        lambda message: message.text == '↩️ Назад'
    )
    dp.message.register(
        AdministrationMenu.crypto,
        lambda message: message.text == 'Чек кошелька'
    )
    dp.message.register(
        AdministrationMenu.msg,
        lambda message: message.text == '📨 Отправить в канал'
    )
    dp.message.register(
        AdministrationMenu.choice_group,
        StateFilter(groups.waiting_for_message)
    )
    dp.callback_query.register(process_callback)
