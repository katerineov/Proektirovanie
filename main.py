def min_travel_path(m, n, matrix):
    # Динамическое программирование для вычисления минимального пути
    dp = [[float('inf')] * n for _ in range(m)]
    parent = [[-1] * n for _ in range(m)]

    # Инициализация первого столбца
    for i in range(m):
        dp[i][0] = matrix[i][0]

    # Заполнение таблицы DP
    for j in range(1, n):
        for i in range(m):
            # Возможные переходы: вверх, влево и вниз
            for di in [-1, 0, 1]:
                prev_row = (i + di) % m  # с учётом цикличности строк
                if dp[prev_row][j - 1] + matrix[i][j] < dp[i][j]:
                    dp[i][j] = dp[prev_row][j - 1] + matrix[i][j]
                    parent[i][j] = prev_row
                elif dp[prev_row][j - 1] + matrix[i][j] == dp[i][j]:
                    # Если стоимость одинаковая, выбираем лексикографически меньший путь
                    if prev_row < parent[i][j]:
                        parent[i][j] = prev_row

    # Поиск минимального пути
    min_cost = float('inf')
    end_row = -1
    for i in range(m):
        if dp[i][n - 1] < min_cost:
            min_cost = dp[i][n - 1]
            end_row = i

    # Восстановление пути
    path = [0] * n
    current_row = end_row
    for j in range(n - 1, -1, -1):
        path[j] = current_row + 1  # Индексы строк с 1
        current_row = parent[current_row][j]

    return path, min_cost


# Читаем все входные данные
input_numbers = []
while True:
    try:
        line = input().strip()
        if line == "":
            break
        input_numbers.append(line)
    except EOFError:
        break

# Обрабатываем все матрицы из данных
i = 0
while i < len(input_numbers):
    # Считываем размеры матрицы
    m, n = map(int, input_numbers[i].split())
    matrix = []

    # Считываем строки матрицы
    for j in range(m):
        if i + 1 + j < len(input_numbers):  # Убедитесь, что строки матрицы не выходят за пределы
            matrix.append(list(map(int, input_numbers[i + 1 + j].split())))

    # Решаем задачу для текущей матрицы
    path, cost = min_travel_path(m, n, matrix)

    # Выводим результат
    print(' '.join(map(str, path)))
    print(cost)

    # Переходим к следующей матрице
    i += m + 1
