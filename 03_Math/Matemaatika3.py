import math


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    sum_result = num_a + num_b
    difference_result = num_a - num_b

    return sum_result, difference_result


def float_division(num_a: int, num_b: int) -> float:
    return num_a / num_b


def integer_division(num_a: int, num_b: int) -> int:
    return num_a // num_b


def powerful_operations(num_a: int, num_b: int) -> tuple:
    return num_a * num_b, num_a ** num_b, num_a % num_b


def find_average(num_a: int, num_b: int) -> float:
    return (num_a + num_b) / 2


def area_of_a_circle(radius: float) -> float:
    return round(math.pi * radius ** 2, 2)


def area_of_an_equilateral_triangle(side_length: float) -> int:
    return round((math.sqrt(3) / 4) * side_length ** 2)


def calculate_discriminant(a: int, b: int, c: int) -> int:
    return b ** 2 - 4 * a * c


def calculate_hypotenuse_length(a: int, b: int) -> float:
    return math.sqrt(a ** 2 + b ** 2)


def calculate_cathetus_length(c: int, a: int) -> float:
    c, a = max(c, a), min(c, a)

    return math.sqrt(c ** 2 - a ** 2)
