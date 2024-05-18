import random
import string


def generate_random_word(length):

    all_characters = string.ascii_letters + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    random_word = ''.join(random.choice(all_characters) for _ in range(length))

    return random_word


def generate_keyword_based_password(keyword, length):

    all_characters = string.ascii_letters + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    total_random_chars = length - len(keyword)

    if total_random_chars < 0:
        raise ValueError("Длина ключевого слова слишком велика для заданной длины пароля.")

    random_choice = random.choice(['before', 'after', 'both'])

    if random_choice == 'before':
        random_chars = ''.join(random.choice(all_characters) for _ in range(total_random_chars))
        return keyword + random_chars

    elif random_choice == 'after':
        random_chars = ''.join(random.choice(all_characters) for _ in range(total_random_chars))
        return random_chars + keyword

    else:
        total_random_chars = length - len(keyword) * 2
        if total_random_chars < 0:
            raise ValueError("Длина ключевого слова слишком велика для удвоенной длины пароля.")
        random_prefix = ''.join(random.choice(all_characters) for _ in range(total_random_chars // 2))
        random_suffix = ''.join(random.choice(all_characters) for _ in range(total_random_chars - len(random_prefix)))
        return random_prefix + keyword + random_suffix + keyword


def generate_multiple_random_words(length, count):

    return [generate_random_word(length) for _ in range(count)]


def generate_multiple_keyword_based_passwords(keyword, length, count):

    return [generate_keyword_based_password(keyword, length) for _ in range(count)]


def get_valid_length(min_length=3):

    while True:
        try:
            length = int(input(f"Введите длину строки (минимум {min_length} символа): "))
            if length >= min_length:
                return length
            else:
                print(f"Ошибка: длина строки должна быть не менее {min_length} символов. Попробуйте снова.")

        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")


def get_valid_count():

    while True:
        try:
            count = int(input("Введите количество строк: "))
            if count > 0:
                return count
            else:
                print("Ошибка: количество строк должно быть положительным числом. Попробуйте снова.")

        except ValueError:
            print("Ошибка: введите целое число. Попробуйте снова.")

def save_passwords_to_file(passwords):
    filename = input("Введите имя файла для сохранения паролей: ")
    with open(filename + '.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Пароли сохранены в файл {filename}")

def main_menu():

    print("Выберите метод генерации паролей:")
    print("1. Стандартная генерация паролей")
    print("2. Генерация паролей с помощью ключевого слова (keyword)")

    while True:
        choice = input("Введите 1 или 2: ")

        if choice == '1':
            length = get_valid_length()
            count = get_valid_count()
            random_words = generate_multiple_random_words(length, count)

            print("\nСгенерированные пароли:")
            for word in random_words:
                print(word)

            save_choice = input("Хотите сохранить пароли в файл? (да/нет): ")
            if save_choice.lower() in ['да', 'yes', 'д', 'ye', 'y']:
                save_passwords_to_file(random_words)
            break

        elif choice == '2':
            keyword = input("Введите ключевое слово: ")
            length = get_valid_length(len(keyword))
            count = get_valid_count()
            keyword_passwords = generate_multiple_keyword_based_passwords(keyword, length, count)

            print("\nСгенерированные пароли на основе ключевого слова:")
            for password in keyword_passwords:
                print(password)
            
            save_choice = input("Хотите сохранить пароли в файл? (да/нет): ")
            if save_choice.lower() in ['да', 'yes', 'д', 'ye', 'y']:
                save_passwords_to_file(keyword_passwords)
            break

        else:
            print("Ошибка: введите 1 или 2. Попробуйте снова.")