import unittest
import io
import csv
from task2.solution.infrastructure.file_writer import save_counts_to_csv

class TestFileWriter(unittest.TestCase):
    def test_csv_output_format(self):
        data = {"А": 10, "Б": 5}
        buffer = io.StringIO()
        writer = csv.writer(buffer)
        for letter in sorted(data):
            writer.writerow([letter, data[letter]])
        expected = "А,10\r\nБ,5\r\n"
        self.assertEqual(buffer.getvalue(), expected)
