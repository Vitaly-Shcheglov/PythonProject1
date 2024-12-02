import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_numbers():
    """Фикстура, возвращающая список номеров карт для тестирования."""
    return [
        "7000792289606361",
        "1234567812345678",
        "7000 792289606361",
        "70007922896063",
        "abcdefg12345678",
        "",
    ]

@pytest.fixture
def account_numbers():
    """Фикстура, возвращающая список номеров счетов для тестирования."""
    return [
        "73654108430135874305",
        "12345678901234567890",
        "1234",
        "1234567890",
        "abcd123456789012345",
        "",
    ]

@pytest.mark.parametrize("card_number, expected", [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234567812345678", "1234 56** **** 5678"),
])
def test_get_mask_card_number_valid(card_number, expected):
    """Тестирование правильности маскирования номера карты."""
    assert get_mask_card_number(card_number) == expected

def test_get_mask_card_number_invalid(card_numbers):
    """Тестирование обработки некорректных номеров карт."""
    for number in card_numbers[2:]:
        assert get_mask_card_number(number) == ""

@pytest.mark.parametrize("account_number, expected", [
    ("73654108430135874305", "**4305"),
    ("12345678901234567890", "**7890"),
])
def test_get_mask_account_valid(account_number, expected):
    """Тестирование правильности маскирования номера счета."""
    assert get_mask_account(account_number) == expected

def test_get_mask_account_invalid(account_numbers):
    """Тестирование обработки некорректных номеров счетов."""
    for number in account_numbers[2:]:
        assert get_mask_account(number) == ""
