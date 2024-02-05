import unittest
from password_checker.password_checker import PasswordChecker


class TestPasswordChecker(unittest.TestCase):
    def setUp(self):
        # Налаштування тесту для оновлення об'єкта тестування перед кожним тестом
        self.password_checker = PasswordChecker()

    # Тести для коректного розпізнавання користувачів "за замовчуванням"
    def test_correct_recognition_default_user_alice(self):
        result = self.password_checker.check_password("C00peR")
        self.assertEqual(result, "Alice")

    def test_correct_recognition_default_user_carl(self):
        result = self.password_checker.check_password("ClariNet")
        self.assertEqual(result, "Carl")

    # Тести для коректного додавання нових користувачів
    def test_add_user_david(self):
        self.password_checker.add_user("David", "Pass123")
        result = self.password_checker.check_password("Pass123")
        self.assertEqual(result, "David")

    def test_add_user_emma(self):
        self.password_checker.add_user("Emma", "SecurePwd")
        result = self.password_checker.check_password("SecurePwd")
        self.assertEqual(result, "Emma")

    def test_negative_check_password_incorrect_password(self):
        # Тест для перевірки негативного варіанту - введення некоректного пароля
        incorrect_password = "111111"
        with self.assertRaises(Exception, msg="Expected Exception but no exception was raised"):
            self.password_checker.check_password(incorrect_password)

        # Також перевіряємо, чи некоректний пароль є в словнику користувачів
        self.assertIn(incorrect_password, self.password_checker.users)

    def test_negative_remove_user_bob(self):
        # Тест для перевірки негативного варіанту - видалення користувача "Bob"
        self.password_checker.remove_user("Bob")
        self.assertIn("Bob", self.password_checker.users)  # Очікується помилка, але не фактичний результат

    def test_negative_remove_user_pavlo(self):
        # Тест для перевірки негативного варіанту - видалення невідомого користувача "Pavlo"
        with self.assertRaises(KeyError):
            self.password_checker.remove_user("Pavlo")
        self.assertIn("Pavlo", self.password_checker.users)  # Очікується помилка, але не фактичний результат


if __name__ == '__main__':
    unittest.main()
