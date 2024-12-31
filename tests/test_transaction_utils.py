import pytest
import json
from src.transaction_utils import search_transactions_by_description, count_transactions_by_category


def load_transactions_from_json():
    with open("data/operations.json", "r", encoding="utf-8") as f:
        return json.load(f)


transactions = load_transactions_from_json()

def test_search_transactions_by_description():
    result = search_transactions_by_description(transactions, "Перевод организации")
    assert len(result) == 40, "Должно быть 40 транзакций с 'Перевод организации'"

    result = search_transactions_by_description(transactions, "Открытие вклада")
    assert len(result) == 10, "Должно быть 10 транзакций с 'Открытие вклада'"

    result = search_transactions_by_description(transactions, "такой транзакции нет")
    assert len(result) == 0, "Не должно быть транзакций"

def test_count_transactions_by_category():
    result = count_transactions_by_category(transactions)
    assert result["Перевод организации"] == 40, "Должно быть 40 транзакций с 'Перевод организации'"
    assert result["Открытие вклада"] == 10, "Должно быть 10 транзакций с 'Открытие вклада'"
    assert result["Перевод со счета на счет"] == 15, "Должно быть 15 транзакции с 'Перевод со счета на счет'"
    assert result["Перевод с карты на карту"] == 19, "Должно быть 19 транзакции с 'Перевод с карты на карту'"

    result = count_transactions_by_category([])
    assert result == {}, "Словарь должен быть пустым для пустого списка транзакций"

if __name__ == "__main__":
    pytest.main()
