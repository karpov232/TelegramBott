from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


bank = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='альфа банк'),
                                     KeyboardButton(text='т банк')],
                                     [KeyboardButton(text='сбербанк'),
                                      KeyboardButton(text='есть все')],
                                     [KeyboardButton(text='нет ничего')]],
                           resize_keyboard=True,
                           input_field_placeholder='выберите банк...')


ppp = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='от друга'),
                                     KeyboardButton(text='из ютуба')],
                                    [KeyboardButton(text='другое')]],
                          resize_keyboard=True,
                          input_field_placeholder='выберите откуда узнал о нас...')


age = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='больше 18'),
                                     KeyboardButton(text='меньше 18')]],
                          resize_keyboard=True)
