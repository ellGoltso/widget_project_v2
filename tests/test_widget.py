import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 7365", ""),
        ("Maestro 15968378687051996546546", ""),
    ],
)
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected


def test_incorrect_input_data_for_mask_account_card():
    with pytest.raises(AttributeError) as exc_info:
        mask_account_card(1313)

    assert str(exc_info.value) == "Некорректный тип данных"


@pytest.mark.parametrize(
    "date_time, expected", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("2024-03-1T02:26:18.671407", "1.03.2024")]
)
def test_get_date(date_time, expected):
    assert get_date(date_time) == expected


@pytest.mark.parametrize("incorrect_format_date", ["year", "*&", "2024-o3-ll", ""])
def test_incorrect_date_format(incorrect_format_date):
    with pytest.raises(ValueError) as exc_info:
        get_date(incorrect_format_date)

    assert str(exc_info.value) == "Некорректный формат даты"
