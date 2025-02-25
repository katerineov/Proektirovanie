def find_smallest_one_sequence(n):
    remainder = 1 % n
    length = 1

    while remainder != 0:
        remainder = (remainder * 10 + 1) % n
        length += 1

    return length

# Считываем вводимые пользователем числа
input_numbers = []
print("Введите числа (пустая строка для завершения):")
while True:
    line = input().strip()
    if not line:
        break
    input_numbers.append(int(line))

# Пропускаем строку перед выводом результатов
print()

# Вычисляем и выводим результаты
for n in input_numbers:
    print(find_smallest_one_sequence(n))
