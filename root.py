from module.module import *
from os import *
from colorama import *
root='''
  ██▄████   ▄████▄    ▄████▄   ███████
  ██▀      ██▀  ▀██  ██▀  ▀██    ██
  ██       ██    ██  ██    ██    ██
  ██       ▀██▄▄██▀  ▀██▄▄██▀    ██▄▄▄
  ▀▀         ▀▀▀▀      ▀▀▀▀       ▀▀▀▀
'''
info='''
версия:0.0.1
лецензии:нет
интернет:нужен
рут:не нужен
автор:артём
скрипт бесплатный
с открытом кодом
без вирусов
если нашли баг писать
сюда:artemrezanov56@mail.ru
'''
l='========================================='
menu='''
[1]-спам на email
[2]-смс бомбер
[3]-информация об ip
[4]-информация о телефоне
[5]-скапиравать код с сайта
[6]-крутая надпись
[7]-выход
'''
def main():
	system('clear')
	print(Fore.GREEN + l)
	print(Fore.RED + root)
	print(Fore.GREEN + l)
	print(Fore.YELLOW + info)
	print(Fore.GREEN + l)
	print(Fore.BLUE + menu)
	what = input('root@root|> ')
	if what == '1':
		email()
	elif what == '2':
		sms()
	elif what == '3':
		ip()
	elif what == '4':
		phone()
	elif what == '5':
		pars()
	elif what == '6':
		wir()
	elif what == '7':
		pass
main()
