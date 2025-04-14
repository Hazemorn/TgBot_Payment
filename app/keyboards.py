from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


start = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='I have subscription', callback_data='sub')],#check in db
    [InlineKeyboardButton(text="I haven't subscription", callback_data='unsub')]
])

payment_type = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='PayPal payment', callback_data='pp_payment')],
    [InlineKeyboardButton(text='Back to the main menu', callback_data='back_mm')]
])

def create_kb_paypal():
    payment = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Pay', callback_data='check_payment_pp')]  #url= href_ord
    ])
    return payment

vrf_payment = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Verify', callback_data='verif_payment')] 
    ])
   
vip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Welcome to VIP', url='https://www.youtube.com')]#temp
])

novip = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Try again.Back to the main menu', callback_data='back_mm')],
    [InlineKeyboardButton(text='Help',callback_data ='help')]
])

ping_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Connect admin', url= "https://t.me/verif_1_bot")] # temp: admin tg
])



#another version 
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Payment')],
    [KeyboardButton(text='Stop Bot')]
],
    resize_keyboard=True,
    input_field_placeholder='Select menu item',
    one_time_keyboard=True
)
