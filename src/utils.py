import json
import logging

utils_logger = logging.getLogger("utils")
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_data(path: str) -> list:
    """Принимает на вход путь до JSON-файла
    и возвращает список словарей с данными"""

    try:
        utils_logger.info(f"Поиск списка финансовых транзакций в файле: {path}")
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        utils_logger.error("Неверный формат файла")
        return []
    except FileNotFoundError:
        utils_logger.error("Файл не найден")
        return []

    if isinstance(data, list):
        utils_logger.info("Получен список транзакций")
        return data
    utils_logger.error("В файле содержится не список")
    return []
