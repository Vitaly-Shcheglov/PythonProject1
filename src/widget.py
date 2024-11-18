from src.masks import get_mask_card_number, get_mask_account
import os

def mask_account_card(info: str) -> str:
    """Функция, которая маскирует номер карты или счета."""
    parts = info.split()
    if len(parts) < 2:
        return "Ошибка: некорректный ввод."

    identifier = ' '.join(parts[:-1])
    number = parts[-1]

    if identifier.lower().startswith("счет"):
        masked_info = get_mask_account(number)
        return f"{identifier} **{masked_info}"
    else:
        masked_info = get_mask_card_number(number)
        return f"{identifier} {masked_info}"

def get_date(date_str: str) -> str:
    """Функция, которая преобразует строку даты в нужный формат."""
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"

user_input = input("Введите тип и номер карты (или счет): ")
masked_output = mask_account_card(user_input)
print(masked_output)


print(get_date("2024-03-11T02:26:18.671407"))