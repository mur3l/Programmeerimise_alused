"""
Kirjuta programm, mis küsib kasutajalt ilma ja kuupäeva ning
olenevalt vastusest kirjutab erineva tegevuse ekraanile.

Kasutame liit tingimust ja vähemalt kolme erinevat tegevust.
"""
import datetime
from wsgiref.util import request_uri

x = datetime.datetime.now()
print(x)

rainy = "vihmane"
date_before_christmas = "20.12.2024"
date_in_autumn = "10.10.2025"

weather = input("Milline ilm on?")
date = input("Mis kuupäev on?")

if weather == rainy and date == date_before_christmas:
    print("Pole eriti talvine ilm aga jalutada võib ikka.")
elif weather == rainy and date == date_in_autumn:
    print("Ilus sügis ilm, mine porilompi hüppama.")

if weather == rainy:
    if date == "20.12.2024":
        print("Pole eriti talvine ilm aga jalutada võib ikka.")
    elif date == "10.10.2025":
        print("Ilus sügis ilm, mine porilompi hüppama.")

"""
Koosta programm, mis küsib kasutajalt temperatuuri Celsiuse kraadides ja
väljastab tulemuse Fahrenheiti kraadides.
Kuidas muuta programmi nii, et võimalik oleks teisendamine nii üht- kui teistpidi?
Proovi.
"""


def convert(temperature, from_unit, to_unit):
    from_unit = unit.lower() [0]
    if from_unit == to_unit:
        return temperature, unit
    if from_unit == "c":
        if to_unit == "f":
            result = temperature * 1.8 + 32
            return result, "fahrenheit"
        elif to_unit == "k":
            result = temperature - 273.15
            return result, "kelvin"
    elif from_unit == "f":
        result_c = (temperature - 32) / 1.8
        if to_unit == "c":
            return result_c, "celsius"
        elif from_unit == "k":
            result = result_c - 273.15
            return result, "kelvin"
    return "võimatu", "teisendada"


if __name__ == '__main__':
    temperature = float(input("Mis on temperatuur?"))
    unit = input("Mis ühikutes (celsius/fahrenheit/kelvin)?")
    to_unit = input("Mis ühikus soovid vastust (c/f/k)?")
result_temperature, result_unit = convert(temperature, unit, to_unit)
print(f"{temperature} {unit} on {result_temperature} {result_unit}")
