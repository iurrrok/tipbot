import time
import json
import telebot
bot = telebot.TeleBot('телеграм бот апи')# minter bot
from sqlite_tip import tip_save,tip_find1,tip_find,tip_edit2,tip_find_row,tip_read,tip_del,tip_edit3
#перед тем,как начать работать надо создать таблицу 
#tip_table('название файла.расширение')
#import logging
#мой айди
id_admin=**

#logger = telebot.logger
#telebot.logger.setLevel(logging.DEBUG)
#пере

@bot.message_handler(commands=['start'])
def start_message(message):
	if message.json['chat']['type']=='private':
		bot.send_message(message.chat.id, 'Бот в стадии тестирования,отправь команду /help')
		bot.reply_to(message, "We are testing bot right now, enter /help")
		tg_id=message.json['from']['id']
		hhh=tip_find_row('sqlite_tip_test.db',tg_id)
		print(hhh)
	#print(message)
	#m=[]
	#m.append(message)
		#print (message.json['chat']['type'])
#	for n,m in message.json.items():
	#print(message.json['text'],message.json['message_id'],message.json['from'],'----',message.json['from']['username'])
#	print('{0},{1}'.format(message.chat.id,message.from_user.id))
#	for i in m:
#		print (f'{i[0]}')


@bot.message_handler(commands=['help','h'])
def start_message(message):
	if message.json['chat']['type']=='private':
		bot.send_message(message.chat.id, 'Список команд: /set , /my , /balance , /tipp')





#регистрация пользователя
@bot.message_handler(commands=['set'])
def set_message(message):
	if message.json['chat']['type']=='private':
		msg=message.json['text']
		if msg[5:] == '':
			bot.send_message(message.chat.id, 'Тут ты можешь указать свой адрес минтер для вывода монет.Порядок такой: /set адрес минтер')
		elif len(msg[5:]) >= 43:
			bot.send_message(message.chat.id, 'Слишком много символов')
		else :
			mint_w=msg[5:]#кошелек
			tg_id=message.json['from']['id']
			uname=message.json['from']['username']
		#проверка ,адреса,если он уже есть
			hhh=tip_find1('sqlite_tip_test.db',tg_id,'id')
			if hhh == 'None':
				tip_save(tg_id,mint_w,uname,0,0)
				bot.send_message(message.chat.id, 'Адрес зарегестрирован,спасибо.')
			else:
				bot.send_message(message.chat.id, 'Адрес уже существует в базе')

#бот отображает кошелек
@bot.message_handler(commands=['my'])
def my_my(message):
	if message.json['chat']['type']=='private':
		tg_id=message.json['from']['id']
		hhh=tip_find1('sqlite_tip_test.db',tg_id,'id')
		if hhh == 'None':
			bot.send_message(message.chat.id, 'У вас нет адреса,зарегестрируйтесь')
		else:
			bot.send_message(message.chat.id, 'Ваш адрес '+hhh[1])
		
#бот отображает баланс
@bot.message_handler(commands=['balance'])
def my_balance(message):
	if message.json['chat']['type']=='private':
		tg_id=message.json['from']['id']
		hhh=tip_find_row('sqlite_tip_test.db',tg_id)
#	print(hhh)
		if hhh == None:
			bot.send_message(message.chat.id, 'У вас нет адреса,зарегестрируйтесь')
		else:
			bot.send_message(message.chat.id, 'Ваш  баланс '+str(hhh[4])+' BIP'+'\n'+str(hhh[5])+' кастом')

#бот будет отправлять 
@bot.message_handler(commands=['tipp'])
def my_tip(message):
	#проверка если чат не приватный
	if message.json['chat']['type']!='private':
		tg_id=message.json['from']['id']
		tg_nick=message.json['from']['username']
	#repl2id=message.json['reply_to_message']['from']['id']
		msg=message.json['text']
		hhh=tip_find_row('sqlite_tip_test.db',tg_id)
	#нужно,проверить если у пользователя есть баланс
		if int(hhh[4])<=1:
			bot.send_message(message.chat.id, 'Ваш баланс должен быть больше 1 бип')
		#если есть
		else:
			#забираем одну монету у первого
			newbal=int(hhh[4])-1
			tip_edit2('sqlite_tip_test.db','id',tg_id,'bal',newbal)
			totgid=message.json['reply_to_message']['from']['id']
			hhh1=tip_find1('sqlite_tip_test.db','id',totgid)
			mintw=''
			unname=message.json['reply_to_message']['from']['username']
			balance=0+1
			#если пользователя нет в системе
			#создаём акк в бд
			if hhh1 == None :
				tip_save(totgid,mintw,unname,balance,0)
			#если пользователь есть,то просто 
			#накидываем ему монет
			else:
				hhh2=tip_find1('sqlite_tip_test.db','id',totgid)
				fff=hhh2[3]
				finalbal=fff+1
				tip_edit2('sqlite_tip_test.db','id',totgid,'bal',finalbal)
		bot.send_message(message.chat.id, tg_nick+' Типнул 1 бип '+'@'+unname)
	#если чат не приватный пишем:
	else:
		bot.send_message(message.chat.id, 'Отправь монеты другу,для этого оветь другу этой коммандой в общем чате,по умолчанию отправляется 1 БИП')
	
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

#бот будет отправлять 
@bot.message_handler(commands=['tp'])
def my_tp(message):
	#проверка если чат не приватный
	if message.json['chat']['type']!='private':
		try:
			u2id=message.json['reply_to_message']['from']['id']
			u2nick=message.json['reply_to_message']['from']['username']
			
		except:
			bot.send_message(message.chat.id, 'Что бы отправить комуто монеты нужно оветить ему на сообщение коммандой /tp')
		numb=1
		u1id=message.json['from']['id']
		u1nick=message.json['from']['username']
		msg=message.json['text']
		u1=tip_find_row('sqlite_tip_test.db',u1id)
		u2=tip_find_row('sqlite_tip_test.db',u2id)
		if int(u1[4])<=numb:
			bot.send_message(message.chat.id, 'Что бы отправить кому то монеты,баланс должен быть больше '+str(numb))
		else:
			if u2 == None:
				bal1=int(u1[4])-numb
				bal2=0+numb
				mw=''
				tip_edit3('sqlite_tip_test.db','id',u1id,'bal',bal1)
				tip_save(u2id,mw,u2nick,bal2,0)
				bot.send_message(message.chat.id, '@'+u1nick+' отправил '+str(numb)+' BÎP @'+u2nick)
			else:
				#import ipdb; ipdb.set_trace()
				bal11=int(u1[4])-int(numb)
				#print(bal11,u1[4],numb)
				bal21=int(u2[4])+int(numb)
				#print(bal21,u2[4],numb)
				tip_edit3('sqlite_tip_test.db','id',u1id,'bal',bal11)
				#print(u1id,bal11)
				tip_edit3('sqlite_tip_test.db','id',u2id,'bal',bal21)
				#print(u2id,bal21)
				bot.send_message(message.chat.id, '@'+u1nick+' отправил '+str(numb)+' BĪP @'+u2nick)


#бот будет пополнять баланс
@bot.message_handler(commands=['rise'])
def my_rise(message):
	if message.json['chat']['type']=='private':
		tg_nick=message.json['from']['username']
		tg_id=message.json['from']['id']
		msg=message.json['text']
		print(tg_id)
		if tg_id == id_admin:
			bot.send_message(message.chat.id, 'Это меню админа,что бы пополнить чей-то баланс отправь команду:/rise ник количество')
			nickn=msg[6:].split()[0]
			print(nickn)
			amount=msg[6:].split()[1]
			if tip_find('sqlite_tip_test.db',nickn)==nickn:
				hhh=tip_find_row('sqlite_tip_test.db',nickn)
				finalbal=int(hhh[4])+int(amount)
				print(hhh[4])
				tip_edit2('sqlite_tip_test.db','nickname',nickn,'bal',finalbal)
				bot.send_message(message.chat.id, 'Поздравляю вы увеличили баланс '+nickn+' на '+amount+' BIP')
			else:
				bot.send_message(message.chat.id, 'Добавьте пользователя типнув ему немного монет или попросите его зарегестрироватся.(для этого надо что бы пользователь написал в личку боту)')
		else:
			print('Эта команда для админов')
		
	
#бот будет пополнять баланс
@bot.message_handler(commands=['deli'])
def my_rise(message):
	if message.json['chat']['type']=='private':
		tg_nick=message.json['from']['username']
		tg_id=message.json['from']['id']
		msg=message.json['text']
		print(tg_id)
		if tg_id == id_admin:
			bot.send_message(message.chat.id, 'Это меню админа,через пробел укажи никнейм,что бы удалить из бд')
			nickn=msg[6:].split()[0]
			tip_del('sqlite_tip_test.db','nickname',nickn)
			bot.send_message(message.chat.id, 'Пользователь удален')

	
#бот отобразит всю бд
@bot.message_handler(commands=['bd'])
def my_bd(message):
	if message.json['chat']['type']=='private':
		try:
			d=tip_read('sqlite_tip_test.db')
			for i in d:
				print(i)
		except:
			print('Errrrrorrrr!!!')
	
	
bot.polling()
