from functools import wraps


def print_or_write(filename: str, mode: str, message: str):
    """Печатает сообщение в конец файла или в консоль,
    в зависимости от наличия имя файла"""

    if filename:
        with open(filename, mode, encoding="utf-8") as log_file:
            log_file.write(message)
    else:
        print(message)


def log(filename: str = None, mode: str = "a"):
    """Логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                print_or_write(filename, mode, f"Start: {func.__name__} ok\n")

                result = func(*args, **kwargs)

                print_or_write(filename, "a", f"Finish: {func.__name__} ok\n")
                return result
            except Exception as e:
                print_or_write(filename, "a", f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")

        return wrapper

    return decorator
