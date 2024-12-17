from functools import wraps
from typing import Callable, Any, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Декоратор для логирования функции, её аргументов, результатов и ошибок."""

    def logging_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """Функция-декоратор для логирования."""

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Обертка для логирования вызовов функции."""
            try:
                log_message = f"Starting {func.__name__} with inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end='')

                result = func(*args, **kwargs)

                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end='')

                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}\n"
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message)
                else:
                    print(log_message, end='')
                raise

        return wrapper

    return logging_decorator
