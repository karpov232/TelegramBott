#You must create this file in the app folder, which will be in the project folder.
from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
#imports keyboards from app as kb
import app.keyboards as kb

#creating router
router = Router()

#if command == start ...
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('this is your text')
    await message.answer('hello, your peaple?', reply_markup=kb.choice)#programm does this code

#if text == yes...
@router.message(F.text == 'yes')
async def yes(message: Message):
    await message.answer('text', reply_markup=kb.choice)#programm does this code

#if text == no
@router.message(F.text == 'no')
async def no(message: Message):
    await message.answer('text')#programm does this code

#if command == help ...
@router.message(Command('help'))
async def commands(message: Message):
    await message.answer('text')#programm does this code

#if callback == to the second argument from the program app.keyboards...
@router.callback_query(F.data == 'what the program sends')
async def cap(callback: CallbackQuery):
    await callback.message.answer('выберии лучшую кепку')#programm does this code
