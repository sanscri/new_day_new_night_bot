from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from settings import settings

help_router = Router()


def help_kb():
    kb_list = [
      [InlineKeyboardButton(text="Группа", url=settings.GROUP_LINK)]

    ]
    return InlineKeyboardMarkup(
        inline_keyboard=kb_list
    )


@help_router.message(Command("help"))
async def cmd_help(message: Message):
  
    help = f"Бот каждый день смотрит в каллендарь и говрит, какой сегодня день."
    await message.answer(help,
                              reply_markup=help_kb())