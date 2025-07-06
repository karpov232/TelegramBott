from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

#creating buttons
#These buttons send messages to the chat with the bot.
choice = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='no'),  #writing the text of the buttons
                                        KeyboardButton(text='yes')] #writing the text of the buttons
                                      ]
                             resize_keyboard=True, #changing the keyboard size
                             input_field_placeholder='') #choose what will be displayed on the line when the user enters the text


catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='кепка', callback_data='cap')],
    [InlineKeyboardButton(text='шорты', callback_data='shorts')],
    [InlineKeyboardButton(text='футболка', callback_data='t-shirt')]
    ]
)
