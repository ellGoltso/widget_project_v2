import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(fixture_data, fixture_executed, fixture_canceled):

    assert filter_by_state(fixture_data) == fixture_executed
    assert filter_by_state(fixture_data, "CANCELED") == fixture_canceled


@pytest.mark.parametrize("state, expected", [("canceled", []), ("incorrect_state", [])])
def test_filter_by_state_with_different_states(fixture_data, state, expected):
    assert filter_by_state(fixture_data, state) == expected


def test_sort_by_date(fixture_data, fixture_reverse_sort, fixture_sort):
    assert sort_by_date(fixture_data) == fixture_reverse_sort
    assert sort_by_date(fixture_data, False) == fixture_sort
