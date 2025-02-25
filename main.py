import sys

v = ["0", "2", "5", "13"]

def add(a, b):
    s = ""
    a = a[::-1]
    b = b[::-1]
    i = 0
    k = 0
    while i < len(a) and i < len(b):
        m = int(a[i]) + int(b[i]) + k
        k = m // 10
        s += str(m % 10)
        i += 1
    while i < len(a):
        m = k + int(a[i])
        k = m // 10
        s += str(m % 10)
        i += 1
    while i < len(b):
        m = k + int(b[i])
        k = m // 10
        s += str(m % 10)
        i += 1
    if k:
        s += str(k)
    return s[::-1]

def solve():
    global v
    for i in range(4, 1001):  # 1001, так как n ≤ 1000
        s = add(v[i - 1], v[i - 1])
        s = add(v[i - 2], s)
        s = add(v[i - 3], s)
        v.append(s)

solve()

# Читаем все входные числа
input_numbers = []
while True:
    try:
        line = input().strip()
        if line == "":
            break
        input_numbers.append(int(line))
    except EOFError:
        break

# Печатаем пустую строку
print()

# Выводим ответы
for n in input_numbers:
    print(v[n])
