import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum_result = num_a + num_b
    difference_result = num_a - num_b

    return sum_result, difference_result


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    return num_a / num_b


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    return num_a // num_b


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    return num_a * num_b, num_a ** num_b, num_a % num_b


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    return (num_a + num_b) / 2


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    return round(math.pi * radius ** 2, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    return round((math.sqrt(3) / 4) * side_length ** 2)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    return b ** 2 - 4 * a * c


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    return math.sqrt(a ** 2 + b ** 2)


def calculate_cathetus_length(c: int, a: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    c, a = max(c, a), min(c, a)

    return math.sqrt(c ** 2 - a ** 2)
