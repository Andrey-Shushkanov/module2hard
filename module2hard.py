n = int(input('Введите число от 3 до 20: '))
if n < 3 or n > 20:
    print('Некорректное число')
else:
    result = ''
    for i in range(1, n):
        for j in range(i+1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    print(result)