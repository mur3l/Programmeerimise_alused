"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False


def test_students_study_evening_without_coffee_studying():
    """During the evening without coffee students study."""
    assert students_study(19, False) is True


def test_lottery_all_same_numbers():
    """If all three numbers are the same, return 10."""
    assert lottery(5, 5, 5) == 10


def test_lottery_two_same_numbers():
    """If two numbers are the same, return 5."""
    assert lottery(5, 5, 3) == 5


def test_lottery_all_different_numbers():
    """If all three numbers are different, return 1."""
    assert lottery(2, 3, 1) == 1


def test_fruit_order_possible():
    """Order can be fulfilled with given small and big baskets."""
    assert fruit_order(4, 1, 9) == 4


def test_fruit_order_not_possible():
    """Order cannot be fulfilled with given small and big baskets."""
    assert fruit_order(3, 1, 10) == -1
