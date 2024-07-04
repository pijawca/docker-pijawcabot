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

def test_dbconn():
    text = f'''
    {dbconn()}
    '''
    return text

def default_message(location):
    text = f'''
    Вы перешли в {location}
    '''
    return text

def denied_access(location):
    text = f'''
    У вас нет доступа к {location}
    '''
    return text

def show_wallet():
    text = '''
```UQBa4RzuM8dr4qBcHSoudfIE9mf5p6jrOs6BK48-pRNgo-fC```
    '''
    return text

def crypto():
    status = cryptoparse.ton_status()
    payed = 6300
    ton = 9.27
    math = float(status[2]) * 9.272
    total = int(math - payed)
    if total > 0:
        msg = f'🙂 {total}'
    elif total < 0:
        msg = f'😔 {total}'
    
    text = f'''
*TON*

*$ {status[0]}  |  ₽ {status[2]}*
vol {status[5]}
1h {status[3]}  |  24h {status[1]}  |  7d {status[4]}

*TOTAL {payed}  |  {ton}*
{msg}
'''
    return text 

def send_to():
    text = f'''
Что написать в канал?
'''
    return text

def tons():
    text = f'''
К сожалению в данный момент не работает. Заявка на рассмотрении у TON Wallet
'''
    return text
