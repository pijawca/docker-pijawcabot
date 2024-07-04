from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from listgroups import groups

admin_button = KeyboardButton(text='⚙️ Администрирование')
support_button = KeyboardButton(text='💌 Связаться')
back_button = KeyboardButton(text='↩️ Назад')
dbconn_button = KeyboardButton(text='🟨 Тест с базой')
crypto = KeyboardButton(text='Чек кошелька')
deal_button = KeyboardButton(text='🤝 Сделка')
sendtogroups = KeyboardButton(text='📨 Отправить в канал')
bots_button = KeyboardButton(text='🔩 Список ботов')
passbot = InlineKeyboardButton(text='в разработке', url='t.me/pijawca')
coder_link = InlineKeyboardButton(text='Разработчик', url='t.me/pijawca')
support_link = InlineKeyboardButton(text='Поддержка', url='t.me/pijawca')
channel = InlineKeyboardButton(text='Канал с новостями', url='t.me/pijawcatoday')
wallet_ton = InlineKeyboardButton(text='📩 Показать адрес TON', callback_data='show_wallet')
test_pay = InlineKeyboardButton(text='0.01 TON', callback_data='test_pay')
half_pay = InlineKeyboardButton(text='0.50 TON', callback_data='half_pay')
one_pay = InlineKeyboardButton(text='1 TON', callback_data='one_pay')

def user_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(admin_button, deal_button, bots_button)
    builder.row(support_button)
    return builder.as_markup(resize_keyboard=True)

def admin_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(dbconn_button, crypto, sendtogroups)
    builder.row(back_button)
    return builder.as_markup(resize_keyboard=True)

def deal_kb():
    builder = InlineKeyboardBuilder()
    builder.row(wallet_ton)
    builder.row(test_pay, half_pay, one_pay)
    return builder.as_markup()

def bots_kb():
    builder = InlineKeyboardBuilder()
    builder.row(passbot)
    return builder.as_markup()

def feedback_kb():
    builder = InlineKeyboardBuilder()
    builder.row(coder_link, support_link)
    builder.row(channel)
    return builder.as_markup()

def send_to_kb():
    builder = InlineKeyboardBuilder()
    for group in groups:
        button = InlineKeyboardButton(text=group, callback_data=group)
        builder.row(button)
    return builder.as_markup()
