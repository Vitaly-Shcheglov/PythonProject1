import json
import os
import unittest
from unittest.mock import mock_open, patch

from src.utils import \
    get_operations_data


class TestGetOperationsData(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data=json.dumps(
            [
                {"id": 1, "amount": 100, "currency": "RUB"},
                {"id": 2, "amount": 200, "currency": "USD"},
            ]
        ),
    )
    def test_get_operations_data_success(self, mock_file):
        """Тест успешного получения данных операций из JSON-файла"""
        test_path = (
            r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\test_file.json"
        )
        result = get_operations_data(test_path)

        expected_result = [
            {"id": 1, "amount": 100, "currency": "RUB"},
            {"id": 2, "amount": 200, "currency": "USD"},
        ]

        self.assertEqual(result, expected_result)
        mock_file.assert_called_once_with(test_path, "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open)
    def test_get_operations_data_empty_file(self, mock_file):
        """Тест получения пустого списка операций из пустого JSON-файла"""
        mock_file.return_value.__enter__.return_value.read.return_value = "[]"

        test_path = (
            r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\empty_file.json"
        )
        result = get_operations_data(test_path)

        self.assertEqual(result, [])
        mock_file.assert_called_once_with(test_path, "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open)
    def test_get_operations_data_invalid_json(self, mock_file):
        """Тест на обработку некорректного JSON"""
        mock_file.return_value.__enter__.return_value.read.return_value = (
            "{ invalid json }"
        )

        test_path = (
            r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\invalid.json"
        )
        result = get_operations_data(test_path)

        self.assertEqual(result, [])
        mock_file.assert_called_once_with(test_path, "r", encoding="utf-8")

    @patch("builtins.open", new_callable=mock_open)
    def test_get_operations_data_file_not_found(self, mock_file):
        """Тест на случай, когда файл не найден"""
        mock_file.side_effect = FileNotFoundError

        test_path = (
            r"C:\Users\PC\PycharmProjects\Homework_Bank_widget\data\nonexistent.json"
        )
        result = get_operations_data(test_path)

        self.assertEqual(result, [])
        mock_file.assert_called_once_with(test_path, "r", encoding="utf-8")


if __name__ == "__main__":
    unittest.main()
