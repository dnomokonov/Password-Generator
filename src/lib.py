import random
import string

def generate_random_word():

    length = 4
    # Символы = 'a - z, A - Z'  +  '0 - 9'  +  'специальные символы'
    all_characters = string.ascii_lowercase + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    random_word = ''.join(random.choice(all_characters) for _ in range(length))

    return random_word