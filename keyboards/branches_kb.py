from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BRANCHES


def get_branches_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с выбором филиалов"""
    buttons = []
    
    for i, branch in enumerate(BRANCHES):
        buttons.append([InlineKeyboardButton(
            text=branch,
            callback_data=f"branch_{i}"
        )])
    
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
