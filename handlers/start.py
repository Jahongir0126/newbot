from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import AGREEMENT_TEXT
from keyboards.agreement_kb import get_agreement_keyboard
from utils.states import UserStates

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """Обработчик команды /start"""
    await state.set_state(UserStates.waiting_agreement)
    
    await message.answer(
        f"👋 Добро пожаловать, {message.from_user.first_name}!\n\n{AGREEMENT_TEXT}",
        reply_markup=get_agreement_keyboard()
    )
