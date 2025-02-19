from collections import defaultdict, deque

def F_ErdosNumber(articles, ErdosNumber):
    # Создаем граф, где каждый узел это автор, а ребра между ними означают, что они работали вместе
    graph = defaultdict(list)

    for article in articles:
        authors = article.split(':')[0].split(', ')
        for i in range(0, len(authors), 2):
            author = authors[i] + ', ' + authors[i+1]
            for j in range(i + 2, len(authors), 2):
                coauthor = authors[j] + ', ' + authors[j+1]
                graph[author].append(coauthor)
                graph[coauthor].append(author)

    # BFS для вычисления чисел Эрдеша
    queue = deque()
    queue.append("Erdos, P.")
    ErdosNumber["Erdos, P."] = 0

    while queue:
        author = queue.popleft()
        for coauthor in graph[author]:
            if coauthor not in ErdosNumber:
                ErdosNumber[coauthor] = ErdosNumber[author] + 1
                queue.append(coauthor)

def printErdosNumber(name, ErdosNumber):
    if name not in ErdosNumber:
        print(f"{name} infinity")
    else:
        print(f"{name} {ErdosNumber[name]}")

def main():
    print("Введите количество сценариев (T):")
    T = int(input())  # Читаем количество сценариев
    scenario = 1

    while T > 0:
        T -= 1
        print(f"\nВведите количество статей (P) и количество имен для вывода (N) для сценария {scenario}:")
        P, N = map(int, input().split())  # Читаем P и N

        print(f"\nВведите {P} строк с описаниями статей (в формате 'Фамилия, И., Фамилия, И., Эрдеш, П.: Название статьи'):")
        articles = []
        for _ in range(P):
            article = input().strip()
            articles.append(article)

        print(f"\nВведите {N} строк с именами авторов, для которых нужно вычислить число Эрдеша (в формате 'Фамилия, И.'):")
        names = []
        for _ in range(N):
            name = input().strip()
            names.append(name)

        ErdosNumber = {}
        F_ErdosNumber(articles, ErdosNumber)

        # Выводим результаты для текущего сценария
        print(f"\nScenario {scenario}")
        for name in names:
            printErdosNumber(name, ErdosNumber)

        scenario += 1

if __name__ == "__main__":
    main()
