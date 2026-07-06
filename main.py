import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart , Command 
from aiogram.types import Message,ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
load_dotenv()


Token = os.getenv("API")
bot = Bot(token=Token)
dp = Dispatcher()

Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Payment")
        ]
    ],
    resize_keyboard=True
)


menyu=ReplyKeyboardMarkup(
    keyboard=[
            [KeyboardButton=(text='Katalog'),KeyboardButton(text='Sebet'),
            [KeyboardButton=(text='Baylanis')],
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Hello')



@dp.message(Command('sawda'))
async def sawda(message:Message):
    await message.answer('xush kelibsiz',reply_markup=menyu)

@dp.message(Command(commands=["payment"]))
async def payment(message: Message):
    await message.answer('Payment command received!')
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())