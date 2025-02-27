"""
Koosta vähemalt kümnest elemendist koosnev järjend arvudest.
Koosta programm, mis küsib kasutajalt tegurit ja
korrutab kõik algses järjendis olnud arvud sellega läbi ning
väljastab tulemuse ekraanile.


Sisesta tegur: 3
45 * 3 = 135
7 * 3 = 21
...
267 * 3 = 801
"""
import numbers


def print_multiplications(numbers:list,multiplier:int) -> None:
    for number in numbers:
        print(f"{number} * {multiplier} = {number * multiplier}")



if __name__ == '__main__':
    number = int(input("Siesta tegur: "))
    print_multiplications([45,7,12,25,9,100,67,123,-6,267], number)
