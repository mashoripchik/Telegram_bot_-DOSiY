from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp
from aiogram.dispatcher.filters import Text

class FSMAdmin(StatesGroup):
	photo = State()
	name = State()
	info = State()
	office = State()

#Хэндлер для начала диалога загрузки нового пункта меню
@dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message : types.Message):
	await FSMAdmin.photo.set()
	await message.reply('Загрузи фото')

#Ловим первый ответ от админа и пишем в словарь
#@dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['photo'] = message.photo[0].file_id
	await FSMAdmin.next()
	await message.reply("Теперь введи ФИО")

#Ловим второй ответ
#@dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['name'] = message.text
	await FSMAdmin.next()
	await message.reply("Введи описание профиля")

#Ловим третий ответ
#@dp.message_handler(state=FSMAdmin.info)
async def load_info(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['info'] = message.text
	await FSMAdmin.next()
	await message.reply("Теперь укажи кабинет")

# Ловим последний ответ и используем полученные данные
#@dp.message_handler(state=FSMAdmin.office)
async def load_office(message: types.Message, state: FSMContext):
	async with state.proxy() as data:
		data['office'] = message.text

	async with state.proxy() as data:
		await message.reply(str(data))
	await state.finish()

#Выход из машинного состояния
@dp.message_handler(state="*", commands='отмена')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state="*")
async def cancel_handler(message: types.Message, state: FSMContext):
	current_state = await state.get_state()
	if current_state is None:
		return
	await state.finish()
	await message.reply('ОК')


# Регистрируем хендлеры
def register_handlers_admin(dp : Dispatcher):
	dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
	dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
	dp.register_message_handler(load_name, state=FSMAdmin.name)
	dp.register_message_handler(load_info, state=FSMAdmin.info)
	dp.register_message_handler(load_office, state=FSMAdmin.office)
	dp.register_message_handler(cancel_handler, state="*", commands='отмена')
	dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state="*")

