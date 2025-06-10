from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_account: str) -> str:
    """Принимает строку, содержащую тип и номер карты или счета и возвращает строку с замаскированным номером"""

    if not isinstance(card_or_account, str):
        raise AttributeError("Некорректный тип данных")

    card_or_account_type: str = ""
    number: str = ""
    full_name_card_account: str = ""

    for ch in card_or_account:
        if ch.isalpha() or ch == " ":
            card_or_account_type += ch
        else:
            number += ch

    if len(number) == 16:
        full_name_card_account += card_or_account_type + get_mask_card_number(int(number))
    elif len(number) == 20:
        full_name_card_account += card_or_account_type + get_mask_account(int(number))
    else:
        return ""

    return full_name_card_account


def get_date(date_time: str) -> str:
    """Получает строку даты и времени и возвращает строку с датой в формате: ДД.ММ.ГГГГ"""

    if len(date_time) < 10:
        raise ValueError("Некорректный формат даты")

    date_ = ""

    for letter in date_time:
        if letter == "T":
            break
        date_ += letter

    for letter in date_:
        if not letter.isdigit() and letter != "-":
            raise ValueError("Некорректный формат даты")

    year: str = date_[:4]
    month: str = date_[5:7]
    day: str = date_[8:]

    return f"{day}.{month}.{year}"
