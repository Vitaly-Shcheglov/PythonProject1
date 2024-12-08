import pytest
from typing import List, Dict, Any, Iterator
from src.generators import filter_by_currency, transaction_description, card_number_generator

@pytest.fixture
def transactions() -> List[Dict[str, Any]]:
    """Создает фикстуру с тестовыми транзакциями."""
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации", "from": "Счет 75106830613657916952",
         "to": "Счет 11776614605963066702"},
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878",
         "operationAmount": {"amount": "79114.93", "currency": {"name": "EUR", "code": "EUR"}},
         "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
         "to": "Счет 75651667383060284188"},
    ]

@pytest.mark.parametrize("currency, expected", [
    ("USD", [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572",
              "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
              "description": "Перевод организации", "from": "Счет 75106830613657916952",
              "to": "Счет 11776614605963066702"}]),
])
def test_filter_by_currency(transactions: List[Dict[str, Any]], currency: str, expected: List[Dict[str, Any]]) -> None:
    """Тестирование функции filter_by_currency для проверки фильтрации транзакций по валюте."""
    generator = filter_by_currency(transactions, currency)

    filtered_transactions = list(generator)

    # Проверяем, что отфильтрованные транзакции соответствуют ожидаемым
    assert filtered_transactions == expected

def test_invalid_filter_by_currency() -> None:
    """Обработка ошибки функции filter_by_currency при получении пустого списка."""
    with pytest.raises(StopIteration):
        assert next(filter_by_currency([], "USD"))

def test_transaction_description(transactions: List[Dict[str, Any]]) -> None:
    """Тестирование функции transaction_description для получения описаний транзакций."""
    generator = transaction_description(transactions)
    descriptions = list(generator)
    expected_descriptions = [
        "Перевод организации",
        "Перевод со счета на счет"
    ]
    assert descriptions == expected_descriptions

def test_empty_transactions() -> None:
    """Тестирование функции transaction_description с пустым списком транзакций."""
    generator = transaction_description([])
    filtered_transactions = list(generator)
    assert filtered_transactions == []  # Ожидаем пустой список

def test_card_number_generator() -> None:
    """Тестирование функции генератора номеров карт по заданному диапазону."""
    card_number = card_number_generator(1000, 1004)
    assert next(card_number) == "0000 0000 0000 1000"
    assert next(card_number) == "0000 0000 0000 1001"
    assert next(card_number) == "0000 0000 0000 1002"
    assert next(card_number) == "0000 0000 0000 1003"
