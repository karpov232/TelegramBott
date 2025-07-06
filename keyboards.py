from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

#creating buttons
#These buttons send messages to the chat with the bot.
choice = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='no'),  #writing the text of the buttons
                                        KeyboardButton(text='yes')] #writing the text of the buttons
                                      ]
                             resize_keyboard=True, #changing the keyboard size
                             input_field_placeholder='') #choose what will be displayed on the line when the user enters the text

#The difference between these buttons is that they do not send messages to a chat with a bot.
catalog = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='what the user sees', callback_data='what the program sends')],
    [InlineKeyboardButton(text='shorts', callback_data='shorts')],
    [InlineKeyboardButton(text='123', callback_data='t-shirt')]
    ]
)
