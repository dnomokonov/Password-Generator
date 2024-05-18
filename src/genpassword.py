from src.lib import generate_multiple_random_words

if __name__ == "__main__":

    length = int(input("Введите длину строки: "))
    count = int(input("Введите количество строк: "))

    random_words = generate_multiple_random_words(length, count)
    for word in random_words:
        print(word)