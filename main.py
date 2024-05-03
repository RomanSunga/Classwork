import asyncio

from aiogram import Bot, Dispatcher, Router, F

from aiogram.filters import Command 
from aiogram.fsm.context import FSMContext




bot = Bot(token="7158364646:AAF5SJorIUaCPBU7t3v7sShKVl_KmsPF3hM")
dp = Dispatcher()






@router.message(Command("anketa"))
async def anketa_handler(msg: Message, state: FSMContext):
    await state.set_state(Anketa. name)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa')]])
    await msg.answer('Введите ваше имя', reply_markup=markup)
    

@router.callback_query(F.data == 'cancel_anketa')
async def next_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer('Регистрация отменена')


@router.message(Anketa.name)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(name=msg.text)
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите ваш возраст', reply_markup=markup)

@router.callback_query(F.data == 'set_name_anketa')
async def set_name_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    await anketa_handler(callback_query.message, state)

@router.message(Anketa.age)
async def set_name_by_anketa_handler(msg: Message, state: FSMContext):
    try:
        await state.update_data(age=int(msg.text))
    except ValueError:
        await msg.answer('Вы не верно ввели возраст!')
        markup = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text='Назад', callback_data='set_name_anketa'),
            InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])    
        await msg.answer('Введите ваш возраст', reply_markup=markup)
        return

    await state.set_state(Anketa.gender)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data='set_age_anketa'), 
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await msg.answer('Введите Ваш пол', reply_markup=markup)

@router.callback_query(F.data == 'set_age_anketa')
async def set_age_anketa_handler(callback_query: CallbackQuery, state: FSMContext):
    await state.set_state(Anketa.age)
    markup = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text='Назад', callback_data= 'set_name_anketa'),
        InlineKeyboardButton(text='Отмена', callback_data='cancel_anketa'),]])
    await callback_query.message.answer('Введите Ваш возраст', reply_markup=markup)


@router.message(Anketa.gender)
async def set_age_by_anketa_handler(msg: Message, state: FSMContext):
    await state.update_data(gender=msg.text)
    await msg.answer(str(await state.get_data()))
    await state.clear()




async def main():
    await dp.start_polling(bot)




dp.include_routers(router)

if __name__ == '__main__':
    asyncio.run(main())