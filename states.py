from aiogram.fsm.state import StatesGroup, State

class profile(StatesGroup):
    set_photo = State()
    set_name = State()
    set_gender = State()
    set_age = State()

class Reg(StatesGroup):
    your_photo = State()
    your_name = State()
    your_gender = State()
    your_age = State()

class get_prompt(StatesGroup):
    text_prompt = State()
