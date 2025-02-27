def get_sum_and_diff(a: int, b: int) -> tuple:
    return a + b, a - b

if __name__ == '__main__':
    assert get_sum_and_diff(1, 2) == (3, -1)
    assert get_sum_and_diff(1, 1) == (2, 0)
    assert get_sum_and_diff(5, 1) == (6, 4)

def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    return tuple({a, b})

if __name__ == '__main__':
    assert create_tuple_from_two_numbers(1, 2) == (1, 2)
    assert create_tuple_from_two_numbers(1, 1) == (1,)

def create_tuple_up_to_n(n: int) -> tuple:
    result = ()
    for i in range(n+1):
        result += (i, )
    return result

if __name__ == '__main__':
    assert create_tuple_up_to_n(2) == (0, 1, 2)
    assert create_tuple_up_to_n(0) == (0,)
    assert create_tuple_up_to_n(-10) == ()

