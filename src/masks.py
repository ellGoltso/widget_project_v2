def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    card_number_list: list = []
    masked_card_number: str = ""

    while card_number > 0:
        card_number_list.append(card_number % 10)
        card_number //= 10

    card_number_list.reverse()

    if len(card_number_list) != 16:
        return ""

    for i, v in enumerate(card_number_list):
        if 6 <= i <= 11:
            masked_card_number += "*"
        else:
            masked_card_number += str(v)

    return " ".join(masked_card_number[i * 4 : (i + 1) * 4] for i in range(4))


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    if len(str(account_number)) != 20:
        return ""
    return "**" + str(account_number)[-4:]
