"""LOOP exercise."""


def sum_between(start: int, end: int) -> int:
    """Return sum of integers between start and end (both included).

    print(sum_between(3, 5)) => 3 + 4 + 5 = 12
    print(sum_between(5, 5)) => 5
    """
    return sum(range(start, end + 1))


def sum_of_even_numbers(n: int) -> int:
    """Return sum of even numbers from 0 up to n (included).

    print(sum_of_even_numbers(5)) => 0 + 2 + 4 = 6
    print(sum_of_even_numbers(0)) => 0
    """
    return sum(i for i in range(n + 1) if i % 2 == 0)


def sum_of_multiples(n: int, end: int) -> int:
    """Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    return sum(i for i in range(0, end + 1) if i % n == 0)


def cross_sum(numbers: str) -> int:
    """Return cross sum of numbers.

    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    return sum(int(i) for i in numbers)


def multiply_between(start: int, end: int) -> int:
    """Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    result = 1
    for i in range(start, end + 1):
        result *= i
    return result


def make_hola_string(count: int) -> str:
    """Make hola string.

    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) =>
    """""
    return "hola" * count


def compound_interest(amount: int, years: int, rate: int) -> float:
    """Calculate compound interest.

    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    return amount * ((1 + rate / 100) ** years)


def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.

    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    vowels = "aeiouAEIOUöõäüÖÕÄÜ"
    return ''.join(char for char in original_string if char not in vowels)


if __name__ == '__main__':
    print(sum_between(3, 5))
    print(sum_between(5, 5))

    print(sum_of_even_numbers(5))
    print(sum_of_even_numbers(0))

    print(sum_of_multiples(3, 10))
    print(sum_of_multiples(7, 10))
    print(sum_of_multiples(11, 10))

    print(cross_sum("1234"))
    print(cross_sum("0"))
    print(cross_sum("4129458"))

    print(multiply_between(1, 3))
    print(multiply_between(4, 14))
    print(multiply_between(0, 7))

    print(make_hola_string(3))
    print(make_hola_string(0))

    print(compound_interest(100, 2, 2))
    print(compound_interest(2000, 6, 8))

    print(remove_vowels("tere-tere"))
    print(remove_vowels("hklmn"))
    print(remove_vowels("aauuiii"))
    print(remove_vowels("öäöü"))
    print(remove_vowels("Vkl hk täshäälk n häälk"))
