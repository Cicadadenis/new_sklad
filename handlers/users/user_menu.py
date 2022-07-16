# - *- coding: utf- 8 - *-
from keyboards.default.main_settings import get_settings_func
from typing import Text
import ftplib
from aiogram.types import ReplyKeyboardMarkup
from threading import Timer
from threading import *
import shutil
import re
from threading import Timer
from threading import *
from aiogram import types
from my_fake_useragent import UserAgent
import general as gen
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, message
import requests
from keyboards.inline.user_func import confirm_buy_items
from keyboards.inline.user_func import open_item_func
from keyboards.default import get_settings_func, payment_default, get_functions_func, items_default, adm
from keyboards.default import check_user_out_func, all_back_to_main_default
from keyboards.inline.cicada import soglasie, soglasie2
from keyboards.inline.inline_page import *
from loader import dp, bot
from states import state_url
from smsactivateru import Sms, SmsTypes, SmsService, GetBalance, GetFreeSlots, GetNumber, SetStatus, GetStatus

from data.config import config
from states.state_users import *
from utils.other_func import  get_dates
from states.state_url import cicada
import datetime
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types.user import User
from Users.Users import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
import random
import config
from data.config import bot_description
import time
import os
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard
import json
from keyboards.default.menu import reg_back, virtualsim, virtualsimadm, sit, pon, dano, pravila, otm
import pyshorteners
from data.config import sms_api
from threading import Timer
from threading import *
import os
from aiogram.types import CallbackQuery, Message
import re 
import time
import ftplib
import secrets
import configparser
import re
from Users.Users import Admin
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from handlers.users.main_start import sozdatel
from handlers.users.cicada_menu import cicada
from keyboards.inline.cicada import gen_pass, uss
from keyboards.inline.user_profiles import get_user_profile
from keyboards.inline.user_inline import open_profile_inl
import ftplib
import re
import requests
from threading import Timer
from threading import *
from datetime import datetime, date
import requests, os
from io import BytesIO
import aiohttp
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


class PhotoStorage:
    def __init__(self, path: str):
        self.path = path
        self.data = self.load()
    
    def load(self):
        if exists(self.path):
            with open(self.path) as file:
                return file.readlines()


async def upload_document(
    bot, doc: types.photo_size.PhotoSize or types.Document
) -> str:
    with await doc.download(BytesIO()) as file:

        form = aiohttp.FormData()
        form.add_field(
            name="file",
            value=file,
        )

        async with bot.session.post("https://telegra.ph/upload", data=form) as response:
            img_src = await response.json()

    return "http://telegra.ph/" + img_src[0]["src"]


wrapper = Sms('d4c14d3e44e06932975eB8d839B56152')
user_starii = []
user_new = []
old_baza = []
new_baza = []
sait = []
dopusk = []

temp = []

def balans():
    bal = GetBalance().request(wrapper)
    return bal


mesmes = []

class cicada(StatesGroup):
    size = State()
    vg = State()
    vg2 = State()
    pz = State()
    pz2 = State()
    pzl = State()
    pzl2 = State()
    kdrtop = State()
    kdrtop2 = State()
    kdrtopl = State()
    kdrtopl2 = State()
    amzntop = State()
    amzntop2 = State()
    arizonel = State()
    arizonel2 = State()
    arizone = State()
    arizone2 = State()
    chizhtop = State()
    chizhtop2 = State()
    abawork = State()
    abawork2 = State()
    murmur48 = State()
    lokwork = State()
    lokwork2 = State()
    amzntopl2 = State()
    amzntopl = State()
    lokshop = State()
    lokshop2 = State()
    chizhtopl = State()
    chizhtopl2 = State()
    up_y = State()
    up_x = State()
    red = State()
    passw = State()
    capha = State()
    cicada_url = State()
    ip_up = State()
    probiv = State()
    site = State()
    site_new = State()
    old_user = State()
    new_user = State()
    par = State()
    dat = State()
    gad = State()



s = pyshorteners.Shortener()
# Разбив сообщения на несколько, чтобы не прилетало ограничение от ТГ
def split_messages(get_list, count):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Обработка кнопки "Купить"
@dp.message_handler(text="🔐 Акаунты", state="*")
async def show_search(message: types.Message, state: FSMContext):
    await message.delete()
    await state.finish()
    get_categories = get_all_categoriesx()
    if len(get_categories) >= 1:
        get_kb = buy_item_open_category_ap(0)
        
        await message.answer("<b>🔐 Выберите нужный вам Акаунт:</b>", reply_markup=get_kb)
    else:
        await message.answer("<b>🔐 Акаунты в данное время отсутствуют.</b>")



@dp.message_handler(text='🌐 Сайты', state="*")
async def siteee(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    chat_id = message.chat.id
    print(dopusk)
    if chat_id in dopusk:
        fo = open("img.png", "rb").read()
        messm = "<b>✳️✳️  Управление  -  Сайтами  ✳️✳️</b>"
        await bot.send_photo(chat_id, photo=fo, caption=messm, reply_markup=sit)
    else:
        await message.answer(f"<b>Сюда Ограничен Доступ</b>\n", parse_mode="html")
        await message.answer(f"<b>Для Входа Введи Пароль:</b>", parse_mode="html")
        await cicada.par.set()

ggg = []
@dp.message_handler(state=cicada.par)
async def par(message: types.Message, state: FSMContext):
    chat_id = message.chat.id
    xxx = message.text
    await message.delete()
    await state.finish()
  
    if xxx == "web":
        if chat_id not in dopusk:
            dopusk.append(chat_id)
        fo = open("img.png", "rb").read()
        messm = "<b>✳️✳️  Управление  -  Сайтами  ✳️✳️</b>"
        await bot.send_photo(chat_id, photo=fo, caption=messm, reply_markup=sit)
    else:
        await bot.send_message(chat_id, "<b>❌ НЕВЕРНЫЙ ПАРОЛЬ ❌</b>") 
        

@dp.callback_query_handler(text='kdrtop', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'murmur48.cc'
    ftp_user = 'cicada@kdrtop.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"krdtop.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"krdtop.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.kdrtop.set()

tem = []
@dp.callback_query_handler(state=cicada.kdrtop)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
        await cicada.kdrtop2.set()


@dp.message_handler(state=cicada.kdrtop2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"krdtop.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("krdtop.html", "r", encoding="utf-8").readlines()
        open("new-krdtop.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-krdtop.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-krdtop.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)



@dp.callback_query_handler(text='amzntop', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'amzntop.ru'
    ftp_user = 'amazon@amzntop.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"amzntop.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"amzntop.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.amzntop.set()

tem = []
@dp.callback_query_handler(state=cicada.amzntop)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.amzntop2.set()

@dp.message_handler(state=cicada.amzntop2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"amzntop.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("amzntop.html", "r", encoding="utf-8").readlines()
        open("new-amzntop.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-amzntop.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-amzntop.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)





@dp.callback_query_handler(text='amzntopl', state="*")
async def best(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'amzntopl.ru'
    ftp_user = 'amzl@amzntopl.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    ncncc = ftp.nlst()
    print(ncncc)
    input()
    local_file = f"amzntopl.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"amzntopl.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    m
    asasa = []
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                  
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    print(name)
                    h = g.split('" rel="')[0]
                    print(h)
                    
                    if len(h) <= 30:
                        if h in asasa:
                            pass
                        else:
                            asasa.append(h)
                            satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                  
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.amzntopl.set()


tem = []
@dp.callback_query_handler(state=cicada.amzntopl)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.amzntopl2.set()

@dp.message_handler(state=cicada.amzntopl2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"amzntopl.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("amzntopl.html", "r", encoding="utf-8").readlines()
        open("new-amzntopl.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-amzntopl.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-amzntopl.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.callback_query_handler(text='lokshop', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'ruvip54.hostiman.ru'
    ftp_user = 'shop'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"lokshop.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"lokshop.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_message(call.message.chat.id, mj, reply_markup=satana)
    await cicada.lokshop.set()


tem = []
@dp.callback_query_handler(state=cicada.lokshop)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.lokshop2.set()

@dp.message_handler(state=cicada.lokshop2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"lokshop.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("lokshop.html", "r", encoding="utf-8").readlines()
        open("new-lokshop.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-lokshop.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-lokshop.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)

@dp.callback_query_handler(text='lokwork', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'lok-work.cc'
    ftp_user = 'lok-work.cc@lok-work.cc'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"lokwork.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"lokwork.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.lokwork.set()


tem = []
@dp.callback_query_handler(state=cicada.lokwork)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.lokwork2.set()

@dp.message_handler(state=cicada.lokwork2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"lokwork.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("lokwork.html", "r", encoding="utf-8").readlines()
        open("new-lokwork.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-lokwork.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-lokwork.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.callback_query_handler(text='murmur48', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'murmur48.cc'
    ftp_user = 'murmur48@murmur48.cc'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"{call.message.chat.id}.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"{call.message.chat.id}.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)

    for x in gg:

        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await call.message.answer(mj, reply_markup=satana)
    await cicada.murmur48.set()


@dp.callback_query_handler(text='abawork', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'murmur48.cc'
    ftp_user = 'aba@abawork.cc'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"abawork.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"abawork.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.abawork.set()

tem = []
@dp.callback_query_handler(state=cicada.abawork)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.abawork2.set()

@dp.message_handler(state=cicada.abawork2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"abawork.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("abawork.html", "r", encoding="utf-8").readlines()
        open("new-abawork.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-abawork.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-abawork.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)





@dp.callback_query_handler(text='chizhtopl', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'chizhtopl.ru'
    ftp_user = 'cacady@chizhtopl.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"chizhtopl.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"chizhtopl.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.chizhtopl.set()





tem = []
@dp.callback_query_handler(state=cicada.chizhtopl)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.chizhtopl2.set()

@dp.message_handler(state=cicada.chizhtopl2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"chizhtopl.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("chizhtopl.html", "r", encoding="utf-8").readlines()
        open("new-chizhtopl.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-chizhtopl.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-chizhtopl.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)

@dp.callback_query_handler(text='chizhtop', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'omwork.cc'
    ftp_user = 'cicada@chizhtop.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"chizhtop.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"chizhtop.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.chizhtop.set()


tem = []
@dp.callback_query_handler(state=cicada.chizhtop)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.chizhtop2.set()

@dp.message_handler(state=cicada.chizhtop2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"chizhtop.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("chizhtop.html", "r", encoding="utf-8").readlines()
        open(f"new-chizhtop.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-chizhtop.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-chizhtop.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.callback_query_handler(text='arizone', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'arizone.ru'
    ftp_user = 'cicada@arizone.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"arizone.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"arizone.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.arizone.set()

tem = []
@dp.callback_query_handler(state=cicada.arizone)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.arizone2.set()

@dp.message_handler(state=cicada.arizone2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"arizone.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("arizone.html", "r", encoding="utf-8").readlines()
        open(f"new-arizone.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-arizone.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-arizone.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)



@dp.callback_query_handler(text='arizonel', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'arizonel.ru'
    ftp_user = '777@arizonel.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"arizonel.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"arizonel.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.arizonel.set()


tem = []
@dp.callback_query_handler(state=cicada.arizonel)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.arizonel2.set()

@dp.message_handler(state=cicada.arizonel2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"arizonel.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("arizonel.html", "r", encoding="utf-8").readlines()
        open(f"new-arizonel.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-arizonel.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-arizonel.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)

@dp.callback_query_handler(text='kdrtopl', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'kdrtopl.ru'
    ftp_user = 'zzz@kdrtopl.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"kdrtopl.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"kdrtopl.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.kdrtopl.set()



tem = []
@dp.callback_query_handler(state=cicada.kdrtopl)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.kdrtopl2.set()

@dp.message_handler(state=cicada.kdrtopl2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"kdrtopl.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("kdrtopl.html", "r", encoding="utf-8").readlines()
        open(f"new-kdrtopl.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-kdrtopl.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-kdrtopl.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)

@dp.callback_query_handler(text='pz', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'omwork.cc'
    ftp_user = 'pzh@pzhtop.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"pz.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"pz.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.pz.set()



tem = []
@dp.callback_query_handler(state=cicada.pz)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.pz2.set()

@dp.message_handler(state=cicada.pz2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"pz.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("pz.html", "r", encoding="utf-8").readlines()
        open(f"new-pz.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-pz.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-pz.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.callback_query_handler(text='vg', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'vegaswork.cc'
    ftp_user = 'cicada@vegaswork.cc'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"vg.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"vg.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=1)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))
    mj = " \n".join(baza)
    await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)
    await cicada.vg.set()
 
tem = []
@dp.callback_query_handler(state=cicada.vg)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.vg2.set()

@dp.message_handler(state=cicada.vg2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"vg.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("vg.html", "r", encoding="utf-8").readlines()
        open(f"new-vg.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-vg.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-vg.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.callback_query_handler(text='pzl', state="*")
async def ban_add(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("<b>Идет Загрузка Сайта Ожидай .....</b>")
    host = 'omwork.cc'
    ftp_user = 'zzz@pzhtopl.ru'
    ftp_password = 'Tramadol1989'
    sait.append(host)
    sait.append(ftp_user)
    sait.append(ftp_password)
    await state.finish()
    ftp = ftplib.FTP(host, ftp_user, ftp_password)
    local_file = f"pzl.html"
    ftp_file  = "index.html"
    with open(local_file, 'wb') as local_file: 
        ftp.retrbinary('retr ' + ftp_file, local_file.write)
    ftp.close()
    baza = []
    saiit = ftp_user.split("@")[-1]
    titl = f"✳️ <b>Управление Сайтом http://{saiit}</b>"
    baza.append(titl)
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
    gg = open(f"pzl.html", "r", encoding="utf-8").readlines()
    satana = InlineKeyboardMarkup(row_width=3)
    fotoo = []
    for x in gg:
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if 'http://telegra.ph//file/' in x:
            if x.split("url(")[-1] in x:
                if x.split(');"></div>\n')[0] in x:
                    x = x.split("url(")[-1]
                    x = x.split(');"></div>\n')[0]
                    fotoo.append(x)
        if '<div class=' in x:
            if 'href=' in x:
                if 'target="_blank"' in x:
                    nam = x.split('target="_blank">')[-1]
                    name = nam.split('</a></div>')[0]
                    g = x.split('href="')[-1]
                    h = g.split('" rel="')[0]
                    if len(h) <= 30:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}|{h}"))
                        sfsf = f"👤 <b>{name}:</b>   <code>{h}</code>   💥"
                        baza.append(sfsf)
                        baza.append("➖➖➖➖➖➖➖➖➖➖➖➖➖")
                    else:
                        satana.add(InlineKeyboardButton(text=f"Изменить {name}", callback_data=f"{name}"))
    satana.add(InlineKeyboardButton(text='◀️ Назад', callback_data='tttt'))

    mj = " \n".join(baza)
    fff = await bot.send_photo(chat_id=call.message.chat.id, photo=fotoo[0], caption=mj, reply_markup=satana)


    mesmes.append(fff)
    await cicada.pzl.set()

 
tem = []
@dp.callback_query_handler(state=cicada.pzl)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.pzl2.set()

@dp.message_handler(state=cicada.pzl2)
async def nene(message: types.Message, state: FSMContext):
    x = message.text
    print(x)
    kto = message.chat.username
    admin = 1144785510


    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"pzl.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        
        gg = open("pzl.html", "r", encoding="utf-8").readlines()
        open(f"new-pzl.html", "w")
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-pzl.html", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")

        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-pzl.html", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)



# @dp.message_handler(state=cicada.old_user)
# async def old(m: types.Message, state: FSMContext):
#     x = m.text
#     x = x.split("https://t.me/")[-1]
#     sts = open("index.html", "r", encoding="utf-8").read()
#     md = re.search(pattern=x, string=sts)
#     await bot.delete_message(chat_id=m.from_user.id, message_id=m.message_id)
#     while True:
#         if md  is None:
#             await m.answer("<b>‼️‼️‼️ Такого Username Нет На Сайте ‼️‼️‼️\n\n🔄 Попробуй Снова:  </b>", parse_mode="html", reply_markup=all_back_to_main_default)
#             break
#         if "@" in x:
#             x = x.split("@")[-1]
#             old_baza.append(x)
#             await m.answer(
#                 f"<b>Теперь Введи Username</b>\n"
#                 f"<b>Который Нужно Установить</b>")
#             await cicada.new_user.set()
#             break
#         if "http://t.me/" in x:
#             x = x.split("http://t.me/")[-1]
#             old_baza.append(x)
#             await m.answer(
#                 f"<b>Теперь Введи Username</b>\n"
#                 f"<b>Который Нужно Установить</b>")
#             await cicada.new_user.set()
#             break
#         if "https://t.me/" in x:
#             x = x.split("https://t.me/")[-1]
#             old_baza.append(x)
#             await m.answer(
#                 f"<b>Теперь Введи Username</b>\n"
#                 f"<b>Который Нужно Установить</b>")
#             await cicada.new_user.set()
#             break
#         else:
#             old_baza.append(x)
#             await m.answer(
#                 f"<b>Теперь Введи Username</b>\n"
#                 f"<b>Который Нужно Установить</b>")
#             await cicada.new_user.set()
#             break


# @dp.message_handler(state=cicada.new_user)
# async def old(m: types.Message, state: FSMContext):
#     y = m.text
  
#     if "@" in y:
#         y = y.split("@")[-1]
#         new_baza.append(y)
#     if "http://t.me/" in y:
#         y = y.split("http://t.me/")[-1]
#         new_baza.append(y)
#     if "https://t.me/" in y:
#         y = y.split("https://t.me/")[-1]
#         new_baza.append(y)
#     else:
#         new_baza.append(y)
#     # try:
#     for x in new_baza:
#         y = x
#     for c in old_baza:
#         pattern = c
#     host = sait[0]
#     ftp_user = sait[1]
#     ftp_password = sait[2]
#     ftp = ftplib.FTP(host, ftp_user, ftp_password)
#     sait.clear()
#     try:
#         string = open("index.html", "r", encoding="utf-8").read()

#         dd = re.sub(pattern, y, string)
#         with open("index.html", "w", encoding="utf-8") as f:
#             f.write(str(dd))
#         await state.finish()

#         await m.answer(f"<b>Мы Меняем</b>  <i>{old_baza[0]}</i><b>  На </b><i>{new_baza[0]}</i>\n"
#                     f"<b>Идет Процесс Изменения Ожидай.....</b>")
#         old_baza.clear()
#         new_baza.clear()
#         time.sleep(2)
#         file = "index.html"
#         file_to_upload = open('index.html', 'rb')
#         ftp.storbinary('STOR ' + file, file_to_upload)
#         ftp.close()
#         await m.answer("<b>Контакт Успешно Изменен  !!!</b>", reply_markup=all_back_to_main_default)

#     except:
#         await m.answer("<b>Неверно Указан Username</b>", reply_markup=all_back_to_main_default)
#         old_baza.clear()
#         new_baza.clear()


              

tem = []
@dp.callback_query_handler(state=cicada.gad)
async def poc_callback_but(c:CallbackQuery, state: FSMContext):
    ydal = c.data
    if ydal == "tttt":
        await c.message.delete()
        await state.finish()
        await c.message.answer(f"<b>❌ Отмена ❌</b>",  reply_markup=sit)
    else:
        await c.message.delete()
        tem.append(ydal)
        tr  = ReplyKeyboardMarkup(resize_keyboard=True)
        tr.row("❌ Отмена")
        await c.message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                f"<b>Введи Username \nКоторый Нужно Установить</b>\n"
                                f"➖➖➖➖➖➖➖➖➖➖➖➖➖", reply_markup=tr)
    await cicada.dat.set()


@dp.message_handler(state=cicada.dat)
async def nene(message: types.Message, state: FSMContext):
    x = message.text

    kto = message.chat.username
    admin = 1144785510
    await message.delete()

    if x == "❌ Отмена":

        await state.finish()
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        await message.answer("Отменено",  reply_markup=check_user_out_func(message.from_user.id)) 
    else:
        x = x.split("https://t.me/")[-1]
        x = x.split("http://t.me/")[-1]
        y = tem[0]
        naiti = y.split('|')[0]
        y = y.split("https://t.me/")[-1]
        y = y.split("http://t.me/")[-1]
        tem.clear()
        host = sait[0]
        ftp_user = sait[1]
        ftp_password = sait[2]
        local_file = f"{message.chat.id}.html"
        await state.finish()
        
        mmg = f"Пользователь {kto}\nВ {date.today()}\nПоменял Контакты:\nC {y}  На {x}\nНа Сервере {ftp_user}"
        await bot.send_message(admin, mmg)
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Меняем 👤 </b><code>{y}</code>\n"
                             f"<b>На </b> 👤 <code>{x}</code>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n")
        open(f"new-{local_file}", "w")
        gg = open(local_file, "r", encoding="utf-8").readlines()
        for string in gg:
            if naiti in string:
                string = re.sub(pattern=y, repl=x, string=string)
            with open(f"new-{local_file}", "a", encoding="utf-8") as f:
                f.write(f"{string}\n")
        old_baza.clear()
        new_baza.clear()
        sait.clear()
        time.sleep(2)

        ftp = ftplib.FTP(host, ftp_user, ftp_password)
        file = "index.html"
        file_to_upload = open(f"new-{local_file}", 'rb')
        ftp.storbinary('STOR ' + file, file_to_upload)
        ftp.close()
        await message.answer(f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"<b>Контакт Успешно Изменен  !!!</b>\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n", reply_markup=all_back_to_main_default)


@dp.message_handler(text='📶 Номера')
async def sim(message: types.Message):
    chat_id = message.chat.id
    if chat_id == 1144785510:
        await message.answer('®️ Регистрация Тelegram и Signal', reply_markup=virtualsimadm)
    else:
        await message.answer('®️ Регистрация Тelegram и Signal', reply_markup=virtualsim)
    
# Обработка кнопки "Профиль"
@dp.message_handler(text="📱 Профиль", state="*")
async def show_profile(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    await message.answer(get_user_profile(message.from_user.id), reply_markup=open_profile_inl)




@dp.callback_query_handler  (text="bak", state="*")
async def bak(call: CallbackQuery, state: FSMContext):
    await message.answer('Вы вернулись в Главное Меню !!!',  reply_markup=get_functions_func(call.message.from_user.id))
###################################
##################################
@dp.callback_query_handler  (text="uurl", state="*")
async def reg_url(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Введите ссылку в таком формате http://google.com/')
    await cicada.cicada_url.set()

@dp.message_handler(state=cicada.cicada_url)
async def ssylka(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['cicada.cicada_url'] = str(f"{message.text}")
    await cicada.cicada_url.set()
    uurl = data['cicada.cicada_url']
    try:
        r = (requests.get(f'https://is.gd/create.php?format=simple&url={uurl}/'))
    except:
        r = (requests.get(f'https://is.gd/create.php?format=simple&url={uurl}/'))


        
    await message.answer('Шифруем вашу ссылку ожидайте ....')
    r2 = (requests.get(f"https://uni.su/api/?url={uurl}/"))
    r3 = (requests.get(f"https://clck.ru/--?url={uurl}/"))
    r4 = (requests.get(f"https://v.gd/create.php?format=simple&url={uurl}/"))
    s = pyshorteners.Shortener()
    pr = (s.chilpit.short(uurl))
    pr8 = (s.osdb.short(uurl))
    pr9 = (s.dagd.short(message.text))
    s = pyshorteners.Shortener()
    #pr1 = (s.qpsru.short(message.text))
    time.sleep(4)
    await message.answer(
        f"🔗 Готово! Вот ваши ссылки:\n\n"
    f"Ссылка №1️⃣: {r.text} \nСсылка №2️⃣: {r2.text} \nСсылка №3️⃣: {r3.text} \nСсылка №4️⃣: {r4.text} \nСсылка №5️⃣: {pr} \nСсылка №6️⃣: {pr9} \n<b>TOP-ССЫЛКА: {pr8}</b>", parse_mode='HTML',disable_web_page_preview = True)
    


@dp.callback_query_handler  (text="BBB", state="*")
async def BBB(call: CallbackQuery, state: FSMContext):
    await call.message.answer(balans())



@dp.callback_query_handler  (text="gen_pass", state="*")
async def gen_pass(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    password0 = secrets.token_hex(4)
    password1 = secrets.token_hex(6)
    password2 = secrets.token_hex(8)
    password3 = secrets.token_hex(10)
    password4 = secrets.token_hex(12)
    paroli = (
        f"<b>Пароли успешно сгенерировано:</b>\n\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"{password0}\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"{password1}\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"{password2}\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"{password3}\n"
        f"➖➖➖➖➖➖➖➖\n"
        f"{password4}")
    await bot.send_message(chat_id, text=paroli)



@dp.callback_query_handler  (text="vega")
async def vega(call: CallbackQuery):
    await call.message.answer("<b>Cначало указуем username Который сейчас на сайте\nПосле Указываем На Какой Нужно Заменить</b>", reply_markup=pon)


@dp.callback_query_handler  (text="ponyal_vega", state="*")
async def ponyal_vega(call: CallbackQuery, state: FSMContext):
    await call.message.answer("<b>Введи Username Который Будем Изменять</b>")
    await cicada.site.set()



@dp.message_handler(state=cicada.site)
async def site(message: types.Message, state: FSMContext):
    star = message.text
    user_starii.append(star)
    await message.answer("<b>А Теперь Username Который Теперь Будет На Сайте</b>")
    await cicada.site_new.set()

@dp.message_handler(state=cicada.site_new)
async def site_new(message: types.Message, state: FSMContext):
    star_new = message.text
    user_new.append(star_new)
    await message.answer(f"<b>Мы Меняем</b> <i>{user_starii[0]}</i> <b>на</b> <i>{user_new[0]}</i> <b>\n\nВсе Верно ?</b>", reply_markup=dano)


@dp.callback_query_handler  (text="da_vega")
async def da_vega(call: CallbackQuery):
    sawe()
    await call.message.answer("OK")

@dp.callback_query_handler  (text="proton")
async def send_danet(call: CallbackQuery):

    def telega():
        available_phones = GetFreeSlots(country=SmsTypes.Country.UK).request(wrapper)
        
        tele = ('Доступно: {} номеров'.format(available_phones.Telegram.count))
        return tele

        
    msg_teleg = f"""
        ➖➖➖➖➖➖➖➖➖➖➖➖➖
        💡<b>Регистрация Telegram</b>💡

        ✅  <b>{telega()}</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
    <b> Получить номер для Telegram ?</b>
        """
    await call.message.answer(msg_teleg, reply_markup=soglasie)


@dp.callback_query_handler  (text="sig")
async def sssig(call: CallbackQuery):
    def kol():
        available_phones = GetFreeSlots(country=SmsTypes.Country.NL).request(wrapper)
        
        sigg = ('Доступно: {} номеров'.format(available_phones.AnyOther.count))
        return sigg
    msg_sig = f"""
        ➖➖➖➖➖➖➖➖➖➖➖➖➖
            💡<b>Регистрация Signal</b>💡

        ✅  <b>{kol()}</b>
➖➖➖➖➖➖➖➖➖➖➖➖➖
        <b> Получить номер для Signal ?</b>
        """
    await call.message.answer(msg_sig, reply_markup=soglasie2)


@dp.callback_query_handler(text="nene")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    await call.message.answer("Регистрация Telegram Отменена", reply_markup=check_user_out_func(call.message.from_user.id)) 

@dp.callback_query_handler(text="nene2")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    await call.message.answer("Регистрация Signal Отменена", reply_markup=check_user_out_func(call.message.from_user.id)) 



@dp.callback_query_handler(text="dow")
async def send_dom_value(call: types.CallbackQuery):
        chat_id = call.message.chat.id
        await call.message.answer('Отправь мне фото', reply_markup=download_photo())



@dp.callback_query_handler(text="dada2")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    chat_id = call.message.chat.id
    if balans() < 40:
        await call.message.answer('Сервер перегружен попробуйте позже')
    else:
        async def threading():
            t2=Thread(target=await poexali)
            t2.start()
        async def poexali():
            available_phones = GetFreeSlots(country=SmsTypes.Country.NL).request(wrapper)
            activation = GetNumber(service=SmsService().AnyOther,country=SmsTypes.Country.NL).request(wrapper)          
            nomer = ('Есть 3 минуты для регистрации. \nНомер на Signal: \n🇳🇱  {}'.format(str(activation.phone_number)))
            await call.message.answer(nomer)
            response = GetStatus(id=activation.id).request(wrapper)
            number = (activation.phone_number)
            set_as_sent = SetStatus(id=activation.id, status=SmsTypes.Status.SmsSent).request(wrapper)
            timeout = 180
            counter = 0
            while True:
                time.sleep(1)
                counter += 1
                if counter >= timeout:
                    await call.message.answer(f'Время вышло, номер {number} больше не актуален')
                    set_as_cancel = SetStatus(id=activation.id, status=SmsTypes.Status.Cancel).request(wrapper)
                    break
                response = GetStatus(id=activation.id).request(wrapper)
                if response['code']:
                    code_sms = (response['code'])
                    await call.message.answer(f'Код для номера {number}:\n {code_sms}')
                    break
        await threading()

@dp.callback_query_handler(text="dada")
async def send_danet(call: CallbackQuery):
    await call.message.delete() 
    chat_id = call.message.chat.id
    if balans() < 40:
        await call.message.answer('Сервер перегружен попробуйте позже')
    else:
        async def threading():
            t2=Thread(target= await poexali)
            t2.start()

        async def poexali():
            available_phones = GetFreeSlots(country=SmsTypes.Country.UK).request(wrapper)
            activation = GetNumber(service=SmsService().AnyOther,country=SmsTypes.Country.UK).request(wrapper)          
            nomer = ('Есть 3 минуты для регистрации. \nНомер на Telegram: \n🇬🇧  {}'.format(str(activation.phone_number)))
            await call.message.answer(nomer)
            response = GetStatus(id=activation.id).request(wrapper)
            number = (activation.phone_number)
            set_as_sent = SetStatus(id=activation.id, status=SmsTypes.Status.SmsSent).request(wrapper)
            timeout = 180
            counter = 0
            while True:
                time.sleep(1)
                counter += 1
                if counter >= timeout:
                    await call.message.answer(f'Время вышло, номер {number} больше не актуален')
                    set_as_cancel = SetStatus(id=activation.id, status=SmsTypes.Status.Cancel).request(wrapper)
                    break
                response = GetStatus(id=activation.id).request(wrapper)
                if response['code']:
                    code_sms = (response['code'])
                    await call.message.answer(f'Код для номера {number}:\n {code_sms}')
                    break
        await threading()

@dp.callback_query_handler  (text="gen_proxy", state="*")
async def genene(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
    await call.answer("❗В плижайшее время допишу")
#######################
@dp.callback_query_handler  (text="gen_nick", state="*")
async def gen_name(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    line = random.choice(open('names.txt').readlines())
    line2 = random.choice(open('names.txt').readlines())
    line3 = random.choice(open('names.txt').readlines())
    line4 = random.choice(open('names.txt').readlines())
    line5 = random.choice(open('names.txt').readlines())
    await bot.send_message(chat_id=chat_id,  text=f'''
✅ <b>Ники</b> успешно сгенерирован:

{line}
{line2}
{line3}
{line4}
{line5}''')

###########################
@dp.callback_query_handler  (text="gen_agent", state="*")
async def gen_ag(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await bot.send_message(chat_id=call.message.chat.id, text=f'Привет!Выбери устройстра 📱💻🖥 ', reply_markup=uss)

"""
@dp.callback_query_handler  (text="uss_android", state="*")
async def gen_ag(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    """



@dp.callback_query_handler  (text="uss_windows", state="*")
async def link(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'windows')
    res = ua.random()
    ua = UserAgent(os_family = 'windows')
    res1 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res2 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res3 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res4 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res5 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res6 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res7 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res8 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res9 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res10 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res11 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res12 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res13 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res14 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res15 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res16 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res17 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res18 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res19 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res20 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res21 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res22 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res23 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res24 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res25 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res26 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res27 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res28 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res29 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res30 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res31 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res32 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res33 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res34 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res35 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res36 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res37 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res38 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res39 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res40 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res41 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res42 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res43 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res44 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res45 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res46 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res47 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res48 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res49 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res50 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res51 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res52 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res54 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res55 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res56 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res57 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res58 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res59 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res60 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res61 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res62 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res63 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res64 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res65 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res66 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res67 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res68 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res69 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res70 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res71 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res72 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res73 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res74 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res75 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res76 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res77 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res78 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res79 = ua.random()
    ua = UserAgent(os_family = 'windows')
    res80 = ua.random()
    ff.write(f'''
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent Windows\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)

@dp.callback_query_handler  (text="uss_linux", state="*")
async def link(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'linux')
    res = ua.random()
    ua = UserAgent(os_family = 'linux')
    res1 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res2 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res3 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res4 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res5 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res6 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res7 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res8 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res9 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res10 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res11 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res12 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res13 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res14 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res15 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res16 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res17 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res18 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res19 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res20 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res21 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res22 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res23 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res24 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res25 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res26 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res27 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res28 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res29 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res30 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res31 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res32 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res33 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res34 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res35 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res36 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res37 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res38 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res39 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res40 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res41 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res42 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res43 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res44 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res45 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res46 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res47 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res48 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res49 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res50 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res51 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res52 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res54 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res55 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res56 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res57 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res58 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res59 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res60 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res61 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res62 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res63 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res64 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res65 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res66 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res67 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res68 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res69 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res70 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res71 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res72 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res73 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res74 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res75 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res76 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res77 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res78 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res79 = ua.random()
    ua = UserAgent(os_family = 'linux')
    res80 = ua.random()
    ff.write(f'''
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent Linux\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)



@dp.callback_query_handler  (text="uss_ios", state="*")
async def gen_ios(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'ios')
    res = ua.random()
    ua = UserAgent(os_family = 'ios')
    res1 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res2 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res3 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res4 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res5 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res6 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res7 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res8 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res9 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res10 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res11 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res12 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res13 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res14 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res15 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res16 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res17 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res18 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res19 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res20 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res21 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res22 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res23 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res24 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res25 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res26 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res27 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res28 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res29 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res30 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res31 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res32 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res33 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res34 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res35 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res36 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res37 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res38 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res39 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res40 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res41 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res42 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res43 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res44 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res45 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res46 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res47 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res48 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res49 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res50 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res51 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res52 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res54 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res55 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res56 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res57 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res58 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res59 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res60 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res61 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res62 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res63 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res64 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res65 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res66 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res67 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res68 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res69 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res70 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res71 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res72 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res73 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res74 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res75 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res76 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res77 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res78 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res79 = ua.random()
    ua = UserAgent(os_family = 'ios')
    res80 = ua.random()
    ff.write(f'''
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')

    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent IOS\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)


@dp.callback_query_handler  (text="uss_android", state="*")
async def gen_andr(call: CallbackQuery, state: FSMContext):
    chat_id = call.message.chat.id
    await call.message.delete()
    ff = open('useragent.txt', 'w')
    ua = UserAgent(os_family = 'android')
    res = ua.random()
    ua = UserAgent(os_family = 'android')
    res1 = ua.random()
    ua = UserAgent(os_family = 'android')
    res2 = ua.random()
    ua = UserAgent(os_family = 'android')
    res3 = ua.random()
    ua = UserAgent(os_family = 'android')
    res4 = ua.random()
    ua = UserAgent(os_family = 'android')
    res5 = ua.random()
    ua = UserAgent(os_family = 'android')
    res6 = ua.random()
    ua = UserAgent(os_family = 'android')
    res7 = ua.random()
    ua = UserAgent(os_family = 'android')
    res8 = ua.random()
    ua = UserAgent(os_family = 'android')
    res9 = ua.random()
    ua = UserAgent(os_family = 'android')
    res10 = ua.random()
    ua = UserAgent(os_family = 'android')
    res11 = ua.random()
    ua = UserAgent(os_family = 'android')
    res12 = ua.random()
    ua = UserAgent(os_family = 'android')
    res13 = ua.random()
    ua = UserAgent(os_family = 'android')
    res14 = ua.random()
    ua = UserAgent(os_family = 'android')
    res15 = ua.random()
    ua = UserAgent(os_family = 'android')
    res16 = ua.random()
    ua = UserAgent(os_family = 'android')
    res17 = ua.random()
    ua = UserAgent(os_family = 'android')
    res18 = ua.random()
    ua = UserAgent(os_family = 'android')
    res19 = ua.random()
    ua = UserAgent(os_family = 'android')
    res20 = ua.random()
    ua = UserAgent(os_family = 'android')
    res21 = ua.random()
    ua = UserAgent(os_family = 'android')
    res22 = ua.random()
    ua = UserAgent(os_family = 'android')
    res23 = ua.random()
    ua = UserAgent(os_family = 'android')
    res24 = ua.random()
    ua = UserAgent(os_family = 'android')
    res25 = ua.random()
    ua = UserAgent(os_family = 'android')
    res26 = ua.random()
    ua = UserAgent(os_family = 'android')
    res27 = ua.random()
    ua = UserAgent(os_family = 'android')
    res28 = ua.random()
    ua = UserAgent(os_family = 'android')
    res29 = ua.random()
    ua = UserAgent(os_family = 'android')
    res30 = ua.random()
    ua = UserAgent(os_family = 'android')
    res31 = ua.random()
    ua = UserAgent(os_family = 'android')
    res32 = ua.random()
    ua = UserAgent(os_family = 'android')
    res33 = ua.random()
    ua = UserAgent(os_family = 'android')
    res34 = ua.random()
    ua = UserAgent(os_family = 'android')
    res35 = ua.random()
    ua = UserAgent(os_family = 'android')
    res36 = ua.random()
    ua = UserAgent(os_family = 'android')
    res37 = ua.random()
    ua = UserAgent(os_family = 'android')
    res38 = ua.random()
    ua = UserAgent(os_family = 'android')
    res39 = ua.random()
    ua = UserAgent(os_family = 'android')
    res40 = ua.random()
    ua = UserAgent(os_family = 'android')
    res41 = ua.random()
    ua = UserAgent(os_family = 'android')
    res42 = ua.random()
    ua = UserAgent(os_family = 'android')
    res43 = ua.random()
    ua = UserAgent(os_family = 'android')
    res44 = ua.random()
    ua = UserAgent(os_family = 'android')
    res45 = ua.random()
    ua = UserAgent(os_family = 'android')
    res46 = ua.random()
    ua = UserAgent(os_family = 'android')
    res47 = ua.random()
    ua = UserAgent(os_family = 'android')
    res48 = ua.random()
    ua = UserAgent(os_family = 'android')
    res49 = ua.random()
    ua = UserAgent(os_family = 'android')
    res50 = ua.random()
    ua = UserAgent(os_family = 'android')
    res51 = ua.random()
    ua = UserAgent(os_family = 'android')
    res52 = ua.random()
    ua = UserAgent(os_family = 'android')
    res54 = ua.random()
    ua = UserAgent(os_family = 'android')
    res55 = ua.random()
    ua = UserAgent(os_family = 'android')
    res56 = ua.random()
    ua = UserAgent(os_family = 'android')
    res57 = ua.random()
    ua = UserAgent(os_family = 'android')
    res58 = ua.random()
    ua = UserAgent(os_family = 'android')
    res59 = ua.random()
    ua = UserAgent(os_family = 'android')
    res60 = ua.random()
    ua = UserAgent(os_family = 'android')
    res61 = ua.random()
    ua = UserAgent(os_family = 'android')
    res62 = ua.random()
    ua = UserAgent(os_family = 'android')
    res63 = ua.random()
    ua = UserAgent(os_family = 'android')
    res64 = ua.random()
    ua = UserAgent(os_family = 'android')
    res65 = ua.random()
    ua = UserAgent(os_family = 'android')
    res66 = ua.random()
    ua = UserAgent(os_family = 'android')
    res67 = ua.random()
    ua = UserAgent(os_family = 'android')
    res68 = ua.random()
    ua = UserAgent(os_family = 'android')
    res69 = ua.random()
    ua = UserAgent(os_family = 'android')
    res70 = ua.random()
    ua = UserAgent(os_family = 'android')
    res71 = ua.random()
    ua = UserAgent(os_family = 'android')
    res72 = ua.random()
    ua = UserAgent(os_family = 'android')
    res73 = ua.random()
    ua = UserAgent(os_family = 'android')
    res74 = ua.random()
    ua = UserAgent(os_family = 'android')
    res75 = ua.random()
    ua = UserAgent(os_family = 'android')
    res76 = ua.random()
    ua = UserAgent(os_family = 'android')
    res77 = ua.random()
    ua = UserAgent(os_family = 'android')
    res78 = ua.random()
    ua = UserAgent(os_family = 'android')
    res79 = ua.random()
    ua = UserAgent(os_family = 'android')
    res80 = ua.random()
    ff.write(f'''
{res} 
{res1} 
{res2} 
{res3} 
{res4} 
{res5} 
{res6} 
{res7} 
{res8} 
{res9} 
{res10} 
{res11} 
{res12} 
{res13} 
{res14} 
{res15} 
{res16} 
{res17} 
{res18} 
{res19} 
{res20} 
{res21} 
{res22} 
{res23} 
{res24} 
{res25} 
{res26} 
{res27} 
{res28} 
{res29} 
{res30} 
{res31} 
{res32} 
{res33} 
{res34} 
{res35} 
{res36} 
{res37} 
{res38} 
{res39} 
{res40} 
{res41} 
{res42} 
{res43} 
{res44} 
{res45} 
{res46} 
{res47} 
{res48} 
{res49} 
{res50} 
{res51} 
{res52} 
{res55} 
{res54} 
{res55} 
{res56} 
{res57} 
{res58} 
{res59} 
{res60} 
{res61} 
{res62} 
{res63} 
{res64} 
{res65} 
{res66} 
{res67} 
{res68} 
{res69} 
{res70} 
{res71} 
{res72} 
{res73} 
{res74} 
{res75} 
{res76} 
{res77} 
{res78} 
{res79} 
{res80} ''')
    ff.close()
    f = open("useragent.txt","rb")
    titleus = (
        f"User-Agent android\n"
        f"Количество: 80 шт.")
    await bot.send_document(chat_id,f, caption=titleus)   


# Обработка кнопки "FAQ"
@dp.message_handler(text="ℹ FAQ", state="*")
async def show_my_deals(message: types.Message, state: FSMContext):
    await state.finish()
    await message.delete()
    send_msg = bot_description
    if "{username}" in send_msg:
        send_msg = send_msg.replace("{username}", f"<b>{message.from_user.username}</b>")
    if "{user_id}" in send_msg:
        send_msg = send_msg.replace("{user_id}", f"<b>{message.from_user.id}</b>")
    if "{firstname}" in send_msg:
        send_msg = send_msg.replace("{firstname}", f"<b>{(message.from_user.first_name)}</b>")
    await message.answer(send_msg, disable_web_page_preview=True)


@dp.callback_query_handler  (text="ip", state="*")
async def reg_url(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await state.finish()
    await call.message.answer('Введите IP Адрес Жертвы')
    await cicada.ip_up.set()


@dp.message_handler(state=cicada.ip_up)
async def reg_uip(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            data['cicada.ip_up'] = message.text
            r = requests.get(f"https://api.ipdata.co/{message.text}?api-key=7149ffee49a432bb1c7557e3235afdf78a2d22fcdde3a4ecd7a5d5ca")
            data = json.loads(r.text)
            city = str(data['city'])
            region = str(data['region'])
            country_name = str(data['country_name'])
            country_code = str(data['country_code'])
            continent_name = str(data['continent_name'])
            continent_code = str(data['continent_code'])
            calling_code = str(data['calling_code'])
            latitude = str(data['latitude'])
            longitude = str(data['longitude'])
            postal = str(data['postal'])
            
            time_zone = str(data['time_zone']['name'])
            time_zone2 = str(data['time_zone']['current_time'])
            
            currency = str(data['currency']['name'])
            currency2 = str(data['currency']['code'])
            
            #languages = str(data['languages']['name']) Error = list indices must be integers or slices, not str
            
            await bot.send_message(message.chat.id, f'''<b> 🔎 Результат поиска:</b>

    <b>IP</b> - {message.text}

    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    <b>Город</b>: {city} | {region}
    <b>Страна</b>: {country_name} ({country_code})
    <b>Часовой пояс</b>: {time_zone}
    <b>Код страны</b>: +{calling_code}
    <b>Широта</b>: {latitude} | <b>Долгота</b>: {longitude}
    <b>Почтовый индекс</b>: {postal}
    <b>Континет</b>: {continent_name} ({continent_code})
    ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
    <b>Валюта</b>: {currency} ({currency2})
    <b>Точное время</b>: {time_zone2}
                            ''', parse_mode='HTML')
            #func.act_count_ip("add", message.chat.id,)
        except Exception as e:
            await bot.send_message(message.chat.id, 'Не верный айпи! Попробуйте еще раз')
            print(e)






# Обработка колбэка "Мои покупки"
@dp.callback_query_handler(text="my_buy", state="*")
async def show_referral(call: CallbackQuery, state: FSMContext):
    last_purchases = last_purchasesx(call.from_user.id)
    if len(last_purchases) >= 1:
        await call.message.delete()
        count_split = 0
        save_purchases = []
        for purchases in last_purchases:
            save_purchases.append(f"<b>📃 Код Выдачи:</b> #{purchases[4]}\n"
                                  f"▶ {purchases[9]} | {purchases[5]} шт \n"
                                  f"🕜 {purchases[13]}\n"
                                  f"{purchases[10]}")
        await call.message.answer("<b>ℹ️ Последние 10 запросов</b>\n"
                                  "➖➖➖➖➖➖➖➖➖➖➖➖➖")
        save_purchases.reverse()
        len_purchases = len(save_purchases)
        if len_purchases > 4:
            count_split = round(len_purchases / 4)
            count_split = len_purchases // count_split
        if count_split > 1:
            get_message = split_messages(save_purchases, count_split)
            for msg in get_message:
                send_message = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n".join(msg)
                await call.message.answer(send_message)
        else:
            send_message = "\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n".join(save_purchases)
            await call.message.answer(send_message)

        await call.message.answer(get_user_profile(call.from_user.id), reply_markup=open_profile_inl)
    else:
        await call.answer("❗ Ты еще не брал Акаунт(ы)")


################################################################################################
######################################### ПОКУПКА ТОВАРА #######################################
# Открытие категории для покупки
@dp.callback_query_handler(text_startswith="buy_open_category", state="*")
async def open_category_for_buy_item(call: CallbackQuery, state: FSMContext):
    category_id = int(call.data.split(":")[1])
    get_category = get_categoryx("*", category_id=category_id)
    get_positions = get_positionsx("*", category_id=category_id)

    get_kb = buy_item_item_position_ap(0, category_id)
    if len(get_positions) >= 1:
        await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                     reply_markup=get_kb)
    else:
        await call.answer(f"❕ Акаунт(ы) в категории {get_category[2]} отсутствуют.")


# Вернутсья к предыдущей категории при покупке
@dp.callback_query_handler(text_startswith="back_buy_item_to_category", state="*")
async def back_category_for_buy_item(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_open_category_ap(0))


# Следующая страница категорий при покупке
@dp.callback_query_handler(text_startswith="buy_category_nextp", state="*")
async def buy_item_next_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_next_page_category_ap(remover))


# Предыдущая страница категорий при покупке
@dp.callback_query_handler(text_startswith="buy_category_prevp", state="*")
async def buy_item_prev_page_category(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=buy_item_previous_page_category_ap(remover))


# Следующая страница позиций при покупке
@dp.callback_query_handler(text_startswith="buy_position_nextp", state="*")
async def buy_item_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=item_buy_next_page_position_ap(remover, category_id))


# Предыдущая страница позиций при покупке
@dp.callback_query_handler(text_startswith="buy_position_prevp", state="*")
async def buy_item_prev_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.edit_text("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                                 reply_markup=item_buy_previous_page_position_ap(remover, category_id))


# Возвращение к страницам позиций при покупке товара
@dp.callback_query_handler(text_startswith="back_buy_item_position", state="*")
async def buy_item_next_page_position(call: CallbackQuery, state: FSMContext):
    remover = int(call.data.split(":")[1])
    category_id = int(call.data.split(":")[2])

    await call.message.delete()
    await call.message.answer("<b>🔐 Выберите нужный вам Акаунт(ы):</b>",
                              reply_markup=buy_item_item_position_ap(remover, category_id))


# Открытие позиции для покупки
@dp.callback_query_handler(text_startswith="buy_open_position", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])
    remover = int(call.data.split(":")[2])
    category_id = int(call.data.split(":")[3])

    get_position = get_positionx("*", position_id=position_id)
    get_category = get_categoryx("*", category_id=category_id)
    get_items = get_itemsx("*", position_id=position_id)

    send_msg = f"<b>🔐 Выбор Акаунта:</b>\n" \
               f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n" \
               f"<b>📜 Категория:</b> {get_category[2]}\n" \
               f"<b>🏷 Название:</b> {get_position[2]}\n" \
               f"<b>📦 Количество:</b> {len(get_items)}шт\n" \
               f"<b>📜 Описание:</b>\n" \
               f"{get_position[4]}\n"
    if len(get_position[5]) >= 5:
        await call.message.delete()
        await call.message.answer_photo(get_position[5],
                                        send_msg,
                                        reply_markup=open_item_func(position_id, remover, category_id))
    else:
        await call.message.edit_text(send_msg,
                                     reply_markup=open_item_func(position_id, remover, category_id))


# Выбор кол-ва товаров для покупки
@dp.callback_query_handler(text_startswith="buy_this_item", state="*")
async def open_category_for_create_position(call: CallbackQuery, state: FSMContext):
    position_id = int(call.data.split(":")[1])

    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=call.from_user.id)
    if len(get_items) >= 1:
        if int(get_user[4]) >= int(get_position[3]):
            async with state.proxy() as data:
                data["here_cache_position_id"] = position_id
            await call.message.delete()
            await StorageUsers.here_input_count_buy_item.set()
            await call.message.answer(f"📦 <b>Введите количество Акаунтов для получения</b>\n"
                                      f"▶ От 1 до 3\n"
                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                      f"🏷 Название Акаунта: {get_position[2]}\n"
                                      f"❗❗❗ Вам Доступно: {get_user[4]} шт\n",
                                      reply_markup=all_back_to_main_default)
        else:
            await call.answer("❗ Лимит Исчерпан ❗Для поднятия лимита писать Админу"),
            await call.answer("❗ Для поднятия лимита писать Админу❗")
    else:
        await call.answer("🔐 Акаунтов нет в наличии.")


# Принятие кол-ва товаров для покупки
@dp.message_handler(state=StorageUsers.here_input_count_buy_item)
async def input_buy_count_item(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        position_id = data["here_cache_position_id"]
    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=message.from_user.id)

    if message.text.isdigit():
        get_count = int(message.text)
        amount_pay = int(get_position[3]) * get_count
        if len(get_items) >= 1:
            if 1 <= get_count <= len(get_items):
                if 30 >= amount_pay:
                    await state.finish()
                    delete_msg = await message.answer("<b>🔐 Акаунты подготовлены.</b>",
                                                      reply_markup=check_user_out_func(message.from_user.id))

                    await message.answer(f"<b>🔐 Получить Акаут(ы)?</b>\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"🏷 Название Акаунта: {get_position[2]}\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"▶ Количество Акаунтов: {get_count} шт\n",
                                         reply_markup=confirm_buy_items(position_id, get_count,
                                                                        delete_msg.message_id))
                else:
                    await message.answer(f"<b>❌ Лимит исчерпан (3 акаунта в сутки).</b>\n"
                                         f"<b>📦 Введите количество Акаунтов для выдачи лимит (3 акаунта в сутки)</b>\n"
                                         f"▶ От 1 до 2\n"
                                         f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                         f"📦 Тебе доступно: {get_user[4]} шт\n"
                                         f"🏷 Название Акаунта: {get_position[2]}\n",
                                         reply_markup=all_back_to_main_default)
            else:
                await message.answer(f"<b>❌ Неверное количество Акаунтов.</b>\n"
                                     f"<b>📦 Введите количество Акаунтов для выдачи</b>\n"
                                     f"▶ От 1 до 2\n"
                                     f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                     f"📦 Тебе доступно: {get_user[4]} шт\n"
                                     f"🏷 Название Акаунтов: {get_position[2]}\n",
                                     reply_markup=all_back_to_main_default)
        else:
            await state.finish()
            await message.answer("<b>❌ Акаунты который ты выбрал закончились</b>",
                                 reply_markup=check_user_out_func(message.from_user.id))
    else:
        await message.answer(f"<b>❌ Данные были введены неверно.</b>\n"
                             f"<b>📦 Введите количество Акаунтов для выдачи</b>\n"
                             f"▶ От 1 до 3\n"
                             f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                             f"📦 Тебе доступно: {get_user[4]} шт\n"
                             f"🏷 Название Акаунтов: {get_position[2]}\n",
                             reply_markup=all_back_to_main_default)


# Отмена покупки товара
@dp.callback_query_handler(text_startswith="not_buy_items", state="*")
async def not_buy_this_item(call: CallbackQuery, state: FSMContext):
    message_id = call.data.split(":")[1]
    await call.message.delete()
    await bot.delete_message(call.message.chat.id, message_id)
    await call.message.answer("<b>☑ Ты отменили получение Акаунтов.</b>",
                              reply_markup=check_user_out_func(call.from_user.id))


# Согласие на покупку товара
@dp.callback_query_handler(text_startswith="xbuy_item:", state="*")
async def yes_buy_this_item(call: CallbackQuery, state: FSMContext):
    
    delete_msg = await call.message.answer("<b>🔄 Жди, Акаунты подготавливаются</b>")
    position_id = int(call.data.split(":")[1])
    get_count = int(call.data.split(":")[2])
    message_id = int(call.data.split(":")[3])

    await bot.delete_message(call.message.chat.id, message_id)
    await call.message.delete()

    get_items = get_itemsx("*", position_id=position_id)
    get_position = get_positionx("*", position_id=position_id)
    get_user = get_userx(user_id=call.from_user.id)
    amount_pay = int(get_position[3]) * get_count

    if 1 <= int(get_count) <= len(get_items):
        if int(get_user[4]) >= amount_pay:
            save_items, send_count, split_len = buy_itemx(get_items, get_count)

            if split_len <= 50:
                split_len = 70
            elif split_len <= 100:
                split_len = 50
            elif split_len <= 150:
                split_len = 30
            elif split_len <= 200:
                split_len = 10
            else:
                split_len = 3

            if get_count != send_count:
                amount_pay = int(get_position[3]) * send_count
                get_count = send_count

            random_number = [random.randint(100000000, 999999999)]
            passwd = list("ABCDEFGHIGKLMNOPQRSTUVYXWZ")
            random.shuffle(passwd)
            random_char = "".join([random.choice(passwd) for x in range(1)])
            receipt = random_char + str(random_number[0])
            buy_time = get_dates()

            await bot.delete_message(call.from_user.id, delete_msg.message_id)

            if len(save_items) <= split_len:
                send_message = "\n".join(save_items)
                await call.message.answer(f"<b>🔐 Твои Акаунты:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                          f"<span class='tg-spoiler'>{send_message}</span>")
            else:
                await call.message.answer(f"<b>🔐 Твои Акаунты:</b>\n"
                                          f"➖➖➖➖➖➖➖➖➖➖➖➖➖")

                save_split_items = split_messages(save_items, split_len)
                for item in save_split_items:
                    send_message = "\n".join(item)
                    await call.message.answer()
            save_items = "\n".join(save_items)

            add_purchasex(call.from_user.id, call.from_user.username, call.from_user.first_name,
                          receipt, get_count, amount_pay, get_position[3], get_position[1], get_position[2],
                          save_items, get_user[4], int(get_user[4]) - amount_pay, buy_time, int(time.time()))
            update_userx(call.from_user.id, balance=get_user[4] - amount_pay)
            await call.message.answer(f"<b>🔐 Ты получил Акаунт(ы) ✅</b>\n"
                                      f"➖➖➖➖➖➖➖➖➖➖➖➖➖\n"
                                      f"🏷 Название Акаунтов: {get_position[2]}\n"
                                      f"📦 Полученно Акаунтов: {get_count}\n"
                                      f"👤 Выданно: <a href='tg://user?id={get_user[1]}'>{get_user[3]}</a> ({get_user[1]})\n"
                                      f"🕜 Дата Выдачи: {buy_time}",
                                      reply_markup=check_user_out_func(call.from_user.id))
        else:
            await call.message.answer("<b>❌ Лимит исчерпан (3 акаунта в сутки).</b>")
    else:
        await state.finish()
        await call.message.answer("<b>❌ Акаунты который ты выбрал закончились.</b>",
                                  check_user_out_func(call.from_user.id))
@dp.callback_query_handler(text='tttt')
async def lica_message(call: types.CallbackQuery):
    chat_id = call.message.chat.id
    with open('ccc.webp', 'rb') as photo:
        await bot.send_photo(chat_id=chat_id, photo=photo, reply_markup=check_user_out_func(call.message.from_user.id))
