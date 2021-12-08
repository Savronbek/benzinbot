from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove
import os
import emoji






# Подписка на канал на узбекском языке
uzb1 = InlineKeyboardButton(text="Обуна бўлиш", url="https://t.me/uzdunyonews")
uzb1Done = InlineKeyboardButton(text="Обуна бўлдим", callback_data="uzbsubchanneldone")
checkUzMenu = InlineKeyboardMarkup(row_width=1)
checkUzMenu.insert(uzb1)
checkUzMenu.insert(uzb1Done)


# a = emoji.emojize(":ru:", use_aliases=True)
# Language in uzbek and russian
uzb = KeyboardButton("🇺🇿O'zbek tili")
rus = KeyboardButton("🇷🇺Русский язык")
uzbrus = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True).add(uzb).add(rus)



# Главное меню
btnMain = KeyboardButton('Главное меню')

# Не трогать
btnProfile = KeyboardButton('Цены на бензин')
profileKeyboard = ReplyKeyboardMarkup(resize_keyboard = True).add(btnProfile)

#uzb
# benz = KeyboardButton('Benzin narxlari')
# benz1 = ReplyKeyboardMarkup(resize_keyboard=True).add(benz)



btnurlChannel = InlineKeyboardButton(text="Подписаться", url="https://t.me/dunyonews_ru")
btnDoneSub = InlineKeyboardButton(text="Проверить подписку", callback_data="subchanneldone")
checkSubMenu = InlineKeyboardMarkup(row_width=1) 
checkSubMenu.insert(btnurlChannel)
checkSubMenu.insert(btnDoneSub)


# Основные цены бензина
# b1 = KeyboardButton('АИ-80')
# b2 = KeyboardButton('АИ-92')
# b3 = KeyboardButton('АИ-95')
# b4 = KeyboardButton('Дизель')

# kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
# kb_client.add(b1, b2, b3, b4, btnMain)

# Детальные кнопки для бензина АИ 80
ai_80a = KeyboardButton('⛽️ Uzgazoil') # 1
ai_80b = KeyboardButton('⛽️ Mustang')  # 2
ai_80c = KeyboardButton('⛽️ Intrans Servis') # 1
ai_80d = KeyboardButton('⛽️ Poytaxt Oil') # 5
ai_80e = KeyboardButton('⛽️ Oil Service') # 3
ai_80f = KeyboardButton('⛽️ DP') # 1
ai_80g = KeyboardButton('⛽️ IBR') # 3
ai_80h = KeyboardButton('⛽️ Tatneft') # 2
ai_80i = KeyboardButton('⛽️ Lukoil') # 2
# ai_80j = KeyboardButton('Full Oil') # 3
ai_80k = KeyboardButton('⛽️ DIP OIL') # 4
# ai_80l = KeyboardButton('Good OIL') # 1
ai_80m = KeyboardButton('⛽️ OK OIL') # 1
# ai_80n = KeyboardButton('IMB') # 1
# ai_80o = KeyboardButton('BRC') # 1
ai80_p = KeyboardButton('⛽️ MBS')
ai80_q = KeyboardButton('⛽️ Arena Petrol')
ai80_r = KeyboardButton('⛽️ Petrol Exclusve')
ai80_s = KeyboardButton('⛽️ Fath OIl')
ai80_t = KeyboardButton('⛽️ BRC')
ai80_u = KeyboardButton('⛽️ NSS')
ai80_v = KeyboardButton('⛽️ UZMAL OIL')
ai80_w = KeyboardButton('⛽️ GATEWAY KOREA')
ai80_x = KeyboardButton('⛽️ OKTAN PETROL')
ai80_y = KeyboardButton('⛽️ SO PETROL')
ai80_z = KeyboardButton('⛽️ RS')
ai80_aa = KeyboardButton('⛽️ MISS PETROL')
ai80_ab = KeyboardButton('⛽️ ZTE')
ai80_ac = KeyboardButton('⛽️ POWER LINE 1')
ai80_ad = KeyboardButton('⛽️ AZS')
ai80_ae = KeyboardButton('⛽️ CHEMPION OIL')
ai80_af = KeyboardButton('⛽️ SHGS')


# Кнопки далее и назад
next1 = KeyboardButton('Еще')
next2 = KeyboardButton('Еще.')
# next3 = KeyboardButton('Еще')
back1 = KeyboardButton('Назад')
back2 = KeyboardButton('Назад.')
# back3 = KeyboardButton('Назад..')


 # Реализация кнопок для импорта к главному файлу
# ai80 = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_80a, ai_80b, ai_80c, ai_80d, ai_80e, ai_80f, ai_80g, ai_80h, ai_80i, ai_80m, ai80_p, ai80_q, ai80_r, ai80_s, ai80_t, ai80_u, ai80_v, ai80_w, ai80_x, ai80_y, ai80_z, ai80_aa, ai80_ab, ai80_ac, ai80_ad, ai80_ae, ai80_af, next1, back, btnMain)
# ai92 = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_80a, ai_80b, ai_80c, ai_80d, ai_80e, ai_80f, ai_80g, ai_80h, ai_80i, ai_80k, ai_80m, ai80_p, ai80_q, ai80_r, ai80_s, ai80_t, ai80_u, ai80_v, ai80_w, ai80_x, ai80_y, ai80_z, ai80_aa, ai80_ab, ai80_ac, ai80_ad, ai80_ae, ai80_af, next1, back, btnMain)
# ai95 = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_80a, ai_80b, ai_80c, ai_80d, ai_80f, ai_80k, ai_80g, ai_80h, ai_80i, ai_80m, ai80_p, ai80_q, ai80_s, ai80_t, ai80_u, ai80_v, ai80_w, ai80_x, ai80_z, ai80_aa, ai80_ab, ai80_ac, ai80_ad, ai80_ae, next1, back, btnMain)
# dizel = ReplyKeyboardMarkup(resize_keyboard=True).add(ai_80a, ai_80b, ai_80f, ai_80h, ai_80i, ai_80m, ai80_q, ai80_r, ai80_s, ai80_v, ai80_w, ai80_x, ai80_z, ai80_ab, ai80_ad, ai80_ae, next1, back, btnMain)




# сортировка
ai_next1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	ai_80a, 
	ai_80b, 
	ai_80c, 
	ai_80d, 
	ai_80e, 
	ai_80f, 
	ai_80g, 
	ai_80h, 
	ai_80i, 
	btnMain, 
	next1)



ai_next2 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	ai_80m, 
	ai80_p, 
	ai80_q, 
	ai80_r, 
	ai80_s, 
	ai80_t, 
	ai80_u, 
	ai80_v, 
	ai80_w, 
	btnMain, 
	back1, 
	next2)



ai_next3 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	ai80_x, 
	ai80_y, 
	ai80_z, 
	ai80_aa, 
	ai_80k, 
	ai80_ab, 
	ai80_ac, 
	ai80_ad, 
	ai80_ae, 
	ai80_af).row(btnMain, back2)



# Инлайн кнопки каждой бензоклонки
# key_b = InlineKeyboardButton(text="Локация", url="https://www.goldenpages.uz/rubrics/?Id=103192")
share_b = InlineKeyboardButton(text='Поделиться', switch_inline_query="Первый и главный бот для узнавания цен на бензин, подпишитесь")
key_b1 = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
# key_b1.insert(key_b)
key_b1.insert(share_b)
# key_b1.row(share_b)

# go_back = ReplyKeyboardMarkup(resize_keyboard=True).add(next1).add(back)

#uzb benzin narxi




uz_80a = KeyboardButton('⛽️Uzgazoil') # 1
uz_80b = KeyboardButton('⛽️Mustang')  # 2
uz_80c = KeyboardButton('⛽️Intrans Servis') # 1
uz_80d = KeyboardButton('⛽️Poytaxt Oil') # 5
uz_80e = KeyboardButton('⛽️Oil Service') # 3
uz_80f = KeyboardButton('⛽️DP') # 1
uz_80g = KeyboardButton('⛽️IBR') # 3
uz_80h = KeyboardButton('⛽️Tatneft') # 2
uz_80i = KeyboardButton('⛽️Lukoil') # 2
uz_80j = KeyboardButton('⛽️DIP OIL') # 4
uz_80k = KeyboardButton('⛽️OK OIL') # 1
uz_80l = KeyboardButton('⛽️MBS')
uz_80m = KeyboardButton('⛽️Arena Petrol')
uz_80n = KeyboardButton('⛽️Petrol Exclusve')
uz_80o = KeyboardButton('⛽️Fath OIl')
uz_80p = KeyboardButton('⛽️BRC')
uz_80q = KeyboardButton('⛽️NSS')
uz_80r = KeyboardButton('⛽️UZMAL OIL')
uz_80s = KeyboardButton('⛽️GATEWAY KOREA')
uz_80t = KeyboardButton('⛽️OKTAN PETROL')
uz_80u = KeyboardButton('⛽️SO PETROL')
uz_80v = KeyboardButton('⛽️RS')
uz_80w = KeyboardButton('⛽️MISS PETROL')
uz_80x = KeyboardButton('⛽️ZTE')
uz_80y = KeyboardButton('⛽️POWER LINE 1')
uz_80z = KeyboardButton('⛽️AZS')
bag = KeyboardButton('⛽️CHEMPION OIL')
uz_80ab = KeyboardButton('⛽️SHGS')

# Кнопки далее и назад на узбекском UZBEK
next_uz_1 = KeyboardButton("Кўпроқ")
next_uz_2 = KeyboardButton("Кўпроқ.")
back_uz_1 = KeyboardButton("Орқага.")
back_uz_2 = KeyboardButton("Орқага")

btn_uz = KeyboardButton("Бензин нархлари")
btn_uz_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_uz)
btnMain_uz = KeyboardButton('Асосий меню')


uz_petrol_1 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	uz_80a,
	uz_80b,
	uz_80c,
	uz_80d,
	uz_80e,
	uz_80f,
	uz_80g,
	uz_80h, 
	uz_80i,
	btnMain_uz,
	next_uz_1)


uz_petrol_2 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	uz_80j,
	uz_80k,
	uz_80l,
	uz_80m,
	uz_80n,
	uz_80o,
	uz_80p,
	uz_80q,
	uz_80r,
	btnMain_uz,
	back_uz_2,
	next_uz_2)

uz_petrol_3 = ReplyKeyboardMarkup(resize_keyboard=True).add(
	uz_80s,
	uz_80t,
	uz_80u,
	uz_80v,
	uz_80w,
	uz_80x,
	bag,
	uz_80y,
	uz_80z, 
	uz_80ab).row(btnMain_uz, back_uz_1)


share_uz = InlineKeyboardButton(text='Яқинлар билан улашиш', switch_inline_query="Бензин нархларини аниқлайдиган энг Биринчи бот")
key_share = InlineKeyboardMarkup(resize_keyboard=True, row_width=2)
key_share.insert(share_uz)

