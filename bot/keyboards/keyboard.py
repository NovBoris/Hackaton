#коммент
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton




button_main_menu = KeyboardButton('Главное меню')
main_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu_kb.add(button_main_menu)

button_main_user_menu = KeyboardButton('Обратно')
main_user_menu_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_user_menu_kb.add(button_main_user_menu)

button_cancel = KeyboardButton('Назад')

kb_cancel = ReplyKeyboardMarkup(resize_keyboard=True)
kb_cancel.add(button_cancel)

button_login = KeyboardButton('Регистрация')
button_signin = KeyboardButton('Вход')
button_admin = KeyboardButton('Преподаватель')

kb_login = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_login.add(button_login).add(button_signin).add(button_admin)

button_diary = KeyboardButton('📜Мой дневник📜')
button_home = KeyboardButton('Моё дз')

kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_diary).row(button_home)
# ------------Кнопки которые выдаются по нажатию на Моё ДЗ
button_done_homework = KeyboardButton("Непроверенное ДЗ")
button_check_homework = KeyboardButton("Проверенное ДЗ")
# ------------Вызов кнопок по нажатию Моё ДЗ
kb_mine_dz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mine_dz.add(button_done_homework, button_check_homework).row(button_cancel)


button_admin_add_new_homework = KeyboardButton('Добавить дз')
button_admin_select_orders = KeyboardButton('Домашние задания')


kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_admin_main.row(button_admin_add_new_homework,button_admin_select_orders)


kb_admin_delete_orders = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_delete_orders.add(button_main_menu)





