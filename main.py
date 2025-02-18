def print_lcd(num, size):
    lcd = [
        [" _ ", "| |", "   ", "| |", " _ "],
        ["   ", "  |", "   ", "  |", "   "],
        [" _ ", "  |", " _ ", "|  ", " _ "],
        [" _ ", "  |", " _ ", "  |", " _ "],
        ["   ", "| |", " _ ", "  |", "   "],
        [" _ ", "|  ", " _ ", "  |", " _ "],
        [" _ ", "|  ", " _ ", "| |", " _ "],
        [" _ ", "  |", "   ", "  |", "   "],
        [" _ ", "| |", " _ ", "| |", " _ "],
        [" _ ", "| |", " _ ", "  |", " _ "]
    ]
    num_str = str(num)
    # вывод строк для каждой цифры
    for i in range(2 + size * 2 + 3):
        line = ""
        for digit in num_str:
            index = int(digit)
            if i == 0:
                line += lcd[index][0][0] + lcd[index][0][1]*size + lcd[index][0][2] + " "
            elif 0 < i < 1 + size:
                line += lcd[index][1][0] + lcd[index][1][1]*size + lcd[index][1][2] + " "
            elif i == 1 + size:
                line += lcd[index][2][0] + lcd[index][2][1]*size + lcd[index][2][2] + " "
            elif 1 + size < i < 2 + size * 2:
                line += lcd[index][3][0] + lcd[index][3][1]*size + lcd[index][3][2] + " "
            elif i == 2 + size * 2:
                line += lcd[index][4][0] + lcd[index][4][1]*size + lcd[index][4][2] + " "
            else:
                line += " " * (size + 2) + " "
        print(line)

if __name__ == "__main__":
    while True:
        # Запросим у пользователя ввод данных
        user_input = input("Введите размер и число через пробел (2 12345): ")

        # Преобразуем введенные данные в два числа
        size, num = map(int, user_input.split())

        # Если введены нули, завершаем программу
        if size == 0 and num == 0:
            break

        # Печатаем LCD-вывод
        print_lcd(num, size)
        print()

