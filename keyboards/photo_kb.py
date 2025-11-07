from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_photo_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура для отправки фото"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📸 Отправить фото")]
        ],
        resize_keyboard=True,
        one_time_keyboard=False
    )
    return keyboard
