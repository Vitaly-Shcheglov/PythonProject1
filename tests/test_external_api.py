import unittest
from unittest.mock import patch

from src.external_api import convert_amount, get_transaction_amount


class TestCurrencyConversion(unittest.TestCase):

    def test_get_transaction_amount_rub(self):
        """Тестирование функции получения суммы операции в рублях"""
        transaction = {"operationAmount": {"amount": "1000", "currency": {"code": "RUB"}}}
        self.assertEqual(get_transaction_amount(transaction), 1000.0)

    @patch("src.external_api.convert_amount")
    def test_get_transaction_amount_usd(self, mock_convert):
        """Тестирование функции получения суммы операции из USD в RUB"""
        transaction = {"operationAmount": {"amount": "5", "currency": {"code": "USD"}}}
        mock_convert.return_value = 479.01
        self.assertEqual(get_transaction_amount(transaction), 479.01)

    def test_get_invalid_transaction_data(self):
        """Тестирование функции на некорректные данные"""
        self.assertEqual(get_transaction_amount({}), 0.0)
        self.assertEqual(get_transaction_amount([]), 0.0)
        self.assertEqual(get_transaction_amount("invalid"), 0.0)

    @patch("requests.get")
    def test_convert_amount_usd(self, mock_get):
        """Тестирование функции конвертации из USD в RUB"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"result": 479.01}

        result = convert_amount("USD", "5")
        self.assertEqual(result, 479.01)

    @patch("requests.get")
    def test_convert_amount_invalid_response(self, mock_get):
        """Тестирование функции конвертации с ошибкой API"""
        mock_get.return_value.status_code = 404
        mock_get.return_value.reason = "The requested resource doesn't exist."

        result = convert_amount("USD", "5")
        self.assertEqual(result, 0.0)


if __name__ == "__main__":
    unittest.main()
