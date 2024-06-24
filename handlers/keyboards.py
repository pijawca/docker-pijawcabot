from aiogram.types import KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Создание кнопок
admin_button = KeyboardButton(text='⚙️ Администрирование')
support_button = KeyboardButton(text='💌 Связаться')
back_button = KeyboardButton(text='↩️ Назад')
dbconn_button = KeyboardButton(text='🟨 Тест с базой')
pass1 = KeyboardButton(text='pass1')
pass2 = KeyboardButton(text='pass2')
pass3 = KeyboardButton(text='pass3')
pass4 = KeyboardButton(text='pass4')
deal_button = KeyboardButton(text='🤝 Сделка')
wallet_ton = InlineKeyboardButton(text='📩 Показать адрес TON', callback_data='show_wallet')
test_pay = InlineKeyboardButton(text='0.01 TON', callback_data='test_pay')
half_pay = InlineKeyboardButton(text='0.50 TON', callback_data='half_pay')
one_pay = InlineKeyboardButton(text='1 TON', callback_data='one_pay')


def user_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(admin_button, deal_button, support_button)
    return builder.as_markup(resize_keyboard=True)

def admin_kb():
    builder = ReplyKeyboardBuilder()
    builder.row(dbconn_button, pass1, pass2, pass4)
    builder.row(pass3, back_button)
    return builder.as_markup(resize_keyboard=True)

def deal_kb():
    builder = InlineKeyboardBuilder()
    builder.row(wallet_ton)
    builder.row(test_pay, half_pay, one_pay)
    return builder.as_markup()