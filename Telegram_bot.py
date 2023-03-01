from aiogram.utils import executor
from create_bot import dp





async def on_startup(_):
    print('Бот вышел в онлайн')

from handlers import students, admin, other

students.register_handlers_students(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
