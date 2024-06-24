from datetime import datetime
from plugins import cryptoparse
from db.core import dbconn


def text_start(username, who_is):
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

Используйте клавиатуру либо команды:
_у команд есть короткий вызов используя только первую букву
/admin  |  /support  |  /bots  |  /payment  |  /checkwallet_
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

Владелец *pijawca* @pijawca - (По всем вопросам.)
Поддержка *pass* @pass
Поддержка *pass* @pass
    '''
    return text

def show_wallet():
    text= f'''
```UQC5ZNcP8k7G3LLNzuX2whcu2PamWdGnnn2GuXESf8uft-_P```
'''
    return text

def bots():
    pass