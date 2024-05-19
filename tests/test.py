import unittest
import os
from src import lib as Lib

class TestGenPassword(unittest.TestCase):
    def test_generate_password_count(self):
        """
        Тестирование количества паролей
        """
        count = 100
        length = 8
        passwords = Lib.generate_multiple_random_words(length, count)
        self.assertEqual(len(passwords), count)

    def test_generate_password_length(self):
        """
        Тестирование длины пароля
        """
        count = 100
        length = 8
        passwords = Lib.generate_multiple_random_words(length, count)
        for password in passwords:
            self.assertEqual(len(password), length)

    def test_generate_password_with_keywords(self):
        """
        Тестирование наличия ключевого слова в пароле 
        """
        count = 100
        length = 10
        keyword = "meow"
        passwords = Lib.generate_multiple_keyword_based_passwords(keyword, length, count)
        for password in passwords:
            self.assertIn(keyword, password)

    def test_keyword_exception(self):
        """
        Тестирование ошибки при передаче ключевого слова длины, большей length 
        """
        length = 5
        keyword = "meow meow meow"
        with self.assertRaises(ValueError):
            Lib.generate_keyword_based_password(keyword, length)
    
    def test_save_to_file(self):
        """
        Тестирование сохранения паролей в файл
        """
        count = 100
        length = 10
        keyword = "meow"
        passwords = Lib.generate_multiple_keyword_based_passwords(keyword, length, count)
        name = "tests"
        Lib.save_passwords_to_file(passwords, name)
        self.assertTrue(os.path.exists("tests.txt"))
        with open("tests.txt", "r") as file:
            self.assertEqual(len(file.readlines()), count)
            for line in file.readlines():
                self.assertIn(keyword, line)
                self.assertEqual(len(line), length)
            file.close()
        os.remove("tests.txt")

if __name__ == '__main__':
    unittest.main()