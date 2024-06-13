import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from plugins import cryptoparse


def text_start(username):
    current_hour = datetime.now().hour
    
    if 5 <= current_hour < 12:
        greeting = 'Доброе утро'
    elif 12 <= current_hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_hour < 23:
        greeting = "Добрый вечер"
    else:
        greeting =  "Доброй ночи"

    ton_status = cryptoparse.ton_status()
    text_start = f'''
{greeting}, @{username}\n
```
TON  ${ton_status[0]} |  ₽{ton_status[2]}
1h:     {ton_status[3]}%
24h:    {ton_status[1]}%
7d:     {ton_status[4]}%
Vol:    ${ton_status[5]}
```

```
USDT
PASS
```

```
SOMETHING
```
'''
    return text_start