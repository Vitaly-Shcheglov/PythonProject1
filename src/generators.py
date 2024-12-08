from typing import List, Dict, Iterator, Any

def filter_by_currency(transactions: List[Dict[str, Any]], currency_of_payments: str) -> Iterator[Dict[str, Any]]:
    """Фильтрует транзакции по валюте платежа и возвращает итератор."""
    return (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency_of_payments)



def transaction_description(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Генератор, возвращающий описание каждой транзакции по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")



def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, выдающий номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, end + 1):
        yield f"{num:016d}"[:4] + " " + f"{num:016d}"[4:8] + " " + f"{num:016d}"[8:12] + " " + f"{num:016d}"[12:16]
