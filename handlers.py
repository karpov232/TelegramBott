from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command

import app.keyboards as kb


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет. Ты попал в ЛУЧШЕГО бота для заработка на банках')
    await message.answer('1/3 выбери откуда узнал о нас', reply_markup=kb.ppp)


@router.message(F.text == 'от друга')
async def ppp(message: Message):
    await message.answer('2/3 выберите банк который у вас есть', reply_markup=kb.bank)


@router.message(F.text == 'из ютуба')
async def ppp(message: Message):
    await message.answer('2/3 выберите банк который у вас есть', reply_markup=kb.bank)


@router.message(F.text == 'другое')
async def ppp(message: Message):
    await message.answer('2/3 выберите банк который у вас есть', reply_markup=kb.bank)


@router.message(Command('help'))
async def commands(message: Message):
    await message.answer('')


@router.message(F.text == 'больше 18')
async def age(message: Message):
    await message.answer('Отлично. Вы можите заработать 800 рублей')
    await message.answer('Условия: ')
    await message.answer('1. оформить карту по ссылке: https://www.tbank.ru/baf/1yQTWOHJ7bi')
    await message.answer('2. сделать покупку на 500 рублей')
    await message.answer('3. получить 500 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('4. получить 300 рублей от нашей компании')


@router.message(F.text == 'меньше 18')
async def age(message: Message):
    await message.answer('Отлично. Вы можите заработать 600 рублей')
    await message.answer('Условия: ')
    await message.answer('1. оформить карту т банка по ссылке: https://www.tbank.ru/baf/1yQTWOHJ7bi')
    await message.answer('2. сделать покупку на 500 рублей')
    await message.answer('3. получить 500 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('4. получить 100 рублей от нашей компании')
    await message.answer('5. если вы всё сделали, вы можете заработать по 100 рублей за каждого приведённого друга. '
                         'Если хотите отправьте 9')


@router.message(F.text == 'альфа банк')
async def alfa_bank(message: Message):
    await message.answer('3/3 сколько вам лет', reply_markup=kb.age)


@router.message(F.text == 'т банк')
async def t_bank(message: Message):
    await message.answer('Отлично. Вы можите заработать 400 рублей')
    await message.answer('Условия: ')
    await message.answer('1. оформить карту альфа банка по ссылке: https://alfa.me/gwXKMu')
    await message.answer('2. сделать 5 покупок на любую сумму')
    await message.answer('3. получить 300 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('4. получить 100 рублей от нашей компании')
    await message.answer('5. если вы сделали всё нажмите на кнопку есть всё')


@router.message(F.text == 'сбербанк')
async def sber_bank(message: Message):
    await message.answer('Отлично. Вы можите заработать 1100 рублей')
    await message.answer('Условия: ')
    await message.answer('1. оформить карту альфа банка по ссылке: https://alfa.me/gwXKMu')
    await message.answer('2. сделать 5 покупок на любую сумму')
    await message.answer('3. получить 300 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('4. получить 100 рублей от нашей компании')
    await message.answer('5. оформить карту т банка по ссылке: https://www.tbank.ru/baf/1yQTWOHJ7bi')
    await message.answer('6. сделать покупку на 500 рублей')
    await message.answer('7. получить 500 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('8. получить 300 рублей от нашей компании')
    await message.answer('9. если вы сделали всё нажмите на кнопку есть всё')


@router.message(F.text == 'нет ничего')
async def no_bank(message: Message):
    await message.answer('Отлично. Вы можите заработать 1100 рублей')
    await message.answer('Условия: ')
    await message.answer('1. оформить карту альфа банка по ссылке: https://alfa.me/gwXKMu')
    await message.answer('2. сделать 5 покупок на любую сумму')
    await message.answer('3. получить 300 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('4. получить 100 рублей от нашей компании')
    await message.answer('5. оформить карту т банка по ссылке: https://www.tbank.ru/baf/1yQTWOHJ7bi')
    await message.answer('6. сделать покупку на 500 рублей')
    await message.answer('7. получить 500 рублей от банка и скинуть скриншоты и номер телефона сюда: bankmoune@mail.ru')
    await message.answer('8. получить 300 рублей от нашей компании')
    await message.answer('9. если вы сделали всё нажмите на кнопку есть всё')


@router.message(F.text == 'есть все')
async def vse(message: Message):
    await message.answer('Вы можете заработать по 100 рублей за каждого приведённого друга. Если хотите отправьте 9')


@router.message(F.text == '9')
async def refirals(message: Message):
    await message.answer('что бы получить 100 рублей вы должны ')
    await message.answer('1. скинуть ссылку на бота другу')
    await message.answer('2. прислать почту и номер друга на почту: bankmoune@mail.ru')
    await message.answer('3. подпишись на наш тг канал там ещё больше подобных темок: https://t.me/+cCC2U3wajnBjNTUy')
