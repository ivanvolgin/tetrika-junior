import unittest
from task2.solution.domen.entities import AnimalLetterCounter

class TestAnimalLetterCounter(unittest.TestCase):
    def test_single_latin_letter(self):
        counter = AnimalLetterCounter()
        counter.add("Apple")
        self.assertEqual(counter.result()["A"], 1)

    def test_single_cyrillic_letter(self):
        counter = AnimalLetterCounter()
        counter.add("Арбуз")
        self.assertEqual(counter.result()["А"], 1)

    def test_non_letter_symbol(self):
        counter = AnimalLetterCounter()
        counter.add(" 123Ёж")
        self.assertIn("?", counter.result())

    def test_multiple_entries(self):
        counter = AnimalLetterCounter()
        words = ["Яблоко", "Арбуз", "apple", "banana", "@@@", "арбуз"]
        for w in words:
            counter.add(w)
        result = counter.result()
        self.assertEqual(result["Я"], 1)
        self.assertEqual(result["А"], 2)
        self.assertEqual(result["A"], 1)
        self.assertEqual(result["B"], 1)
        self.assertEqual(result["?"], 1)
