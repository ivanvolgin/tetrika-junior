import unittest
from unittest.mock import patch, mock_open
from task2.solution.infrastructure import page_cache
from task2.solution.core.settings import CACHE_FILE
import json


class TestPageCache(unittest.TestCase):

    @patch("task2.solution.infrastructure.page_cache.os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open, read_data='["https://page1", "https://page2"]')
    def test_load_cached_links_success(self, mock_file, mock_exists):
        result = page_cache.load_cached_links()
        self.assertEqual(result, ["https://page1", "https://page2"])
        mock_file.assert_called_once_with(CACHE_FILE, "r", encoding="utf-8")

    @patch("task2.solution.infrastructure.page_cache.os.path.exists", return_value=False)
    def test_load_cached_links_file_missing(self, mock_exists):
        result = page_cache.load_cached_links()
        self.assertEqual(result, [])

    @patch("task2.solution.infrastructure.page_cache.os.makedirs")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_links_to_cache(self, mock_file, mock_makedirs):
        links = ["https://a", "https://b"]
        page_cache.save_links_to_cache(links)
        mock_file.assert_called_once_with(CACHE_FILE, "w", encoding="utf-8")
        handle = mock_file()
        handle.write.assert_called()  # проверяем, что вызов записи был
