import csv

import pandas as pd


def csv_reader(path: str) -> list:
    """Принимает путь к csv файлу
    и возвращает список словарей с данными из него"""

    data = []
    try:
        with open(path, encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        return []
    except UnicodeDecodeError:
        return []
    return data


def excel_reader(path: str) -> list[dict]:
    """Принимает путь к xlsx файлу
    и возвращает список словарей с данными из него"""

    try:
        excel_data = pd.read_excel(path)
        return excel_data.to_dict(orient="records")
    except ValueError:
        return []
    except FileNotFoundError:
        return []
