def get_password(number): # Создаем функцию
    password = ''
    for i in range(1, number): # Перебираем элементы
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0: # Проверка на кратность
                password += str(i) + str(j)
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)