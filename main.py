def solve():
    while True:
        M, N = map(int, input().split())
        if M == 0 and N == 0:
            break

        # Входные данные
        team_sizes = list(map(int, input().split()))
        table_sizes = list(map(int, input().split()))

        # Места для размещения участников
        tables = [[] for _ in range(N)]  # Массив для таблиц, хранит список номеров участников
        table_capacity = table_sizes[:]  # Копия вместимости столов

        # Распределение
        result = [[] for _ in range(M)]  # Массив для хранения результата, т.е. какой стол для какой команды

        participants = []
        # Создаем список участников, индексируем их по команде
        for i in range(M):
            participants.extend([(i, j) for j in range(team_sizes[i])])

        # Сортируем столы по количеству мест (по убыванию), для удобства распределения
        table_indices = sorted(range(N), key=lambda x: table_sizes[x], reverse=True)

        # Распределяем участников
        possible = True
        for team_id, member_id in participants:
            placed = False
            for table_id in table_indices:
                # Если за этим столом еще есть место и он не занят участниками этой команды
                if table_capacity[table_id] > 0:
                    # Проверяем, что на этом столе еще нет участников этой команды
                    if team_id not in [t[0] for t in tables[table_id]]:
                        tables[table_id].append((team_id, member_id))
                        result[team_id].append(table_id + 1)  # Столы нумеруются с 1
                        table_capacity[table_id] -= 1
                        placed = True
                        break
            if not placed:
                possible = False
                break

        # Выводим результат
        if possible:
            print()  # Пустая строка перед результатом
            print(1)
            for res in result:
                print(" ".join(map(str, sorted(res))))  # Сортируем номера столов в каждой строке
        else:
            print(0)

# Запускаем решение
solve()
