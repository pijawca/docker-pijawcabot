from datetime import datetime
from plugins import cryptoparse


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
    
    text_start = f'''
    {greeting}, @{username}
    
Вы состоите в группе *{who_is.upper()}*

Используйте клавиатуру либо команды:
_у команд есть короткий вызов используя только первую букву
/admin  |  /support  |  /bots  |  /payment  |  /checkwallet_
    '''
    return text_start

# def text_dbconn():
#     text_dbconn = f'''
#     {dbconn.dbconn()}
#     '''
#     return text_dbconn
