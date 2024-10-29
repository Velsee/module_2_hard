def get_password(number):  # Создаем функцию
    password = ''
    # i начинается с 1, j с i+1 (чтобы не проверять пару (i, j), если j <= i)
    for i in range(1, number):
        for j in range(i + 1, number):  # Оптимизация: начинаем с i+1
            if number % (i + j) == 0:  # Проверка на кратность
                password += str(i) + str(j)  # Формируем пароль
    return password

n = int(input('Введите целое число от 3 до 20: '))

result = get_password(n)
print('Пароль:', result)
