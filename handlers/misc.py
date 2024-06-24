import logging
from config import TOKEN
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


logging.basicConfig(format=u'%(levelname)-8s [ LINE:%(lineno)-4s] %(filename)+13s [%(asctime)s] %(message)s', level=logging.DEBUG)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())
