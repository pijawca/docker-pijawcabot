#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio  
from handlers.misc import dp, bot
from handlers import general


general.register_handlers_commands(dp)


async def start():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
    