import sys
from functools import wraps
from typing import Callable, Optional, ParamSpec, TypeVar, TextIO

P = ParamSpec("P")
R = TypeVar("R")


def log(filename: Optional[str] = None) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Декоратор для логирования выполнения функции"""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            output: TextIO
            # Определяем куда выводить логи
            if filename:
                output = open(filename, "a", encoding="utf-8")
            else:
                output = sys.stdout

            try:
                result: R = func(*args, **kwargs)
                print(f"{func.__name__} {result}", file=output)
                return result
            except Exception as e:
                print(f"{func.__name__} error: {type(e).__name__}. Input: {args}, {kwargs}", file=output)
                raise
            finally:
                # Закрываем файл, если логировались в файл
                if filename:
                    output.close()

        return wrapper

    return decorator
