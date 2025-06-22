import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка"""

    sorted_data: list[dict] = []

    for transaction in data:
        if re.search(search, transaction["description"], flags=re.IGNORECASE):
            sorted_data.append(transaction)

    return sorted_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории"""

    sorted_data: list[dict] = []

    for category in categories:
        sorted_data.extend(process_bank_search(data, category))

    simplified_list = []

    for transaction in sorted_data:
        simplified_list.append(transaction["description"])

    counted = Counter(simplified_list)

    return dict(counted)
