from aiogram.types  import KeyboardButton,InlineKeyboardButton,ReplyKeyboardMarkup,InlineKeyboardMarkup


def reply_menu():
    btn1=KeyboardButton(text="1-tugma",request_location=True)
    btn2=KeyboardButton(text="2-tugma",request_contact=True)

    design=[[btn1,btn2]]

    return ReplyKeyboardMarkup(keyboard=design,one_time_keyboard=True,resize_keyboard=True)


def inline_menu():
    btn1=InlineKeyboardButton(text="1-tugma",callback_data="1")
    btn2=InlineKeyboardButton(text="2-tugma",callback_data="2")

    design=[[btn1,btn2]]

    return InlineKeyboardMarkup(inline_keyboard=design)
