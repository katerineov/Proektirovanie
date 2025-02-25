import sys
from itertools import combinations


def is_dominating_set(graph, subset, n):
    covered = set(subset)
    for node in subset:
        covered.update(graph[node])
    return len(covered) == n


def min_dominating_set(n, edges):
    if n == 0:
        return 0

    graph = {i: set() for i in range(1, n + 1)}
    for u, v in edges:
        if u == 0 or v == 0:
            continue
        graph[u].add(v)
        graph[v].add(u)

    for size in range(1, n + 1):
        for subset in combinations(range(1, n + 1), size):
            if is_dominating_set(graph, subset, n):
                return size
    return n


def main():
    input_data = []
    while True:
        try:
            line = input().strip()
            if line == "":
                if input_data:
                    n, m = map(int, input_data[0].split())
                    if n == 0 and m == 0:
                        break
                    edges = [tuple(map(int, row.split())) for row in input_data[1:]]
                    print(min_dominating_set(n, edges))
                    input_data = []
                continue
            input_data.append(line)
        except EOFError:
            break


if __name__ == "__main__":
    main()
