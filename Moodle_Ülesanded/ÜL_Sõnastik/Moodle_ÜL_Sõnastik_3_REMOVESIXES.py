def remove_sixes(six_dict: dict) -> dict:
    return {k: v for k, v in six_dict.items() if v % 6 != 0}