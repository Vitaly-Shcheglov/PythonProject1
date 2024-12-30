import pandas as pd
from typing import List, Dict

def read_transactions_from_csv(file_path: str) -> List[Dict[str, str]]:
    """Функция считывает финансовые операции из CSV-файла и возвращает список словарей."""
    try:
        df = pd.read_csv(file_path)
        transactions = df.to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        print("Ошибка! Файл не найден.")
        return []
    except pd.errors.EmptyDataError:
        print("Ошибка! Файл пуст.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении CSV: {e}")
        return []

def read_transactions_from_excel(file_path: str) -> List[Dict[str, str]]:
    """Функция считывает финансовые операции из Excel-файла и возвращает список словарей."""
    try:
        df = pd.read_excel(file_path)
        transactions = df.to_dict(orient='records')
        return transactions
    except FileNotFoundError:
        print("Ошибка! Файл не найден.")
        return []
    except ValueError:
        print("Ошибка! Неверный формат файла Excel.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении Excel: {e}")
        return []
