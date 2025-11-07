from aiogram import Router, F, Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from config import CHANNEL_ID, MAX_PHOTOS_PER_USER
from utils.states import UserStates
from utils.user_data import get_user_data, increment_photo_count, get_photo_count

router = Router()


@router.message(F.photo, UserStates.waiting_photo)
async def process_photo(message: Message, state: FSMContext, bot: Bot):
    """Обработка отправленного фото"""
    user_id = message.from_user.id
    
    # Проверяем лимит фото
    current_count = await get_photo_count(user_id)
    if current_count >= MAX_PHOTOS_PER_USER:
        await message.answer(
            f"❌ Вы достигли лимита в {MAX_PHOTOS_PER_USER} фотографий.\n"
            f"Спасибо за участие!"
        )
        return
    
    # Получаем данные пользователя
    user_data = await get_user_data(user_id)
    if not user_data or "branch" not in user_data:
        await message.answer("❌ Ошибка: филиал не выбран. Используйте /start")
        return
    
    branch = user_data["branch"]
    
    # Получаем фото в лучшем качестве
    photo = message.photo[-1]
    
    try:
        # Отправляем фото в канал
        caption = f"📍 {branch}"
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=photo.file_id,
            caption=caption
        )
        
        # Увеличиваем счетчик
        new_count = await increment_photo_count(user_id)
        remaining = MAX_PHOTOS_PER_USER - new_count
        
        await message.answer(
            f"✅ Фото успешно отправлено!\n\n"
            f"📊 Отправлено: {new_count}/{MAX_PHOTOS_PER_USER}\n"
            f"📸 Осталось: {remaining}"
        )
        
    except Exception as e:
        await message.answer(
            f"❌ Ошибка при отправке фото в канал.\n"
            f"Попробуйте еще раз или обратитесь к администратору."
        )


@router.message(F.document, UserStates.waiting_photo)
async def process_photo_as_document(message: Message, state: FSMContext, bot: Bot):
    """Обработка фото отправленного как документ"""
    # Проверяем что это изображение
    if not message.document.mime_type.startswith('image/'):
        await message.answer("❌ Пожалуйста, отправьте именно фото.")
        return
    
    user_id = message.from_user.id
    
    # Проверяем лимит фото
    current_count = await get_photo_count(user_id)
    if current_count >= MAX_PHOTOS_PER_USER:
        await message.answer(
            f"❌ Вы достигли лимита в {MAX_PHOTOS_PER_USER} фотографий.\n"
            f"Спасибо за участие!"
        )
        return
    
    # Получаем данные пользователя
    user_data = await get_user_data(user_id)
    if not user_data or "branch" not in user_data:
        await message.answer("❌ Ошибка: филиал не выбран. Используйте /start")
        return
    
    branch = user_data["branch"]
    
    try:
        # Отправляем документ в канал
        caption = f"📍 {branch}"
        await bot.send_document(
            chat_id=CHANNEL_ID,
            document=message.document.file_id,
            caption=caption
        )
        
        # Увеличиваем счетчик
        new_count = await increment_photo_count(user_id)
        remaining = MAX_PHOTOS_PER_USER - new_count
        
        await message.answer(
            f"✅ Фото успешно отправлено!\n\n"
            f"📊 Отправлено: {new_count}/{MAX_PHOTOS_PER_USER}\n"
            f"📸 Осталось: {remaining}"
        )
        
    except Exception as e:
        await message.answer(
            f"❌ Ошибка при отправке фото в канал.\n"
            f"Попробуйте еще раз или обратитесь к администратору."
        )
