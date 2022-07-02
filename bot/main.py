from create_bot import dp
from aiogram import executor
import logging
from handlers import client,rolls,admin,done_home

logging.basicConfig(level=logging.INFO)

client.register_message_handlers(dp)
rolls.register_message_handlers_rolls(dp)
done_home.register_message_handlers_student(dp) # Раньше называлась бургеры
admin.register_admin_message_handlers(dp)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)
