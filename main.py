def decrypt(test_case, open_text="the quick brown fox jumps over the lazy dog"):
    open_words = open_text.split()

    for encrypted in test_case:
        encrypted_words = encrypted.split()
        if len(encrypted_words) != len(open_words):
            continue  # Пропустить, если количество слов не совпадает
        mapping = {}
        reverse_mapping = {}
        is_valid = True

        for ew, ow in zip(encrypted_words, open_words):
            if len(ew) != len(ow):
                is_valid = False
                break
            for e_char, o_char in zip(ew, ow):
                # Проверяем, если уже есть отображение для символа
                if e_char in mapping:
                    if mapping[e_char] != o_char:
                        is_valid = False
                        break
                if o_char in reverse_mapping:
                    if reverse_mapping[o_char] != e_char:
                        is_valid = False
                        break
                mapping[e_char] = o_char
                reverse_mapping[o_char] = e_char

            if not is_valid:
                break

        if is_valid:
            decrypted_text = []
            for line in test_case:
                decrypted_text.append(''.join([mapping.get(c, c) for c in line]))
            return decrypted_text

    return ["No solution"]

def solve():
    num_cases = int(input().strip())  # Чтение количества тестов
    case_data = []

    # Чтение данных для каждого теста
    for _ in range(num_cases):
        block = []
        while True:
            line = input().strip()
            if not line:
                break
            block.append(line)
        case_data.append(block)

    # Вывод решения для каждого теста
    results = []
    for case in case_data:
        result = decrypt(case)
        results.append("\n".join(result))

    print("\n\n".join(results))

if __name__ == "__main__":
    solve()
