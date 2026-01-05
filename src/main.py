import asyncio
import locale
from datetime import datetime
from aiogram.types import BotCommand, BotCommandScopeDefault
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from create_bot import bot, dp, admins
from start_router import start_router
from help_router import help_router
from settings import settings


locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                    BotCommand(command='help', description='Помощь')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot():
    await set_commands()
    for admin_id in admins:
        try:
            await bot.send_message(admin_id, f'Я запущен🥳.')
        except:
            pass


async def stop_bot():
    try:
        for admin_id in admins:
            await bot.send_message(admin_id, 'Бот остановлен. За что?😔')
    except:
        pass


async def send_daily_message():
    now = datetime.now()
    date_string = now.strftime("%d.%m.%Y")
    day_of_week = now.strftime('%A')
    text = f"<blockquote>Я заглянул в календарь...</blockquote>\n\n<blockquote>...и увидел, что сегодня {date_string} ({day_of_week}).</blockquote>"
    await bot.send_message(chat_id=settings.GROUP_ID, 
                           text=text)


async def main():
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    
    dp.include_routers(start_router, help_router)

    scheduler = AsyncIOScheduler(timezone="Asia/Novosibirsk")
    scheduler.start()
    scheduler.add_job(send_daily_message, 'cron', hour=7, minute=1)
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())


