"""Math exercises."""


def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum(num_a, num_b)
    difference = num_a - num_b
    return num_a, num_b, difference
    return sum


print(sum_and_difference(1, 2))


def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division


def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    integer_division: = (round(num_a / num_b), 2)
    return integer_division


def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_bumbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a % num_b
    return multiply_numbers, power, remainder


def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    # Write your code here
    return average


def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    # Write your code here
    return circle_area


def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    return int(round((side_lenght ** 2 * sqrt(3)) / 4, 0))
    return triangle_area


def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    # Write your code here
    return discriminant


def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    # Write your code here
    return c


def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    # Write your code here
    return b


if __name__ == '__main__':
    assert sum_and_difference(5, 6) == (11, -1)
    print(sum_and_difference(11, 9), "== (20, 2)")
    assert float_division(num_a:9, num_b: 3) == 3.0
    assert round(float_division(num_a:10, num_b: 3), 2) == 3.33

    assert integer_division(num_a:10, num_b: 3) == 3
    assert integer_division(num_a:7, num_b: 11) == 0

    assert powerful_operations(num_a:10, num_b: 3) == (30, 1000, 1)
    assert powerful_operations(num_a:2, num_b: 10) == (20, 1024, 2)

    assert find_average(num_a:3, num_b: 7) == 5.0
    assert find_average(num_a:999, num_b: 999) == 999.0

    assert area_of_a_circle(1) == 3.14
    assert area_of_a_circle(19) == 1134.10

    assert area_of_an_equilateral_triangle(3) == 4
    assert area_of_an_equilateral_triangle(15) == 97
