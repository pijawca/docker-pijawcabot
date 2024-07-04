from datetime import datetime
from plugins import cryptoparse
from db.core import dbconn


def start(username, who_is):
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= current_hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"
    
    text = f'''
    {greeting}, @{username}
    
Вы состоите в группе как *{who_is}*

_Используйте клавиатуру, либо команды в меню бота_
    '''
    return text

def text_dbconn():
    text = f'''
    {dbconn()}
    '''
    return text

def text_open_button(location):
    text= f'''
    Вы перешли в {location}
    '''
    return text

def denied_access(location):
    text= f'''
    У вас нет доступа к {location}
    '''
    return text

def passed():
    text= f'''
    pass
    '''
    return text

def support():
    text= f'''
*Прямые ссылки*

Администратор *pijawca* @pijawca - (По всем вопросам.)
Поддержка *pass* @pass
Поддержка *pass* @pass

Канал @pijawcatoday
    '''
    return text

def show_wallet():
    text= f'''
```UQC5ZNcP8k7G3LLNzuX2whcu2PamWdGnnn2GuXESf8uft-_P```
'''
    return text

def crypto():
    payed = 6300
    ton = 9.27
    math = float(cryptoparse.ton_status()[2]) * 9.272
    total = int(math - payed)
    if total > 0:
        msg = f'🙂 {total}'
    elif total < 0:
        msg = f'😔 {total}'
    
    text= f'''
*TON*

*$ {cryptoparse.ton_status()[0]}  |  ₽ {cryptoparse.ton_status()[2]}*
vol {cryptoparse.ton_status()[5]}
1h {cryptoparse.ton_status()[3]}  |  24h {cryptoparse.ton_status()[1]}  |  7d {cryptoparse.ton_status()[4]}

*TOTAL {payed}  |  {ton}*
{msg}
'''
    return text 

def sendTo():
    text= f'''
Что написать в канал?
'''
    return text

def tons():
    text= f'''
К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet
'''
    return text