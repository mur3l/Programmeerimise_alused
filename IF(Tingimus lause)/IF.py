"""Exercises for if statement."""


def are_equal(num_a: int, num_b: int) -> str:
    """Return "equal" if given numbers are equal and "not equal" if not."""
    return "equal" if num_a == num_b else "not equal"


def positive_or_negative(num_a: int) -> str:
    """Return "negative", "positive" or "zero" depending on the given integer."""
    if num_a > 0:
        return "positive"
    elif num_a < 0:
        return "negative"
    else:
        return "zero"


def is_in_string(letter: str, word: str) -> bool:
    """If given letter is in given word return True, else return False."""
    return letter in word


def are_same_length(str_a: str, str_b: str) -> bool:
    """Return True if given strings are of equal length or False if not."""
    return len(str_a) == len(str_b)


def is_letter_or_digit(symbol: str) -> str:
    """Return "letter" if given symbol is a letter, "digit" if given symbol is a digit and "other" if its neither."""
    if symbol.isalpha():
        return "letter"
    elif symbol.isdigit():
        return "digit"
    else:
        return "other"


def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    """Given two strings, return True if last symbols are the same and False if not."""
    return str_a[-1] == str_b[-1] if str_a and str_b else False


def hundred(num_a: int) -> int:
    """Given a positive integer num_a. If its smaller or equal to 100 return 100 - num_a. Else return the remainder from dividing it with 100."""
    return 100 - num_a if num_a <= 100 else num_a % 100
