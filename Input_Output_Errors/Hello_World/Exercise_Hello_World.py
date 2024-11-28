name = input("Enter your name:")
print(f"Hi {name}!")


def main():
    print("Hello World!")


def print_hello_world():
    return print


if __name__ == "__main__":
    print_hello_world()("Hello World!")
