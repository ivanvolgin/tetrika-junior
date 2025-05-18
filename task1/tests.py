import unittest
from task1.solution import strict


# === Функции для тестирования ===
@strict
def sum_two(a: int, b: int) -> int:
    return a + b

@strict
def greet(name: str, age: int):
    return f"{name} is {age}"

@strict
def do_nothing(x, y):
    return x, y


# === Юнит-тесты ===
class TestStrictDecorator(unittest.TestCase):

    def test_valid_sum(self):
        self.assertEqual(sum_two(1, 2), 3)

    def test_invalid_type_second_argument(self):
        with self.assertRaises(TypeError) as context:
            sum_two(1, 2.5)
        self.assertIn("b", str(context.exception))

    def test_invalid_type_first_argument(self):
        with self.assertRaises(TypeError) as context:
            greet(123, 30)
        self.assertIn("name", str(context.exception))

    def test_valid_greet(self):
        self.assertEqual(greet("Alice", 30), "Alice is 30")

    def test_both_wrong_types(self):
        with self.assertRaises(TypeError):
            sum_two("one", "two")

    def test_function_without_annotations(self):
        # do_nothing не имеет аннотаций, поэтому она должна работать с любыми типами
        result = do_nothing(True, "anything")
        self.assertEqual(result, (True, "anything"))


# === Запуск тестов ===
if __name__ == "__main__":
    unittest.main()

