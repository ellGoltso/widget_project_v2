import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "expected",
    [
        (
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229",
            },
            None,
        )
    ],
)
def test_filter_by_currency_usd(fixture_transactions, expected):
    usd_generator = filter_by_currency(fixture_transactions, "USD")
    usd_transactions_list = []
    for _ in range(4):
        usd_transactions_list.append(next(usd_generator))

    assert usd_transactions_list == list(expected)


@pytest.mark.parametrize(
    "expected",
    [
        (
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160",
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            },
            None,
        )
    ],
)
def test_filter_by_currency_rub(fixture_transactions, expected):
    rub_generator = filter_by_currency(fixture_transactions, "RUB")
    rub_transactions_list = []
    for _ in range(3):
        rub_transactions_list.append(next(rub_generator))

    assert rub_transactions_list == list(expected)


def test_invalid_currency(fixture_transactions):
    generator = filter_by_currency(fixture_transactions, "invalid currency")

    assert next(generator) is None


@pytest.mark.parametrize(
    "expected",
    [
        (
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Перевод организации",
            None,
        )
    ],
)
def test_transaction_descriptions(fixture_transactions, expected):
    descriptions = transaction_descriptions(fixture_transactions)

    descriptions_list = []
    for _ in range(6):
        descriptions_list.append(next(descriptions))

    assert descriptions_list == list(expected)


def test_card_number_generator():
    generator = card_number_generator(1, 3)

    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"
    assert next(generator) == "0000 0000 0000 0003"
