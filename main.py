def solve():
    k = int(input().strip())  # Число тестов

    for test in range(k):
        if test > 0:
            print()  # Пустая строка между тестами

        n = int(input().strip())  # Число заказов
        orders = []

        # Чтение данных
        for i in range(1, n + 1):
            Ti, Si = map(int, input().split())
            orders.append((Ti, Si, i))  # (время, штраф, индекс)

        # Сортировка:
        # 1) По коэффициенту штрафа к времени (чем выше - тем раньше выполняем)
        # 2) Если одинаковые - сортируем по индексу заказа
        orders.sort(key=lambda x: (x[0] / x[1], x[2]))

        # Выводим порядковые номера заказов
        print(" ".join(str(order[2]) for order in orders))

if __name__ == "__main__":
    solve()
