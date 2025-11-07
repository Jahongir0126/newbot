import json
import aiofiles
import os
from typing import Optional
from config import USERS_DATA_FILE


async def load_users_data() -> dict:
    """Загрузка данных пользователей из JSON файла"""
    if not os.path.exists(USERS_DATA_FILE):
        return {}
    
    try:
        async with aiofiles.open(USERS_DATA_FILE, 'r', encoding='utf-8') as f:
            content = await f.read()
            return json.loads(content) if content else {}
    except Exception:
        return {}


async def save_users_data(data: dict) -> None:
    """Сохранение данных пользователей в JSON файл"""
    async with aiofiles.open(USERS_DATA_FILE, 'w', encoding='utf-8') as f:
        await f.write(json.dumps(data, ensure_ascii=False, indent=2))


async def get_user_data(user_id: int) -> Optional[dict]:
    """Получить данные конкретного пользователя"""
    users = await load_users_data()
    return users.get(str(user_id))


async def set_user_branch(user_id: int, branch: str) -> None:
    """Установить филиал для пользователя"""
    users = await load_users_data()
    user_id_str = str(user_id)
    
    if user_id_str not in users:
        users[user_id_str] = {
            "branch": branch,
            "photos_sent": 0,
            "agreed": True
        }
    else:
        users[user_id_str]["branch"] = branch
    
    await save_users_data(users)


async def increment_photo_count(user_id: int) -> int:
    """Увеличить счетчик отправленных фото"""
    users = await load_users_data()
    user_id_str = str(user_id)
    
    if user_id_str in users:
        users[user_id_str]["photos_sent"] = users[user_id_str].get("photos_sent", 0) + 1
        await save_users_data(users)
        return users[user_id_str]["photos_sent"]
    
    return 0


async def get_photo_count(user_id: int) -> int:
    """Получить количество отправленных фото"""
    user_data = await get_user_data(user_id)
    if user_data:
        return user_data.get("photos_sent", 0)
    return 0
