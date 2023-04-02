from aiogram import Router, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.filters.text import Text
from aiogram.types import Message, CallbackQuery

from keyboards.button_recipes import create_inline_kb
from Recipe.prescription import Recipesnt
from Recipe.list_recipes import LEXICON, LEXICON_COMMANDS_RU, barbecue


router: Router = Router()
dp: Dispatcher = Dispatcher()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Блюда на мангале.")


@router.message(Command("help"))
async def cmd_start(message: Message):
    await message.answer(text=LEXICON_COMMANDS_RU['/help'])


@router.message(Command('recipes'))
async def process_more_press(message: Message):
    await message.answer(text=barbecue['/recipes'])


@router.message(Command("support"))
async def process_start_command(callback: CallbackQuery):
    keyboard = create_inline_kb(2, **LEXICON)
    await callback.answer(text='🔥Вы можете заказать такие блюда:',
                          reply_markup=keyboard)


@router.callback_query(Text(text=[key for key in LEXICON.keys()], ignore_case=True))
async def avswer_buttons(callback: CallbackQuery):
    for key, value in LEXICON.items():
        if key == callback.data:
            await callback.message.edit_text(text=Recipesnt[value])
