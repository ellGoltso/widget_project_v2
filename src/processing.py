def filter_by_state(list_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Принимает список словарей и опционально значение ключа,
    возвращает новый список словарей,
    у которых ключ state соответствует указанному значению
    """

    new_list_dict: list[dict] = []
    for item in list_dict:
        if state in item.values():
            new_list_dict.append(item)

    return new_list_dict


def sort_by_date(list_dict: list[dict], decrease: bool = True) -> list[dict]:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание);
    Возвращает новый список, отсортированный по дате
    """

    sorted_list: list[dict] = []

    if decrease:
        sorted_list = sorted(list_dict, key=lambda x: x["date"], reverse=True)
    else:
        sorted_list = sorted(list_dict, key=lambda x: x["date"])

    return sorted_list
