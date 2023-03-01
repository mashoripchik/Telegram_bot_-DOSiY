from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Информация_по_преподавателям')
b2 = KeyboardButton('/Расписание')
b3 = KeyboardButton('/График_консультаций')
b4 = KeyboardButton('/Контакты')
#b5 = KeyboardButton('/Поделиться номером телефона', request_contact=True)


kb_students = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_students.add(b1).row(b2, b3, b4)#.row(b5)