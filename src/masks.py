from typing import List


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты по формату XXXX XX** **** XXXX."""
    if len(card_number) != 16 or not card_number.isdigit():
        print("Ошибка: номер карты должен содержать 16 цифр.")
        return ""

    masked_number = card_number[:4] + " " + card_number[4:6] + " **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета по формату **XXXX."""
    if len(account_number) < 20 or not account_number.isdigit():
        print("Ошибка: номер счета должен содержать как минимум 20 цифр.")
        return ""

    masked_account = "**" + account_number[-4:]
    return masked_account


if __name__ == "__main__":
    card_number = input("Введите номер карты: ")
    account_number = input("Введите номер счета: ")

    masked_card = get_mask_card_number(card_number)
    masked_account = get_mask_account(account_number)

    if masked_card:
        print(masked_card)
    if masked_account:
        print(masked_account)
# изменения