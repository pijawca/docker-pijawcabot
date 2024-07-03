from aiogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from listgroups import groups


admin_button = KeyboardButton(text='⚙️ Администрирование')
support_button = KeyboardButton(text='💌 Связаться')
back_button = KeyboardButton(text='↩️ Назад')
dbconn_button = KeyboardButton(text='🟨 Тест с базой')
crypto = KeyboardButton(text='Чек кошелька')
deal_button = KeyboardButton(text='🤝 Сделка')
wallet_ton = InlineKeyboardButton(text='📩 Показать адрес TON', callback_data='show_wallet')
test_pay = InlineKeyboardButton(text='0.01 TON', callback_data='test_pay')
half_pay = InlineKeyboardButton(text='0.50 TON', callback_data='half_pay')
one_pay = InlineKeyboardButton(text='1 TON', callback_data='one_pay')
bots_button = KeyboardButton(text='🔩 Список ботов')
strojstavbot = InlineKeyboardButton(text='@strojstavbot', callback_data='strojstavbot', url='t.me/strojstavbot')
coder_link = InlineKeyboardButton(text='Разработчик', callback_data='coder', url='t.me/pijawca')
support_link = InlineKeyboardButton(text='Поддержка', callback_data='support', url='t.me/pijawca')
support_link0 = InlineKeyboardButton(text='Поддержка', callback_data='support0', url='t.me/pijawca')
channel = InlineKeyboardButton(text='Канал с новостями', callback_data='channelpijawca', url='t.me/pijawcatoday')
sendtogroups = KeyboardButton(text='📨 Отправить в канал')


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
    builder.row(strojstavbot)
    return builder.as_markup()

def feedback():
    builder = InlineKeyboardBuilder()
    builder.row(coder_link, support_link, support_link0)
    builder.row(channel)
    return builder.as_markup()

def sendTo():
    builder = InlineKeyboardBuilder()
    for i in groups:
        b = InlineKeyboardButton(text=i, callback_data=i)
        builder.row(b)
    return builder.as_markup()