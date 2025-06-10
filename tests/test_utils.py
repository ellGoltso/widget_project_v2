from unittest.mock import patch

from src.utils import get_data


@patch("json.load")
def test_get_data(mock_get, fixture_transactions):
    mock_get.return_value = fixture_transactions

    path = "data/operations.json"
    result = get_data(path)
    assert result == fixture_transactions


@patch("json.load")
def test_get_data_with_not_a_list(mock_get):
    mock_get.return_value = {}

    path = "data/operations.json"
    result = get_data(path)
    assert result == []


def test_get_data_with_incorrect_path():
    path = "data/incorrect.json"
    result = get_data(path)
    assert result == []
