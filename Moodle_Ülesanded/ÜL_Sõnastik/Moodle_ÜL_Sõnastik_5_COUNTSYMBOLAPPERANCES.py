def count_symbol_appearances(stringy: str) -> dict:
    return {char: stringy.count(char) for char in set(stringy)}