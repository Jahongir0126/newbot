from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.branches_kb import get_branches_keyboard
from utils.states import UserStates

router = Router()


@router.callback_query(F.data == "agree", UserStates.waiting_agreement)
async def process_agreement(callback: CallbackQuery, state: FSMContext):
    """Обработка согласия пользователя"""
    await callback.answer()
    await state.set_state(UserStates.waiting_branch)
    
    await callback.message.edit_text(
        "✅ Спасибо за согласие!\n\n"
        "📍 Теперь выберите ваш филиал:",
        reply_markup=get_branches_keyboard()
    )
