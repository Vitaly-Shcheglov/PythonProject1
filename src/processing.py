from typing import List


def filter_by_state(transactions: List[dict], state: str = "EXECUTED") -> List[dict]:
    """Функция, которая фильтрует список словарей по значению ключа 'state'."""
    filtered_transactions = [transaction for transaction in transactions if transaction.get("state") == state]
    return filtered_transactions


def sort_by_date(transactions: List[dict], descending: bool = True) -> List[dict]:
    """Функция, которая сортирует список словарей по дате."""
    sorted_transactions = sorted(transactions, key=lambda x: x["date"], reverse=descending)
    return sorted_transactions


transactions = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

executed_transactions = filter_by_state(transactions)
print("Транзакции с состоянием 'EXECUTED':")
print(executed_transactions)

canceled_transactions = filter_by_state(transactions, "CANCELED")
print("\nТранзакции с состоянием 'CANCELED':")
print(canceled_transactions)

sorted_transactions = sort_by_date(transactions)
print("\nОтсортированные транзакции по дате (по убыванию):")
print(sorted_transactions)
