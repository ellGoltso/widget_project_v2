import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount_in_rub


@patch("requests.request")
def test_get_transaction_amount_in_rub(mock_get, fixture_transaction_usd):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 79114.93},
        "info": {"timestamp": 1749368825, "rate": 78.557285},
        "date": "2025-06-08",
        "result": 1.1111,
    }

    assert get_transaction_amount_in_rub(fixture_transaction_usd) == 1.1111

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    mock_get.assert_called_once_with(
        "GET", "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=79114.93", headers=headers
    )


def test_get_amount_without_exchange(fixture_transaction_rub):
    assert get_transaction_amount_in_rub(fixture_transaction_rub) == float(
        fixture_transaction_rub["operationAmount"]["amount"]
    )
