from aiogram.dispatcher.filters.state import State, StatesGroup

class login(StatesGroup):
    username = State()
    userpass = State()

class sigin(StatesGroup):
    username = State()
    userpass = State()

class adminsigin(StatesGroup):
    adminname = State()
    adminpass = State()

class adminAddHomeWork(StatesGroup):
    name = State()
    photo = State()