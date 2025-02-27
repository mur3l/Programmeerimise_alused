def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    return num_a + num_b, num_a - num_b

num_a = int(input("Enter your first number: "))
num_b = int(input("Enter your second number: "))

result = sum_and_difference(num_a, num_b)

print(f"The sum of the two is {result[0]}, The difference is {result[1]}")