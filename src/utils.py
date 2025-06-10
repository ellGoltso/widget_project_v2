import json


def get_data(path: str) -> list:
    """Принимает на вход путь до JSON-файла
    и возвращает список словарей с данными"""

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        return []

    if isinstance(data, list):
        return data
    return []
