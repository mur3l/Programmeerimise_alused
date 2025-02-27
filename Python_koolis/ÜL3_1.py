name = input("Palun sisesta oma nimi:")
print(name * 5)


def solution():
    name = input("Palun sisesta oma nimi:")
    for i in range(5):
        print(f"Ole tervitatud, {name}, {i+1} korda.")

if __name__ == "__main__":
    solution()



