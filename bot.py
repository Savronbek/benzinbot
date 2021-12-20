import logging
from aiogram import Bot, Dispatcher, executor, types
import config as nav
from data import *
from db import BotDB

# from aiogram import typing    


admin_id = 2020285924
BotDB = BotDB('users.db')
TOKEN = "2130598875:AAFO9ZLU8_crI5caGkfDX5xjH9VSXX1rCTo"
CHANNEL_ID = "@dunyonews_ru"
CHANNEL_ID_UZ = "@uzdunyonews"
NOTSUB_MESSAGE = "Для доступа к функионалу бота, подпишитесь на канал"
NOTSUB_MESSAGE_UZ = "Botni ishlatish uchun, birinchi kanalga obuna bo'ling"

logging.basicConfig(level=logging.INFO)

# Initialize Bot
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




def check_sub_channel(chat_member):
    print(chat_member['status'])
    if chat_member['status'] != 'left':
        return True
    else:
        return False


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await bot.send_message(message.from_user.id, "Tilingizni tanlang\n\nВыберите свой язык", reply_markup=nav.uzbrus)

@dp.message_handler(user_id=admin_id, commands=['admin'])
async def admin_panel(message: types.Message):
    await BotDB.all_users(message)



@dp.message_handler()
async def bot_message(message: types.Message):

    if message.text == "🇷🇺Русский язык":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Здравствуйте! Теперь вы можете узнать все цены ", reply_markup=nav.profileKeyboard)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "🇺🇿O'zbek tili":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Ассалому алейкум! Бензин нархларини билиб олишингиз мумкин", reply_markup=nav.btn_uz_1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


    elif message.text == "Цены на бензин":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Все доступные виды топлива', reply_markup=nav.ai_next1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
   

    elif message.text == "Главное меню":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Выберите кнопки ниже', reply_markup=nav.profileKeyboard)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)


    elif message.text == "⛽️ Uzgazoil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/ai80.jpg', 'rb') as photo1:
                await bot.send_photo(message.from_user.id, photo = photo1, 
                    caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 6890\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> 9500\n\n<b>📍Локация:</b> Яшнабадский, Шайхонтахурский, Чиланзарский, Алмазарский, Яккасарайский и др. районы ', 
                    parse_mode='HTML', reply_markup=nav.key_b1, 
                    disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)



    elif message.text == "⛽️ Mustang":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/mustang.png', 'rb') as photo2:
                await bot.send_photo(message.from_user.id, photo=photo2, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9700\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> 10 300\n\n<b>📍Локация: </b>Чиланзарский, Сергелийский, Алмазарский, Яшнабадский и др. районы', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ Intrans Servis":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/intrans_servis.png', 'rb') as photo3:
                await bot.send_photo(message.from_user.id, photo=photo3, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 8000\n<b>АИ-92:</b> 9700\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Фархадский, Караташ, Юнусабад', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ Poytaxt Oil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/poytaxt.png', 'rb') as photo4:
                await bot.send_photo(message.from_user.id, photo=photo4, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Мирабадский, Юнусабад', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ Oil Service":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/qoganiga.jpg', 'rb') as photo5:
                await bot.send_photo(message.from_user.id, photo=photo5, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9500\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Сергели, Юнусабад, Учтепинский районы', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ DP":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/qoganiga.jpg', 'rb') as photo6:
                await bot.send_photo(message.from_user.id, photo=photo6, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9400\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9600\n\n<b>📍Локация: </b>Сергели, Чиланзар, Яшнабад', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ IBR":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/ibr.png', 'rb') as photo7:
                await bot.send_photo(message.from_user.id, photo=photo7, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Ватан, Малая Кольцевая, Универсам', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ Tatneft":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/tatneft.png', 'rb') as photo8:
                await bot.send_photo(message.from_user.id, photo=photo8, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 8 400\n<b>АИ-92:</b> 10 500\n<b>АИ-95:</b> 11 500\n<b>Дизель:</b> 9900\n\n<b>📍Локация: </b>Шайхонтахурский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ Lukoil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/lukoil.png', 'rb') as photo9:
                await bot.send_photo(message.from_user.id, photo=photo9, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 8490\n<b>АИ-92:</b> 10 190\n<b>АИ-95:</b> 10 690\n<b>Дизель:</b> 9990\n\n<b>📍Локация: </b>Яшнабадский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ DIP OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):

            with open('data/dip_oil.png', 'rb') as photo10:
                await bot.send_photo(message.from_user.id, photo=photo10, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 10 200\n<b>АИ-95:</b> 11 500\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Ул. Янги Юнусабад', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ OK OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo11:
                await bot.send_photo(message.from_user.id, photo=photo11, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> 9300\n\n<b>📍Локация: </b>ТКАД, САМПИ', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ MBS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo12:
                await bot.send_photo(message.from_user.id, photo=photo12, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Гвардейский, Юнусабад', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ Arena Petrol":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo13:
                await bot.send_photo(message.from_user.id, photo=photo13, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9500\n\n<b>📍Локация: </b>Корзинка Эльбек', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "⛽️ Petrol Exclusive":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo14:
                await bot.send_photo(message.from_user.id, photo=photo14, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Корзинка Эльбек', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ Fath OIl":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo15:
                await bot.send_photo(message.from_user.id, photo=photo15, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Локация: </b>Ташсельмаш', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ BRC":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo16:
                await bot.send_photo(message.from_user.id, photo=photo16, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-91:</b> 9900\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Рохат, ТКАД, Шошкафе', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ NSS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo17:
                await bot.send_photo(message.from_user.id, photo=photo17, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-91:</b> 9200\n<b>АИ-92:</b> 9600\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Крестик, Яшнабадский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ UZMAL OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/uzmal_oil.png', 'rb') as photo18:
                await bot.send_photo(message.from_user.id, photo=photo18, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> 9400\n\n<b>📍Локация: </b>Юнусабад-19 квартал', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ GATEWAY KOREA":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo19:
                await bot.send_photo(message.from_user.id, photo=photo19, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Локация: </b>Узбум, Яшнабадский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ OKTAN PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/oktan_petrol.png', 'rb') as photo20:
                await bot.send_photo(message.from_user.id, photo=photo20, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Локация: </b>Электроаппарат, Яшнабадский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ SO PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/so_petrol.png', 'rb') as photo21:
                await bot.send_photo(message.from_user.id, photo=photo21, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9400\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Шастри, Паркентский', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ RS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo22:
                await bot.send_photo(message.from_user.id, photo=photo22, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7600\n<b>АИ-92:</b> 9500\n<b>АИ-95:</b> 9950\n<b>Дизель:</b> 9400\n\n<b>📍Локация: </b>Боткино, Яшнабадский район', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ MISS PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/miss_petrol.png', 'rb') as photo23:
                await bot.send_photo(message.from_user.id, photo=photo23, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-91:</b> 10 000\n<b>АИ-92:</b> 9700\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Южный вокзал', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ ZTE":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/zte.png', 'rb') as photo24:
                await bot.send_photo(message.from_user.id, photo=photo24, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 8000\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9300\n\n<b>📍Локация: </b>Водник', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ POWER LINE 1":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/power_line_1.png', 'rb') as photo25:
                await bot.send_photo(message.from_user.id, photo=photo25, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-91:</b> 9800\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Абу Сахий', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ AZS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo26:
                await bot.send_photo(message.from_user.id, photo=photo26, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 8200\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> 9800\n\n<b>📍Локация: </b>ТКАД, Урикзор', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ CHEMPION OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo27:
                await bot.send_photo(message.from_user.id, photo=photo27, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9800\n\n<b>📍Локация: </b>ТКАД, Урикзор', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ SHGS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo28:
                await bot.send_photo(message.from_user.id, photo=photo28, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 6980\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>ТКАД, Абу Сахий', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

    elif message.text == "⛽️ Full OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo28:
                await bot.send_photo(message.from_user.id, photo=photo28, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7300\n<b>АИ-92:</b> 9400\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9500\n\n<b>📍Локация: </b>Пост Карамурт', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)


    elif message.text == "⛽️ IMB":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo28:
                await bot.send_photo(message.from_user.id, photo=photo28, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7400\n<b>АИ-91:</b> 9800\n<b>АИ-92:</b> 9800\n<b>Дизель:</b> -\n\n<b>📍Локация: </b>Сельхоз', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)



    elif message.text == "Назад":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Вы вернулись назад!', reply_markup=nav.ai_next1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "Назад.":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Вы вернулись назад!', reply_markup=nav.ai_next2)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    # elif message.text == "Назад..":
        # await bot.send_message(message.from_user.id, 'Цены на бензин:\n\nАИ-80: 6980\nАИ-92: 9800\nАИ-95: 10 000\nДизель: 9500', reply_markup=key_b1)

    elif message.text == "Еще":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Другие бензоколонки👇', reply_markup=nav.ai_next2)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
    elif message.text == "Еще.":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Еще больше бензоколонок👇', reply_markup=nav.ai_next3)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)    

















    elif message.text == "Асосий меню":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, "Сиз асосий менюга қайттингиз", reply_markup=nav.btn_uz_1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


    elif message.text == "Бензин нархлари":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Барча маълум бўлган бензин нархлари', reply_markup=nav.uz_petrol_1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


    elif message.text == "⛽️Uzgazoil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/ai80.jpg', 'rb') as photo1:
                await bot.send_photo(message.from_user.id, photo = photo1, 
                    caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 6890\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> 9500\n\n<b>📍Жойлашув:</b> Яшнобод, Шайхонтохур, Чилонзор, Олмазор, Яккасарой ва бошка туманлар ', 
                    parse_mode='HTML', reply_markup=nav.key_share, 
                    disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


# shu yerdan
    elif message.text == "⛽️Mustang":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/mustang.png', 'rb') as photo2:
                await bot.send_photo(message.from_user.id, photo=photo2, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9700\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> 10 300\n\n<b>📍Жойлашув: </b>Чилонзор, Сергели, Олмазор, Яшнобод ва бошка туманлар', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️Intrans Servis":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/intrans_servis.png', 'rb') as photo3:
                await bot.send_photo(message.from_user.id, photo=photo3, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 8000\n<b>АИ-92:</b> 9700\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Фархадский, Қоратош, Юнусобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️Poytaxt Oil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/poytaxt.png', 'rb') as photo4:
                await bot.send_photo(message.from_user.id, photo=photo4, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Миробод, Юнусобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️Oil Service":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/qoganiga.jpg', 'rb') as photo5:
                await bot.send_photo(message.from_user.id, photo=photo5, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9500\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Сергели, Юнусобод, Учтепа туманлари', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️DP":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/qoganiga.jpg', 'rb') as photo6:
                await bot.send_photo(message.from_user.id, photo=photo6, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9400\n<b>АИ-95:</b> 9 900\n<b>Дизель:</b> 9600\n\n<b>📍Жойлашув: </b>Сергели, Чилонзор, Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️IBR":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/ibr.png', 'rb') as photo7:
                await bot.send_photo(message.from_user.id, photo=photo7, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Ватан, Малая Кольцевая(Кичик Халқа), Универсам', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️Tatneft":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/tatneft.png', 'rb') as photo8:
                await bot.send_photo(message.from_user.id, photo=photo8, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 8 400\n<b>АИ-92:</b> 10 500\n<b>АИ-95:</b> 11 500\n<b>Дизель:</b> 9900\n\n<b>📍Жойлашув: </b>Шайхонтохур райони', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️Lukoil":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/lukoil.png', 'rb') as photo9:
                await bot.send_photo(message.from_user.id, photo=photo9, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 8490\n<b>АИ-92:</b> 10 190\n<b>АИ-95:</b> 10 690\n<b>Дизель:</b> 9990\n\n<b>📍Жойлашув: </b>Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️DIP OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):

            with open('data/dip_oil.png', 'rb') as photo10:
                await bot.send_photo(message.from_user.id, photo=photo10, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 10 200\n<b>АИ-95:</b> 11 150\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Янги Юнусобод к.', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️OK OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo11:
                await bot.send_photo(message.from_user.id, photo=photo11, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 500\n<b>Дизель:</b> 9300\n\n<b>📍Жойлашув: </b>ТКАД, САМПИ', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️MBS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo12:
                await bot.send_photo(message.from_user.id, photo=photo12, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Гвардейский, Юнусобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️Arena Petrol":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo13:
                await bot.send_photo(message.from_user.id, photo=photo13, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9500\n\n<b>📍Жойлашув: </b>Корзинка Элбек', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "⛽️Petrol Exclusive":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo14:
                await bot.send_photo(message.from_user.id, photo=photo14, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Корзинка Элбек', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️Fath OIl":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo15:
                await bot.send_photo(message.from_user.id, photo=photo15, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9800\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Жойлашув: </b>Ташсельмаш', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️BRC":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo16:
                await bot.send_photo(message.from_user.id, photo=photo16, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-91:</b> 9900\n<b>АИ-92:</b> 9800\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Рохат, ТКАД, Шошкафе', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️NSS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo17:
                await bot.send_photo(message.from_user.id, photo=photo17, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-91:</b> 9200\n<b>АИ-92:</b> 9600\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Крестик, Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️UZMAL OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/uzmal_oil.png', 'rb') as photo18:
                await bot.send_photo(message.from_user.id, photo=photo18, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7700\n<b>АИ-92:</b> 9900\n<b>АИ-95:</b> 11 600\n<b>Дизель:</b> 9400\n\n<b>📍Жойлашув: </b>Юнусабад-19 квартал', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️GATEWAY KOREA":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo19:
                await bot.send_photo(message.from_user.id, photo=photo19, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Жойлашув: </b>Узбум, Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️OKTAN PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/oktan_petrol.png', 'rb') as photo20:
                await bot.send_photo(message.from_user.id, photo=photo20, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 400\n<b>Дизель:</b> 9700\n\n<b>📍Жойлашув: </b>Электроаппарат, Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️SO PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/so_petrol.png', 'rb') as photo21:
                await bot.send_photo(message.from_user.id, photo=photo21, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9400\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Шастри, Паркентский', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️RS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo22:
                await bot.send_photo(message.from_user.id, photo=photo22, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7600\n<b>АИ-92:</b> 9500\n<b>АИ-95:</b> 9950\n<b>Дизель:</b> 9400\n\n<b>📍Жойлашув: </b>Боткино, Яшнобод', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️MISS PETROL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/miss_petrol.png', 'rb') as photo23:
                await bot.send_photo(message.from_user.id, photo=photo23, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-91:</b> 10 000\n<b>АИ-92:</b> 9700\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Южный вокзал', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️CHEMPION OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo23:
                await bot.send_photo(message.from_user.id, photo=photo23, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9800\n\n<b>📍Жойлашув: </b>ТКАД, Ўрикзор', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)




    elif message.text == "⛽️ZTE":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/zte.png', 'rb') as photo24:
                await bot.send_photo(message.from_user.id, photo=photo24, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 8000\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9300\n\n<b>📍Жойлашув: </b>Водник', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️POWER LINE 1":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/power_line_1.png', 'rb') as photo25:
                await bot.send_photo(message.from_user.id, photo=photo25, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7500\n<b>АИ-91:</b> 9800\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Абу Сахий', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️AZS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo26:
                await bot.send_photo(message.from_user.id, photo=photo26, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 8200\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 10 200\n<b>Дизель:</b> 9800\n\n<b>📍Жойлашув: </b>ТКАД, Ўрикзор', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "⛽️FULL OIL":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo26:
                await bot.send_photo(message.from_user.id, photo=photo26, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7300\n<b>АИ-92:</b> 9400\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9500\n\n<b>📍Жойлашув: </b>Пост Карамурт', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


    elif message.text == "⛽️IMB":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo26:
                await bot.send_photo(message.from_user.id, photo=photo26, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7400\n<b>АИ-91:</b> 9800\n<b>АИ-92:</b> 9800\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>Сельхоз', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)







    elif message.text == "⛽️SHGS":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            with open('data/qoganiga.jpg', 'rb') as photo28:
                await bot.send_photo(message.from_user.id, photo=photo28, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7900\n<b>АИ-91:</b> 9600\n<b>АИ-95:</b> -\n<b>Дизель:</b> -\n\n<b>📍Жойлашув: </b>ТКАД, Абу Сахий', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)

    elif message.text == "Орқага":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Сиз орқага қайттингиз!', reply_markup=nav.uz_petrol_1)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    elif message.text == "Орқага.":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Сиз орқага қайттингиз!', reply_markup=nav.uz_petrol_2)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)
    # elif message.text == "Назад..":
        # await bot.send_message(message.from_user.id, 'Цены на бензин:\n\nАИ-80: 6980\nАИ-92: 9800\nАИ-95: 10 000\nДизель: 9500', reply_markup=key_b1)

    elif message.text == "Кўпроқ":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Қолган бензин шахобчалари👇', reply_markup=nav.uz_petrol_2)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)


    elif message.text == "Кўпроқ.":
        if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
            await bot.send_message(message.from_user.id, 'Қолган бензин шахобчалари👇', reply_markup=nav.uz_petrol_3)
        else:
            await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)






    else:
        await bot.send_message(message.from_user.id, 'Не понимаю о чем вы\n\nНотўғри хабар')







# russian subscrition to channel
@dp.callback_query_handler(text="subchanneldone")
async def subchanneldone(message: types.Message):
    # await bot.delete_message(message.from_user.id, message.message.message_id)
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Здравствуйте! Выберите кнопки ниже", reply_markup=nav.profileKeyboard)
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)

# uzbek subscription to channel
@dp.callback_query_handler(text="uzbsubchanneldone")
async def uzbsubchanneldone(message: types.Message):
    if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Ассалому алейкум! Бензин нархларини билиб олишингиз мумкин", reply_markup=nav.btn_uz_1)
    else:
        await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)            





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



































    # elif message.text == "⛽️CHEMPION OIL":
    #     if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID_UZ, user_id=message.from_user.id)):
    #         with open('data/qoganiga.jpg', 'rb') as photo27:
    #             await bot.send_photo(message.from_user.id, photo=photo27, caption='<b>Бензин нархлари:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9800\n\n<b>📍Жойлашув: </b>ТКАД, Ўрикзор', parse_mode='HTML', reply_markup=nav.key_share, disable_notification=True)
    #     else:
    #         await bot.send_message(message.from_user.id, NOTSUB_MESSAGE_UZ, reply_markup=nav.checkUzMenu)





    # elif message.text == "⛽️ CHEMPION OIL":
    #     if check_sub_channel(await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=message.from_user.id)):
    #         with open('data/qoganiga.jpg', 'rb') as photo27:
    #             await bot.send_photo(message.from_user.id, photo=photo27, caption='<b>Цены на бензин:</b>\n\n<b>АИ-80:</b> 7800\n<b>АИ-92:</b> 9600\n<b>АИ-95:</b> 9900\n<b>Дизель:</b> 9800\n\n<b>📍Локация: </b>ТКАД, Урикзор', parse_mode='HTML', reply_markup=nav.key_b1, disable_notification=True)
    #     else:
    #         await bot.send_message(message.from_user.id, NOTSUB_MESSAGE, reply_markup=nav.checkSubMenu)
