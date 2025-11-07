from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from config import BRANCHES
from keyboards.photo_kb import get_photo_keyboard
from utils.states import UserStates
from utils.user_data import set_user_branch

router = Router()


@router.callback_query(F.data.startswith("branch_"), UserStates.waiting_branch)
async def process_branch_selection(callback: CallbackQuery, state: FSMContext):
    """Обработка выбора филиала"""
    branch_index = int(callback.data.split("_")[1])
    branch_name = BRANCHES[branch_index]
    
    # Сохраняем филиал пользователя
    await set_user_branch(callback.from_user.id, branch_name)
    await state.update_data(branch=branch_name)
    await state.set_state(UserStates.waiting_photo)
    
    await callback.answer()
    await callback.message.edit_text(
        f"✅ Вы выбрали: {branch_name}\n\n"
        f"📸 Теперь вы можете отправлять фото (до 10 штук).\n"
        f"Отправьте фото из галереи или как файл."
    )
    
    await callback.message.answer(
        "Готовы отправить фото? 👇",
        reply_markup=get_photo_keyboard()
    )
