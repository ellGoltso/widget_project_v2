import os

import requests
from dotenv import load_dotenv


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """Принимает на вход транзакцию и
    возвращает сумму транзакции в рублях"""

    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])

    load_dotenv()
    api_key = os.getenv("API_KEY")
    headers = {"apikey": api_key}
    url = (
        f"https://api.apilayer.com/exchangerates_data/"
        f"convert?to=RUB&from={transaction['operationAmount']['currency']['code']}&"
        f"amount={transaction['operationAmount']['amount']}"
    )

    response = (requests.request("GET", url, headers=headers)).json()

    return float(response["result"])
