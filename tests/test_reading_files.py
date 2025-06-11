from unittest.mock import patch

from src.reading_files import csv_reader, excel_reader


@patch("csv.DictReader")
def test_csv_reader(mock_get, fixture_transaction_csv):
    mock_get.return_value = fixture_transaction_csv

    path = "data/transactions.csv"
    result = csv_reader(path)
    assert result == [
        {
            "id": 650703,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]


@patch("pandas.read_excel")
def test_excel_reader(mock_get, fixture_transaction_excel):
    mock_get.return_value = fixture_transaction_excel

    path = "data/transactions_excel.xlsx"
    result = excel_reader(path)
    assert result == [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
