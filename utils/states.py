from aiogram.fsm.state import State, StatesGroup


class UserStates(StatesGroup):
    waiting_agreement = State()
    waiting_branch = State()
    waiting_photo = State()
