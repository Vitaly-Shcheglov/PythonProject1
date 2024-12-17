import os
from typing import Generator

import pytest

from src.decorators import log


@log()
def add(x: int, y: int) -> int:
    """Функция складывает два числа."""
    return x + y


@log()
def divide(x: int, y: int) -> float:
    """Функция делит первое число на второе."""
    return x / y


@log(filename="test_log.txt")
def multiply(x: int, y: int) -> int:
    """Функция умножает два числа."""
    return x * y


def test_add(capsys: pytest.CaptureFixture) -> None:
    """Тестирует функцию add на правильность выполнения и вывод логов."""
    result = add(2, 3)
    captured = capsys.readouterr()
    assert result == 5
    assert "Starting add with inputs: (2, 3), {}" in captured.out
    assert "add ok" in captured.out


def test_divide(capsys: pytest.CaptureFixture) -> None:
    """Тестирует функцию divide на правильность выполнения и вывод логов."""
    result = divide(10, 2)
    captured = capsys.readouterr()
    assert result == 5
    assert "Starting divide with inputs: (10, 2), {}" in captured.out
    assert "divide ok" in captured.out


def test_divide_by_zero(capsys: pytest.CaptureFixture) -> None:
    """Тестирует функцию divide на обработку деления на ноль."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "Starting divide with inputs: (1, 0), {}" in captured.out
    assert "divide error: division by zero. Inputs: (1, 0), {}" in captured.out


def test_multiply_file_logging() -> None:
    """Тестирует функцию multiply на запись логов в файл."""
    multiply(3, 4)
    with open("test_log.txt", "r") as file:
        logs = file.readlines()

    assert "Starting multiply with inputs: (3, 4), {}\n" in logs
    assert "multiply ok\n" in logs


def tear_down() -> None:
    """Функция удаляет файл лога, если он существует."""
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")


@pytest.fixture(autouse=True)
def cleanup() -> Generator[None, None, None]:
    """Фикстура, которая очищает файл лога после выполнения тестов."""
    yield
    tear_down()
