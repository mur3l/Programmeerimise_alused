def organise_by_first_symbol(strings: list) -> dict:
    organised_dict = {}
    for word in strings:
        first_char = word[0]
        organised_dict.setdefault(first_char, []).append(word)
    return organised_dict