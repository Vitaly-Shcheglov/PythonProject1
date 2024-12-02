import pytest
from src.processing import filter_by_state, sort_by_date

@pytest.fixture
def transactions():
    """Фикстура, возвращающая список транзакций."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("NON_EXISTENT", 0)
])
def test_filter_by_state(transactions, state, expected_count):
    """Тестирование функции фильтрации по статусу."""
    filtered_transactions = filter_by_state(transactions, state)
    assert len(filtered_transactions) == expected_count

def test_sort_by_date(transactions):
    """Тестирование функции сортировки по дате."""
    sorted_transactions = sort_by_date(transactions, descending=True)
    assert sorted_transactions == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
