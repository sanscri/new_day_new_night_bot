from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from settings import settings

start_router = Router()

def start_kb():
    kb_list = [
      [InlineKeyboardButton(text="Группа", url=settings.GROUP_LINK)]

    ]
    return InlineKeyboardMarkup(
        inline_keyboard=kb_list
    )

@start_router.message(CommandStart())
async def cmd_start(message: Message):
  greeting = "Бот каждый день смотрит в календарь и говрит, какой сегодня день."
  await message.answer(greeting, reply_markup=start_kb())
   