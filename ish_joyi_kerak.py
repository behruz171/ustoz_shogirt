import re

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from dotenv import load_dotenv
import os
load_dotenv()

storage = MemoryStorage()

pattern = re.compile(r'^\+998[0-9]{9}')
pattern1 = re.compile(r'^[0-9]')

class Partner(StatesGroup):
    full_name = State()
    age = State()
    technology = State()
    phone = State()
    location = State()
    price = State()
    job = State()
    oclock = State()
    desire = State()


bot = Bot("6911317564:AAHKcCGfo0uBHKpexeSl_RJ8imbxUb32Vlk")
dp = Dispatcher(bot, storage=storage)
async def on_startup(_):
    print("Bot ishga tushdi")


def start_buttons() -> ReplyKeyboardMarkup:
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="Sherik kerak")
    button2 = KeyboardButton(text="Ish joyi kerak")
    button3 = KeyboardButton(text="Hodim kerak")
    button4 = KeyboardButton(text="Ustoz kerak")
    button5 = KeyboardButton(text="Shogirt kerak")
    buttons.add(button1, button2)
    buttons.add(button3, button4)
    buttons.add(button5)

    return buttons


@dp.message_handler(commands=['start'])
async def start_button(message: types.Message):
    first_name = message.from_user.first_name
    text = f"Assalom alaykum {first_name} \nUstozShogirt kanalining rasmiy botiga xush kelibsiz!\n/help yordam buyrugi orqali nimalarge qodir ekanligimni bilib oling!"
    await message.answer(text=text, reply_markup=start_buttons())


@dp.message_handler(Text(equals="Ish joyi kerak"), state="*")
async def btn2(message: types.Message):
    text= "Ish joyi topish uchun ariza berish \n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering. \nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.\n\nIsm, familiyangizni kiriting?"
    await message.answer(text=text)
    await Partner.full_name.set()


@dp.message_handler(state=Partner.full_name)
async def set_full_name(message: types.Message, state: FSMContext):
    text = "🕑 Yosh: \n\nYoshingizni kiriting?\nMasalan, 19"

    await state.update_data(full_name=message.text)

    await message.answer(text=text)

    await Partner.next() 

@dp.message_handler(state=Partner.age)
async def set_age(message: types.Message, state: FSMContext):
    text = "📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting? \nTexnologiya nomlarini vergul bilan ajrating. Masalan,\n\nJava, C++, C#"

    await state.update_data(age=message.text)

    await message.answer(text=text)

    await Partner.next()       


@dp.message_handler(state=Partner.technology)
async def set_technology(message: types.Message, state: FSMContext):
    text = "📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67"

    await state.update_data(technology=message.text)

    await message.answer(text=text)

    await Partner.next()  


@dp.message_handler(state=Partner.phone)
async def set_phone(message: types.Message, state: FSMContext):
    if pattern.match(message.text):
        text = "Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting."

        await state.update_data(phone=message.text)

        await message.answer(text=text)

        await Partner.next()
    else:
        await message.answer("Togri telefon raqam kirgizing")


@dp.message_handler(state=Partner.location)
async def set_location(message: types.Message, state: FSMContext):
    text = "💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?"

    await state.update_data(location=message.text)

    await message.answer(text=text)

    await Partner.next()         

@dp.message_handler(state=Partner.price)
async def set_price(message: types.Message, state: FSMContext):
    text = "👨🏻‍💻 Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba"

    await state.update_data(price=message.text)

    await message.answer(text=text)

    await Partner.next()  

@dp.message_handler(state=Partner.price)
async def set_price(message: types.Message, state: FSMContext):
    text = "👨🏻‍💻 Kasbi: \n\nIshlaysizmi yoki o`qiysizmi?\nMasalan, Talaba"

    await state.update_data(price=message.text)

    await message.answer(text=text)

    await Partner.next()      

@dp.message_handler(state=Partner.job)
async def set_job(message: types.Message, state: FSMContext):
    text = "🕰 Murojaat qilish vaqti: \n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00"

    await state.update_data(job=message.text)

    await message.answer(text=text)

    await Partner.next() 


@dp.message_handler(state=Partner.oclock)
async def set_oclock(message: types.Message, state: FSMContext):
    text = "🔎 Maqsad: \n\nMaqsadingizni qisqacha yozib bering."
    await state.update_data(oclock=message.text)

    await message.answer(text=text)

    await Partner.next()          


@dp.message_handler(state=Partner.desire)
async def set_desire(message: types.Message, state: FSMContext):
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton(text="HA")
    button2 = KeyboardButton(text="YOQ")
    buttons.add(button1,button2)
    await state.update_data(desire=message.text)

    data = await state.get_data()

    text = f"Ish joyi: {data['full_name']}\nTexnologiya: {data['technology']}\nTelegram: {message.from_user.username}\nAloqa: {data['phone']}\nHudud: {data['location']}\nNarxi: {data['price']}\nKasbi: {data['job']}\nMurojat qilish vaqti: {data['oclock']}\nMaqsad: {data['desire']}\n\nBarcha malumotlar to'g'rimi"

    await message.answer(text=text, reply_markup=buttons)

    await Partner.next()

@dp.message_handler(Text(equals="HA"))
async def set_application(message: types.Message, state: FSMContext):
    data = await state.get_data()
    text = f"Ish joyi: {data['full_name']}\nTexnologiya: {data['technology']}\nTelegram: @{message.from_user.username}\nAloqa: {data['phone']}\nHudud: {data['location']}\nNarxi: {data['price']}\nKasbi: {data['job']}\nMurojat qilish vaqti: {data['oclock']}\nMaqsad: {data['desire']}\n\nBarcha malumotlar to'g'rimi"
    print(message.from_user.id)
    await bot.send_message(chat_id="6550264522", text=text)
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)    