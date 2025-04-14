from aiogram import F, Router
from aiogram.filters  import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from datetime import datetime

import app.keyboards as kb
from app.keyboards import create_kb_paypal

from paypal.get_token import fun_get_token
from paypal.order import fun_create_order
from paypal.payment import get_cap_url
from paypal.payment import check_payment_pp

from database.sqlite_db import add_new_user_db

import logging
from common import configure_logging

logger = logging.getLogger(__name__)

router = Router(name=__name__)

url_for_capture = ""

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!',reply_markup=kb.start)

@router.message(Command('restart'))
async def cmd_restart(message: Message):
    await message.answer('Hello!',reply_markup=kb.start)

async def get_user_data(callback: CallbackQuery):
    taken_user_data: list = [None]*5
    taken_user_data[0] = callback.from_user.id
    taken_user_data[1] = callback.from_user.first_name
    taken_user_data[2] = callback.from_user.last_name
    taken_user_data[3] = callback.from_user.username
    taken_user_data[4] = datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
    #add mobile phone?
    configure_logging()
    logger.info("User info: %s", taken_user_data)
    return [taken_user_data[0],taken_user_data[1],taken_user_data[2],taken_user_data[3],taken_user_data[4]]

#temp.test
@router.message(F.text == "My data")
async def get_user_info(message: Message):
    await message.reply(f'Hello!\nYour ID:{message.from_user.id}\nName: {message.from_user.first_name}\nLastName:{message.from_user.last_name}\nUsername:{message.from_user.username}')
    #\nMobile
    #\nDate of birth
    #\nBio
###################

#temp
@router.message(Command('help') or F.data == 'help')
async def get_help(message: Message):
    await message.answer('There is a help note.', reply_markup = kb.admin ) # info message
###################

@router.callback_query(F.data == 'unsub')
async def get_vip(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Get a VIP package', reply_markup= kb.payment_type)

@router.callback_query(F.data == 'pp_payment')
async def create_vip(callback: CallbackQuery):
    await callback.answer('')
    fun_get_token()   
    kbpayment_pp = create_kb_paypal()
    await callback.message.edit_text('PayPal', reply_markup= kbpayment_pp)# edit text
    

@router.callback_query(F.data == 'check_payment_pp')
async def check_vip(callback: CallbackQuery):
    href_ord, ord_id = fun_create_order()
    global url_for_capture 
    url_for_capture = get_cap_url(ord_id)
    await callback.answer('')
    await callback.message.edit_text(f'There is a link to your payment.\nClick this: [Click]({href_ord})\nPlease, after making it, verify your payment by clicking the button below.' , parse_mode='Markdown', reply_markup= kb.vrf_payment)

@router.callback_query(F.data == 'verif_payment')  
async def verif_pay_vip(callback: CallbackQuery): 
    global url_for_capture
    approve = check_payment_pp(url_for_capture) 
    if approve:
        #add a user to db
        user_data = await get_user_data(callback)
        add_new_user_db(user_data)#tg_id, first_name, last_name, username, date)
        await callback.message.edit_text('Welcome to VIP club', reply_markup= kb.vip)
    else:
        await callback.message.edit_text('There is no payment', reply_markup= kb.novip)


# @router.callback_query(F.data == '')
# async def ff(callback: CallbackQuery):
#     await callback.answer('')

@router.callback_query(F.data == 'back_mm')
async def back_fun(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Main menu', reply_markup= kb.start)
