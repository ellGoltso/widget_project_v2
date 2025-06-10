from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """Функция принимает на вход список словарей, представляющих транзакции;
    Возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной"""

    filter_transactions = filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)

    for i in filter_transactions:
        yield i

    while True:
        yield None


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Принимает список словарей с транзакциями и
    возвращает описание каждой операции по очереди"""

    for i in transactions:
        yield i["description"]

    while True:
        yield None


def card_number_generator(start: int, stop: int) -> Generator:
    """Принимает начальное и конечное значение;
    Генерирует номера карт в заданном диапазоне"""

    for num in range(start, stop + 1):
        card_num = str(num).zfill(16)
        yield f"{card_num[:4]} {card_num[4:8]} {card_num[8:12]} {card_num[12:]}"
