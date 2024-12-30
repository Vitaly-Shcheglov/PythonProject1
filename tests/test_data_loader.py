import unittest
from unittest.mock import MagicMock, patch

import pandas as pd

from src.data_loader import read_transactions_from_csv, read_transactions_from_excel


class TestTransactionReading(unittest.TestCase):

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_success(self, mock_read_csv):
        """Тестирование считывания транзакций из CSV"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv("dummy_path.csv")
        expected = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]

        self.assertEqual(result, expected)
        mock_read_csv.assert_called_once_with("dummy_path.csv")

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_file_not_found(self, mock_read_csv):
        """Тестирование на случай, когда файл не найден"""
        mock_read_csv.side_effect = FileNotFoundError
        result = read_transactions_from_csv("dummy_path.csv")
        self.assertEqual(result, [])

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_invalid_format(self, mock_read_csv):
        """Тестирование на некорректный формат CSV"""
        mock_read_csv.side_effect = pd.errors.ParserError
        result = read_transactions_from_csv("dummy_path_invalid.csv")
        self.assertEqual(result, [])

    @patch("pandas.read_csv")
    def test_read_transactions_from_csv_missing_columns(self, mock_read_csv):
        """Тестирование на CSV-файл с недостающими столбцами"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"amount": "100"}]
        mock_read_csv.return_value = mock_df

        result = read_transactions_from_csv("dummy_path_missing_columns.csv")
        self.assertEqual(result, [{"amount": "100"}])

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_success(self, mock_read_excel):
        """Тестирование считывания транзакций из Excel"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("dummy_path.xlsx")
        expected = [{"id": "1", "amount": "100"}, {"id": "2", "amount": "200"}]

        self.assertEqual(result, expected)
        mock_read_excel.assert_called_once_with("dummy_path.xlsx")

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_file_not_found(self, mock_read_excel):
        """Тестирование на случай, когда файл не найден"""
        mock_read_excel.side_effect = FileNotFoundError
        result = read_transactions_from_excel("dummy_path.xlsx")
        self.assertEqual(result, [])

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_invalid_format(self, mock_read_excel):
        """Тестирование на некорректный формат Excel"""
        mock_read_excel.side_effect = ValueError
        result = read_transactions_from_excel("dummy_path.xlsx")
        self.assertEqual(result, [])

    @patch("pandas.read_excel")
    def test_read_transactions_from_excel_missing_columns(self, mock_read_excel):
        """Тестирование на Excel-файл с недостающими столбцами"""
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"amount": "100"}]
        mock_read_excel.return_value = mock_df

        result = read_transactions_from_excel("dummy_path_missing_columns.xlsx")
        self.assertEqual(result, [{"amount": "100"}])


if __name__ == "__main__":
    unittest.main()
