import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card, masked_card",
    [(1234567891234567, "1234 56** **** 4567"), (1234567891234567123456, ""), (1234567891234, ""), (0, "")],
)
def test_get_mask_card_number(card, masked_card):
    assert get_mask_card_number(card) == masked_card


@pytest.mark.parametrize(
    "account, masked_account", [(73654108430135874305, "**4305"), (0, ""), (7365410843013587430564554, ""), (1234, "")]
)
def test_get_mask_account(account, masked_account):
    assert get_mask_account(account) == masked_account
