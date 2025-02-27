"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    return (18 <= time <= 24) or (coffee_needed and 5 <= time <= 17)


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == b == c:
        return 10
    if a == b or a == c or b == c:
        return 5
    if a == 2 and b == 2:
        return 0
    return 1


def fruit_order(small_baskets: int, big_baskets: int,
                ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    max_big_baskets_used = min(big_baskets, ordered_amount // 5)
    remaining_fruits = ordered_amount - (max_big_baskets_used * 5)

    if remaining_fruits <= small_baskets:
        return remaining_fruits
    return -1
