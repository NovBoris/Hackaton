from aiogram import Dispatcher, types
from aiogram.dispatcher.filters import Text
from keyboards import kb_admin_main, kb_admin_delete_orders, kb_login, kb_cancel, main_menu_kb
from keyboards import inline_delete_roll_kb_admin, inline_delete_burger_kb_admin, inline_delete_pizza_kb_admin
from datebase import done_homework, check_homework, login, Homework, admin
from handlers import other as oth
from aiogram.dispatcher import FSMContext
from create_bot import bot


async def cancel(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.reply("OK", reply_markup=kb_admin_main)
        return
    await state.finish()
    await message.reply('OK', reply_markup=kb_admin_main)


async def admin_check(message: types.Message):
    await oth.adminsigin.adminname.set()
    await message.reply('Введите логин учителя: ', reply_markup=kb_cancel)


async def admin_username(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['username'] = message.text
    await oth.adminsigin.next()
    await message.reply('Введите логин: ')


async def admin_userpass(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['userpass'] = message.text
        print(admin.CheckUserInfo(data['username'], data['userpass'], 'schools.db'))
        if admin.CheckUserInfo(data['username'], data['userpass'], 'schools.db') == [
            (data['username'], data['userpass'])]:

            await message.reply('Логин введен верно', reply_markup=kb_admin_main)
            await state.finish()
        else:
            await message.reply('Логин введен неверно', reply_markup=kb_login)
            await state.finish()


async def add_homework_start(message: types.Message):
    await oth.adminAddHomeWork.name.set()
    await message.reply('Введите имя ученика которому нужно отправить ДЗ: ', reply_markup=main_menu_kb)


async def add_homework_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await oth.add_good.next()
    await message.reply('Фото ДЗ: ')


async def add_homework_photo(message: types.Message,state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
    await state.finish()


async def add_homework_to_database(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        Homework.addNewHomework([data['name'], data['photo']],'schools.db')
    await state.finish()
    await message.reply('Успешно добавленно', reply_markup=kb_admin_main)


async def check_homework_start(message: types.Message):


def register_admin_message_handlers(dp: Dispatcher):
    dp.register_message_handler(admin_check, Text(equals=['Admin panel'], ignore_case=True), state=None)
    dp.register_message_handler(admin_username, state=oth.adminsigin.adminname)
    dp.register_message_handler(admin_userpass, state=oth.adminsigin.adminpass)
    dp.register_message_handler(cancel, Text(equals='Главное меню', ignore_case=True), state='*')
    dp.register_message_handler(add_homework_start, Text(equals='Добавить товар в меню', ignore_case=True), state=None)
    dp.register_message_handler(add_homework_name, state=oth.add_good.name)

