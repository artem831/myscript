import smtplib as root
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os
def email():
	def send_email():
		login = input('введите вашу почту:')
		password = input('введите ваш пароль:')
		url = input('URL(пример:smtp.mail.ru):')
		toaddr = input('кому:')
		topic = input('тема:')
		message = input('сообщения:')
		msg = MIMEMultipart()
		msg[ 'subject' ] = topic
		msg[ 'from' ] = login
		body = message
		msg.attach(MIMEText(body,'plain'))
		server=root.SMTP_SSL(url,465)
		server.login(login,password)
		while True:
			server.sendmail(login,toaddr,msg.as_string()) 
	send_email()
def sms():
	os.system('pkg install python')
	os.system('pkg install git')
	os.system('git clone https://github.com/FSystem88/spymer')
	if os.path.exists('/data/data/com.termux/files/home/myscript/spymer'):
		os.system('bash /data/data/com.termux/files/home/myscript/spymer/install.sh')
	else:
		print('ошибка')
def ip():
	os.system('pkg install python')
	os.system('pkg install git')
	os.system('git clone https://github.com/MichaelDim02/IPLocator')
	if os.path.exists('/data/data/com.termux/files/home/myscript/IpLocator'):
		os.system('python  /data/data/com.termux/files/home/myscript/IpLocator/iplocator')
	else:
		print('ошибка')
def phone():
	os.system('pkg install python')
	os.system('pkg install git')
	os.system('git clone https://github.com/sundowndev/PhoneInfoga')
def pars():
	url = input('URL:')
	r = requests.get(url)
	with open('body.html','w') as w:
		w.write(r.text)
def wir():
	os.system('pkg install toilet -y')
	os.system('clear')
	writed=input('надпись:')
	os.system('toilet -f mono12 '+writed)
