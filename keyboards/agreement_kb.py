from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_agreement_keyboard() -> InlineKeyboardMarkup:
    """Клавиатура с кнопкой согласия"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="✅ Принимаю", callback_data="agree")]
    ])
    return keyboard
