import logging

masks_logger = logging.getLogger("masks")
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""

    card_number_list: list = []
    masked_card_number: str = ""

    try:
        while card_number > 0:
            card_number_list.append(card_number % 10)
            card_number //= 10
    except TypeError:
        masks_logger.error("Неверный формат номера карты")
        return ""

    card_number_list.reverse()

    if len(card_number_list) != 16:
        masks_logger.error("Неверное число символов в номере карты")
        return ""

    masks_logger.info("Выполняется маскировка номера карты")
    for i, v in enumerate(card_number_list):
        if 6 <= i <= 11:
            masked_card_number += "*"
        else:
            masked_card_number += str(v)

    return " ".join(masked_card_number[i * 4 : (i + 1) * 4] for i in range(4))


def get_mask_account(account_number: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску."""

    if not isinstance(account_number, int):
        masks_logger.error("Неверный формат номера счета")
        return ""

    if len(str(account_number)) != 20:
        masks_logger.error("Неверное число символов в номере счета")
        return ""
    masks_logger.info("Выполняется маскировка номера счета")
    return "**" + str(account_number)[-4:]
