import random
import string


def generate_random_word(length):

    all_characters = string.ascii_letters + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    random_word = ''.join(random.choice(all_characters) for _ in range(length))

    return random_word


def generate_keyword_based_password(keyword: str, length: int):

    all_characters = string.ascii_letters + string.digits + "-_~!@#$%^&*()+`'\";:<>/\\|"
    total_random_chars = length - len(keyword)

    if total_random_chars < 0:
        raise ValueError("The keyword length is too long for the specified password length.")

    if (2 * len(keyword) < length):
        random_choice = random.choice(['before', 'after', 'both'])
        
    else:
        random_choice = random.choice(['before', 'after'])

    if random_choice == 'before':
        random_chars = ''.join(random.choice(all_characters) for _ in range(total_random_chars))
        return keyword + random_chars

    elif random_choice == 'after':
        random_chars = ''.join(random.choice(all_characters) for _ in range(total_random_chars))
        return random_chars + keyword

    else:
        total_random_chars = length - len(keyword) * 2
        if total_random_chars < 0:
            raise ValueError("The keyword length is too long for double the password length.")
        random_prefix = ''.join(random.choice(all_characters) for _ in range(total_random_chars // 2))
        random_suffix = ''.join(random.choice(all_characters) for _ in range(total_random_chars - len(random_prefix)))
        return keyword + random_prefix + random_suffix + keyword


def generate_multiple_random_words(length, count):

    return [generate_random_word(length) for _ in range(count)]


def generate_multiple_keyword_based_passwords(keyword, length, count):

    return [generate_keyword_based_password(keyword, length) for _ in range(count)]


def get_valid_length(min_length=3):

    while True:
        try:
            length = int(input(f"Enter the length of the string (minimum {min_length} characters): "))
            if length >= min_length:
                return length
            else:
                print(f"Error: The length of the string must be at least {min_length} characters. Try again.")

        except ValueError:
            print("Error: Enter an integer. Try again.")


def get_valid_count():

    while True:
        try:
            count = int(input("Enter the number of lines: "))
            if count > 0:
                return count
            else:
                print("Error: The number of rows must be a positive number. Try again.")

        except ValueError:
            print("Error: Enter an integer. Try again.")

def save_passwords_to_file(passwords):
    filename = input("Enter the file name to save the passwords: ")
    with open(filename + '.txt', 'w') as file:
        for password in passwords:
            file.write(password + '\n')
    print(f"Passwords are saved to a file {filename}")

def main_menu():
    menu = (
        "Choose a password generation method\n"
        "1. Standard password generation\n"
        "2. Generating passwords using a keyword"
    )

    lines = menu.split('\n')
    max_length = max(len(line) for line in lines)
    box_width = max_length + 4

    print("┌" + "─" * (box_width - 2) + "┐")
    for line in lines:
        if line:
            print("│ " + line.ljust(max_length) + " │")
        else:
            print("│" + " " * (box_width - 2) + "│")
    print("└" + "─" * (box_width - 2) + "┘")

    while True:
        choice = input("Input: ")

        if choice == '1':
            length = get_valid_length()
            count = get_valid_count()
            random_words = generate_multiple_random_words(length, count)

            print("\nGenerated passwords:")
            for word in random_words:
                print(word)

            save_choice = input("\nDo you want to save passwords to a file? (yes/no): ")
            if save_choice.lower() in ['да', 'yes', 'д', 'ye', 'y']:
                save_passwords_to_file(random_words)
            break

        elif choice == '2':
            keyword = input("Enter the keyword: ")
            length = get_valid_length(len(keyword))
            count = get_valid_count()
            keyword_passwords = generate_multiple_keyword_based_passwords(keyword, length, count)

            print("\nGenerated passwords based on the keyword: ")
            for password in keyword_passwords:
                print(password)
            
            save_choice = input("\nDo you want to save passwords to a file? (yes/no): ")
            if save_choice.lower() in ['да', 'yes', 'д', 'ye', 'y']:
                save_passwords_to_file(keyword_passwords)
            break

        else:
            print("Error: Enter 1 or 2. Try again.")