from typing import Tuple

from src.filters import process_bank_search
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reading_files import csv_reader, excel_reader
from src.utils import get_data
from src.widget import get_date, mask_account_card


def select_file_type() -> Tuple[list[dict], str]:
    while True:
        file_choice: str = input(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )

        data_list: list[dict] = []
        if file_choice == "1":
            print("Для обработки выбран JSON-файл.")
            data_list = get_data("data/operations.json")
            return data_list, "json"
        elif file_choice == "2":
            print("Для обработки выбран CSV-файл.")
            data_list = csv_reader("data/transactions.csv")
            return data_list, "csv_xlsx"
        elif file_choice == "3":
            print("Для обработки выбран XLSX-файл.")
            data_list = excel_reader("data/transactions_excel.xlsx")
            return data_list, "csv_xlsx"
        else:
            print(f'Пункт меню: "{file_choice}" недоступен')
            continue


def select_filter_status(data_list: list[dict]) -> list[dict]:
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        state_choice = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n")

        if state_choice.lower() == "executed":
            print('Операции отфильтрованы по статусу "EXECUTED"')
            data_list = filter_by_state(data_list)
            return data_list
        elif state_choice.lower() == "canceled":
            print('Операции отфильтрованы по статусу "CANCELED"')
            data_list = filter_by_state(data_list, "CANCELED")
            return data_list
        elif state_choice.lower() == "pending":
            print('Операции отфильтрованы по статусу "PENDING"')
            data_list = filter_by_state(data_list, "PENDING")
            return data_list
        else:
            print(f'Статус операции "{state_choice}" недоступен.')
            continue


def select_sort_by_date(data_list: list[dict]) -> list[dict]:
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        date_sort: str = input()
        if date_sort.lower() == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                sorting_direction: str = input()
                if sorting_direction.lower() == "по возрастанию":
                    print("Операции отфильтрованы по возрастанию")
                    data_list = sort_by_date(data_list, False)
                    return data_list
                elif sorting_direction.lower() == "по убыванию":
                    print("Операции отфильтрованы по убыванию")
                    data_list = sort_by_date(data_list)
                    return data_list
                else:
                    print(f"Направление сортировки: {sorting_direction} недоступно")
                    continue

        elif date_sort.lower() == "нет":
            return data_list
        else:
            print(f"Неизвестный ответ: {date_sort}")
            continue


def sort_by_rub_with_json(data_list: list[dict]) -> list[dict]:
    rub_generator = filter_by_currency(data_list, "RUB")
    rub_data: list[dict] = []

    for _ in range(len(data_list)):
        transaction: dict | None = next(rub_generator)
        if transaction is not None:
            rub_data.append(transaction)

    return rub_data


def sort_by_rub_with_csv_excel(data_list: list[dict]) -> list[dict]:
    sorted_data_list: list[dict] = []
    for transaction in data_list:
        if transaction["currency_code"] == "RUB":
            sorted_data_list.append(transaction)
    return sorted_data_list


def select_sort_by_rub(data_list: list[dict], file_type: str) -> list[dict]:
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        sorting_by_rub: str = input()
        if sorting_by_rub.lower() == "да":
            if file_type == "json":
                data_list = sort_by_rub_with_json(data_list)
            else:
                data_list = sort_by_rub_with_csv_excel(data_list)

            print("Операции отфильтрованы по валюте РУБ")
            return data_list
        elif sorting_by_rub.lower() == "нет":
            return data_list
        else:
            print(f"Неизвестный ответ: {sorting_by_rub}")
            continue


def select_sort_by_description(data_list: list[dict]) -> list[dict]:
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        sorting_by_description: str = input()
        if sorting_by_description.lower() == "да":
            print("Введите слово, по которому нужно выполнить фильтрацию.")
            filter_word: str = input()
            data_list = process_bank_search(data_list, filter_word)
            print(f"Операции отфильтрованы по слову: {filter_word}")
            return data_list
        elif sorting_by_description.lower() == "нет":
            return data_list
        else:
            print(f"Неизвестный ответ: {sorting_by_description}")
            continue


def main() -> Tuple[list[dict], str]:
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    operations, file_type = select_file_type()
    operations = select_filter_status(operations)
    operations = select_sort_by_date(operations)
    operations = select_sort_by_rub(operations, file_type)
    operations = select_sort_by_description(operations)

    return operations, file_type


data_list, file_type = main()

if not data_list:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
else:
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(data_list)}\n")

    if file_type == "json":
        for operation in data_list:
            if "from" in operation.keys():
                print(
                    f"{get_date(operation['date'])} {operation['description']}\n"
                    f"{mask_account_card(operation['from'])} -> {mask_account_card(operation['to'])}\n"
                    f"Сумма: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
                )
            else:
                print(
                    f"{get_date(operation['date'])} {operation['description']}\n"
                    f"{mask_account_card(operation['to'])}\n"
                    f"Сумма: {operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n"
                )
    else:
        for operation in data_list:
            if operation["from"]:
                print(
                    f"{get_date(operation['date'])} {operation['description']}\n"
                    f"{mask_account_card(operation['from'])} -> {mask_account_card(operation['to'])}\n"
                    f"Сумма: {operation['amount']} {operation['currency_name']}\n"
                )
            else:
                print(
                    f"{get_date(operation['date'])} {operation['description']}\n"
                    f"{mask_account_card(operation['to'])}\n"
                    f"Сумма: {operation['amount']} {operation['currency_name']}\n"
                )
