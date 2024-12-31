import re
from typing import List, Dict
from collections import Counter

def search_transactions_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Функция ищет транзакции по описанию, используя регулярные выражения."""
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict]) -> Dict[str, int]:
    """Функция подсчитывает количество банковских операций по описанию."""
    descriptions = [transaction.get("description", "") for transaction in transactions]
    category_counts = Counter(descriptions)
    return dict(category_counts)
