from tkinter.font import names


def print_list(capitols, numbered=False):
    for number, name in enumerate(capitols):
        if numbered:
            print(f"{number + 1}. {name}")
        else:
            print(f"{names}")


if __name__ == '__main__':
    capitols = ["Tallinn", "Riia", "Helsinki", "Stockholm", "Vilnius",
                "Warssav", "Brüssel", "Pariis", "Lissabon", "Berlin"]
    print_list(capitols)
    capitols.sort()
    for i in range(2):
        new_capitol = input(f"Sisesta {i+1}. lisa pealinn: ")
        capitols.append(new_capitol)
    capitols.sort()
    print_list(capitols, numbered=True)
    print(f"Meie järjendis on {len(capitols)} Euroopa pealinna")
