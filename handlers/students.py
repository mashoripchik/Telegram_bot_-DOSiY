from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_students
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Что вас интересует?', reply_markup=kb_students)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\nhttps://t.me/DOSiYBot')

#@dp.message_handler(commands=['Информация_по_преподавателям'])
async def info_teachers_command(message : types.Message):
    await bot.send_message(message.from_user.id, '''📌Аникеенко Андрей Федорович - исполняющий обязанности заведующего кафедрой, доцент, ауд. 139-4;\n📌Гриневич Сергей Анатольевич - доцент, ауд. 21-5;\n📌Лукаш Валерий Тадеушевич - доцент, ауд. 21-5;\n📌Раповец Вячеслав Валерьевич - заместитель декана ф-та ЛИД, доцент, ауд. 211-4;\n📌Болочко Дмитрий Леонидович - ассистент, ауд. 12а-5,\n📌Алифировец Григорий Васильевич - ассистент, ауд. 12а-5;\n📌Машорипова Татьяна Александровна - ассистент, ауд. 25-5.''')

#@dp.message_handler(commands=['Расписание'])
async def info_schedule_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Расписание занятий и экзаменационной сессии:\nhttps://ttlp.belstu.by/?page_id=2548')

#@dp.message_handler(commands=['График_консультаций'])
async def info_consultation_command(message : types.Message):
    await bot.send_message(message.from_user.id, '📍График консультаций студентов очной формы обучения:\nhttps://dosy.belstu.by/?url=ochnikam\n📍График консультаций студентов заочной формы обучения:\nhttps://dosy.belstu.by/?url=zaochniki')

#@dp.message_handler(commands=['Контакты'])
async def info_contacts_command(message : types.Message):
    await bot.send_message(message.from_user.id, '📪 220006, г. Минск,  ул. Свердлова, 13а,\n☎️ 8 (017) 366-63-25,\n📩 dosy@belstu.by')

def register_handlers_students(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(info_teachers_command, commands=['Информация_по_преподавателям']) 
    dp.register_message_handler(info_schedule_command, commands=['Расписание']) 
    dp.register_message_handler(info_consultation_command, commands=['График_консультаций']) 
    dp.register_message_handler(info_contacts_command, commands=['Контакты']) 
