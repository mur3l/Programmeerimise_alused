def find_tallest(height_dict: dict) -> str:
    return max(height_dict, key=height_dict.get)