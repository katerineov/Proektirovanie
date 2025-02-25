def is_one_step_away(word1, word2):
    # Проверяем, могут ли два слова отличаться только одной буквой (или одной добавленной/удаленной буквой)
    if len(word1) == len(word2):
        # Проверка на изменение одной буквы
        diff = sum(1 for a, b in zip(word1, word2) if a != b)
        return diff == 1
    elif len(word1) + 1 == len(word2):
        # Проверка на добавление одной буквы в word1, чтобы получить word2
        for i in range(len(word2)):
            if word1 == word2[:i] + word2[i + 1:]:
                return True
        return False
    elif len(word1) == len(word2) + 1:
        # Проверка на удаление одной буквы из word1, чтобы получить word2
        for i in range(len(word1)):
            if word2 == word1[:i] + word1[i + 1:]:
                return True
        return False
    return False


def largest_edit_ladder(words):
    n = len(words)
    dp = [1] * n  # dp[i] будет хранить длину наибольшей лесенки, заканчивающейся на слове words[i]

    for i in range(n):
        for j in range(i):
            if is_one_step_away(words[j], words[i]):
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def main():
    input_data = []
    while True:
        try:
            line = input().strip()
            if line == "":
                if input_data:
                    print(largest_edit_ladder(input_data))
                    input_data = []
                continue
            input_data.append(line)
        except EOFError:
            break


if __name__ == "__main__":
    main()
