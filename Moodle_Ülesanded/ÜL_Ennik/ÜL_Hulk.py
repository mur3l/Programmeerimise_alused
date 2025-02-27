def add_one(set_a: set) -> set:
    result = set()
    for num in set_a:
        result.add(number + 1)
    return result

if __name__ == '__main__':
    assert add_one({1, 2, 3}) == {1, 2, 3}
    assert add_one({-10, 0, 10}) == {-9, 1, 11}