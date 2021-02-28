psw = input('Ввидите пароль: ')

try:
    result = 1 / len(psw)
    result = int(psw)
    
    print('Ваш пароль состоит только из цифр')
except ZeroDivisionError:

    print('Ва ввели пустой пароль')
except:
    print('Требования к паролю соблюдены')


