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

button_menu = KeyboardButton('📜Мой дневник📜')
button_orders = KeyboardButton('Моё дз')


kb_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_main.add(button_orders).row(button_menu)


button_orders_burgers = KeyboardButton('🍔Мои Бургеры🍔')


kb_orders = ReplyKeyboardMarkup(resize_keyboard=True)
kb_orders.row(button_orders_burgers).add(button_cancel)


button_admin_add_new_good = KeyboardButton('Добавить дз')
button_admin_select_orders = KeyboardButton('Домашние задания')


kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
kb_admin_main.row(button_admin_add_new_good,button_admin_select_orders)


kb_admin_delete_orders = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_delete_orders.add(button_main_menu)





