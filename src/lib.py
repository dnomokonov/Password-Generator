import random
import string

def generate_random_word(length=8):

    all_characters = string.ascii_letters + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    random_word = ''.join(random.choice(all_characters) for _ in range(length))

    return random_word


def generate_multiple_random_words(length, count):
    return [generate_random_word(length) for _ in range(count)]