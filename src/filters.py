import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """ Принимает список словарей с данными о банковских операциях и строку поиска,
    возвращает список словарей, у которых в описании есть данная строка """

    sorted_data: list[dict] = []

    for transaction in data:
        if re.search(search, transaction["description"], flags = re.IGNORECASE):
            sorted_data.append(transaction)

    return sorted_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """ Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории """

    sorted_data: list[dict] = []

    for category in categories:
        sorted_data.extend(process_bank_search(data, category))

    simplified_list = []

    for transaction in sorted_data:
        simplified_list.append(transaction['description'])

    counted = Counter(simplified_list)

    return dict(counted)

#
#
# tr = [
#   {
#     "id": 441945886,
#     "state": "EXECUTED",
#     "date": "2019-08-26T10:50:58.294041",
#     "operationAmount": {
#       "amount": "31957.58",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Maestro 1596837868705199",
#     "to": "Счет 64686473678894779589"
#   },
#   {
#     "id": 41428829,
#     "state": "EXECUTED",
#     "date": "2019-07-03T18:35:29.512364",
#     "operationAmount": {
#       "amount": "8221.37",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "MasterCard 7158300734726758",
#     "to": "Счет 35383033474447895560"
#   },
#   {
#     "id": 939719570,
#     "state": "EXECUTED",
#     "date": "2018-06-30T02:08:58.425572",
#     "operationAmount": {
#       "amount": "9824.07",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод организации",
#     "from": "Счет 75106830613657916952",
#     "to": "Счет 11776614605963066702"
#   },
#   {
#     "id": 587085106,
#     "state": "EXECUTED",
#     "date": "2018-03-23T10:45:06.972075",
#     "operationAmount": {
#       "amount": "48223.05",
#       "currency": {
#         "name": "руб.",
#         "code": "RUB"
#       }
#     },
#     "description": "Открытие вклада",
#     "to": "Счет 41421565395219882431"
#   },
#   {
#     "id": 142264268,
#     "state": "EXECUTED",
#     "date": "2019-04-04T23:20:05.206878",
#     "operationAmount": {
#       "amount": "79114.93",
#       "currency": {
#         "name": "USD",
#         "code": "USD"
#       }
#     },
#     "description": "Перевод со счета на счет",
#     "from": "Счет 19708645243227258542",
#     "to": "Счет 75651667383060284188"
#   }]
#
#
# print(process_bank_operations(tr, ["Открытие вклада", "перевод"]))