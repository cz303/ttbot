# -*- coding: utf-8 -*-

import os

import telebot
from telebot import types
import settings
from settings import users as USERS
from settings import order
from settings import admin



bot = telebot.TeleBot(settings.API_TOKEN)


# функция получения реферальной сслки для пользователя
def getRefUrl(u_id):
	u_id = str(u_id)
	refurl = "t.me/thegoodreferalbot?start=" + u_id
	return (refurl)
	

# функция формирования всей требуемой информации о пользователе
def getUserInfo(message):
	u_id = message.from_user.id
	name1 = message.from_user.first_name
	name2 = message.from_user.last_name
	uname = message.from_user.username
	balance = 0
	refurl = getRefUrl(u_id)
	ref1 = []
	ref2 = []
	ref3 = []
	status = 0
	user = dict(zip(["u_id","firstname", "secondname", "username","balance", "refurl", "ref1", "ref2", "ref3", "status"],
	[u_id, name1, name2, uname, balance, refurl, ref1, ref2,ref3, status]))
	return user
	

# данные об админе
def getAdmin(message):
	u_id = message.from_user.id
	name1 = message.from_user.first_name
	name2 = message.from_user.last_name
	uname = message.from_user.username
	status = 6
	email = ""
	com = 0
	admin = dict(zip(["u_id","firstname", "secondname", "username","email", "status"],
	[u_id, name1, name2, uname, email, status]))
	return admin


# функция вывода баланса
def balance_show(message, USERS):
	id = message.from_user.id
	info = USERS.get(id)
	balance = str(info.get("balance"))
	return balance
	

# функция вывода реферальной ссылки
def refurl_show(message, USERS):
	id = message.from_user.id
	info = USERS.get(id)
	refurl = str(info.get("refurl"))
	return refurl
	
	
# функция изменения статуса
def status_change(id, USERS, point):	
	info = USERS.get(id)
	info.update({"status":point})
	print(USERS)
	return USERS 


# функция проверки статуса
def status_check(id):
	a = USERS.get(id)
	status = a.get("status")
	if status == 1:
		return 1
	elif status == 2:
		return 2
	elif status == 3:
		return 3
	elif status == 4:
		return 4
	elif status == 0:
		return 0
	elif status == 6:
		return 6
	elif status == 5:
		return 5
	
# отправка сообщения с заказом админу	
def send_admin(mail, admin):
	admin_id = admin.get("u_id")
	bot.send_message(admin_id, mail)

	

# блок с основным меню
main_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
btn1 = types.KeyboardButton("Как зарабатывать в интернете")
btn2 = types.KeyboardButton("Приглашенные друзья")
btn3 = types.KeyboardButton("Заказать")
main_menu_markup.add(btn1, btn2, btn3)
	

# блок меню "как зарабатывать в интернете"
inet_work_markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
iwb1 = types.KeyboardButton("Способ 1")
iwb2 = types.KeyboardButton("Способ 2")
iwb3 = types.KeyboardButton("Назад")
inet_work_markup.add(iwb1, iwb2, iwb3)


# блок меню "Список приглашенных" и реферальной программы
friedns_list_markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
flb1 = types.KeyboardButton("Ваша реферальная ссылка")
flb2 = types.KeyboardButton("Список приглашенных")
flb3 = types.KeyboardButton("Баланс")
flb4 = types.KeyboardButton("Описание")
flb5 = types.KeyboardButton("Назад")
friedns_list_markup.add(flb1, flb2, flb3, flb4, flb5)


# блок меню админа
admin_menu_markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
ab1 = types.KeyboardButton("Изменить описания заработков")
ab2 = types.KeyboardButton("Изменить описание рефералов")
ab3 = types.KeyboardButton("Изменить описание Заказа")
ab4 = types.KeyboardButton("Изменить e-mail")
admin_menu_markup.add(ab1, ab2, ab3, ab4)


# меню с описаниями
var_markup = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
var1 = types.KeyboardButton("Описание 1")
var2 = types.KeyboardButton("Описание 2")
var_markup.add(var1, var2)


# кнопка для заявки
order_menu = types.InlineKeyboardMarkup(row_width = 1)
order_button = types.InlineKeyboardButton("Оставить заявку", callback_data="Order")
order_menu.add(order_button)


# кнопка для имени
name_menu = types.InlineKeyboardMarkup(row_width = 1)
name_button = types.InlineKeyboardMarkup("Оставить имя")
name_menu.add(name_button)


# кнопка для телефона
phone_menu = types.InlineKeyboardMarkup(row_width = 1)
phone_button = types.InlineKeyboardMarkup("Оставить имя")
phone_menu.add(name_button)


# кнопка для никнейма
tgname_menu = types.InlineKeyboardMarkup(row_width = 1)
tgname_button = types.InlineKeyboardMarkup("Оставить имя")
tgname_menu.add(name_button)


# кнопка для е-mail
mail_menu = types.InlineKeyboardMarkup(row_width = 1)
mail_button = types.InlineKeyboardMarkup("Оставить имя")
mail_menu.add(name_button)


# обработчик специальных команд
@bot.message_handler(commands=['start', 'help', 'admin'])
def send_welcome(message):
	if message.text == "/start":
		bot.send_message(message.chat.id, text = """Приветсвую! Я объясню Вам как заработать в интернете,
		а также буду вести Вашу статистику по нашей реферальной программе.""", reply_markup = main_menu_markup)
		id = message.from_user.id
		user = getUserInfo(message)
		USERS[id] = user
		print(USERS)
		return USERS
	elif message.text == "/help":
		bot.send_message(message.chat.id, text ="""Здесь будет описание того, как мной пользоваться.""")
	elif message.text == "/admin":
		id = message.chat.id
		status = status_check(id)
		print(status)
		bot.send_message(message.chat.id, text ="""Введите пароль:""")
	


# обработчик для навигации по меню бота		
@bot.message_handler(func=lambda message: True)
def main_menu_reply(message):
	if message.text == "Как зарабатывать в интернете":
		bot.send_message(message.chat.id, "Выберите вариант", reply_markup = inet_work_markup)
	elif message.text == "Приглашенные друзья":
		bot.send_message(message.chat.id, "Какую информацию Вы хотите получить?", reply_markup = friedns_list_markup)
	elif message.text == "Назад":
		bot.send_message(message.chat.id, "Чем я могу помочь еще?", reply_markup = main_menu_markup)	
	elif message.text == "Способ 1":
		text = settings.variant1
		bot.send_message(message.chat.id, text, reply_markup = inet_work_markup)
	elif message.text == "Способ 2":
		text = settings.variant2
		bot.send_message(message.chat.id, text, reply_markup = inet_work_markup)
	elif message.text == "Баланс":
		balance = balance_show(message, USERS)
		text = "Ваш баланс \n" + balance + " баллов."
		bot.send_message(message.chat.id, text, reply_markup = friedns_list_markup)
	elif message.text == "Ваша реферальная ссылка":
		refurl = refurl_show(message, USERS)
		text = "Ваша реферальная ссылка (скопируйте, чтобы отправить)\n" + refurl
		bot.send_message(message.chat.id, text, reply_markup = friedns_list_markup)
	elif message.text == "Описание":
		text = settings.refdescribe
		bot.send_message(message.chat.id, text, reply_markup = friedns_list_markup)
	elif message.text == "Список приглашенных":	
		bot.send_message(message.chat.id, "Список приглашенных", reply_markup = friedns_list_markup)
	elif message.text == "Заказать":
		text = settings.order_description
		bot.send_message(message.chat.id, text, reply_markup = order_menu)
	else:
		id = message.chat.id
		status = status_check(id)
		if status == 1:
			status_change(id, USERS, 2)
			settings.order.append(message.text)
			print(order)
			bot.send_message(message.chat.id, "Спасибо! Пожалуйста, укажите Ваш мобтльный телефон:")
		elif status == 2:
			status_change(id, USERS, 3)
			settings.order.append(message.text)
			print(order)
			bot.send_message(message.chat.id, "Спасибо! Пожалуйста, укажите Ваш никнейм в Телеграм:")
		elif status == 3:
			status_change(id, USERS, 4)
			settings.order.append(message.text)
			print(order)
			bot.send_message(message.chat.id, "Спасибо! Пожалуйста, укажите Вашу электронную почту(e-mail):")
		elif status == 4:
			status_change(id, USERS, "ordered")
			settings.order.append(message.text)
			print(settings.order)
			settings.order = "Новый заказ!\nИмя: " + str(order[0]) + "\nТелефон: "  + str(order[1]) + "\nТелеграм никнейм: "  + str(order[2]) + "\nE-mail: " + str(order[3])
			print(settings.order)
			aa = settings.admin
			print(aa)
			send_admin(settings.order, aa)
			bot.send_message(message.chat.id, "Спасибо! Мы свяжемся с Вами в ближайшее время!")
		elif status == 0:
			if message.text == "123456":
				status_change(id, USERS, 6)
				print(status)
				settings.admin = getAdmin(message)
				print(settings.admin)
				bot.send_message(message.chat.id, "Поздравляю, Вы вошли в меню админа!", reply_markup = admin_menu_markup)
				return settings.admin
			else:
				bot.send_message(message.chat.id, "Я вас не понимаю.", reply_markup = main_menu_markup)
		elif status == 6:
			if message.text == "Изменить описания заработков":
				bot.send_message(message.chat.id, "Какое описание вы хотите поменять?", reply_markup = var_markup)
			elif message.text == "Описание 1":
				settings.admin.update({"com":1})
				bot.send_message(message.chat.id, "Напишите новое описание")
			elif settings.admin.get("com") == 1:
				settings.variant1 = message.text	
				bot.send_message(message.chat.id, "Новое описание установлено" ,reply_markup = admin_menu_markup)
				settings.admin.update({"com":0})
			elif message.text == "Описание 2":
				settings.admin.update({"com":2})
				bot.send_message(message.chat.id, "Напишите новое описание")
			elif settings.admin.get("com") == 2:
				settings.variant2 = message.text
				bot.send_message(message.chat.id, "Новое описание установлено", reply_markup = admin_menu_markup)
				settings.admin.update({"com":0})
			elif message.text == "Изменить описание рефералов":
				settings.admin.update({"com":3})
				bot.send_message(message.chat.id, "Напишите новое описание", reply_markup = admin_menu_markup)
			elif message.text == "Изменить описание Заказа":
				settings.admin.update({"com":4})
				bot.send_message(message.chat.id, "Напишите новое описание", reply_markup = admin_menu_markup)
			elif message.text == "Изменить e-mail":
				settings.admin.update({"com":5})
				bot.send_message(message.chat.id, "Напишите новый email", reply_markup = admin_menu_markup)
			elif settings.admin.get("com") == 3:
				settings.refdescribe = message.text
				bot.send_message(message.chat.id, "Новое описание установлено", reply_markup = admin_menu_markup)
				settings.admin.update({"com":0})
			elif settings.admin.get("com") == 4:
				settings.order_description = message.text
				bot.send_message(message.chat.id, "Новое описание установлено", reply_markup = admin_menu_markup)
				settings.admin.update({"com":0})
			elif settings.admin.get("com") == 5:
				settings.admin.update({"email": message.text})
				bot.send_message(message.chat.id, "Новый email установлен", reply_markup = admin_menu_markup)
				print(settings.admin)
				settings.admin.update({"com":0})

			
		
	
# обработчик кнопки заявки		
@bot.callback_query_handler(func=lambda call:True)
def order_menu_reply(call):
	if call.data == "Order":
		id = call.message.chat.id
		print(id)
		status_change(id, USERS, 1)
		print(USERS[id].get("status"))
		bot.send_message(call.message.chat.id, text = "Пожалуйста, напишите как Вас зовут")
		

if __name__ == "__main__":
	bot.polling(none_stop=True)

	
