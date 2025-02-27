print("Tere! Õpime arvtutama, esitan 10 liitmistehet, püüa vastata õigesti.")

#import operator
#import random

#operators = [("+", operator.add), ("-", operator.sub), ("*", operator.mul)]

#for i in range(50):
    #a = random.randint(1, 50)
    #b = random.randint(1, 50)
    #op, fn= random.choice(operators)
    #print("{} {} {}". format(a, op, b, fn(a, b)))

from random import randint

def practice_adding(lowest=1,highest=50,count=10):
    correct_answers = 0
    for i in range(count):
        first_number = randint(lowest, highest)
        second_number = randint(lowest, highest)
        random_operator = randint(1, 3)
        if random_operator == 1:
            correct_answer = first_number + second_number
            correct_answers += show_equation("+", correct_answer, first_number, second_number)
        elif random_operator == 2:
            correct_answer = first_number - second_number
            correct_answers += show_equation("-", correct_answer, first_number, second_number)
    print(f"You tried {count} times and got the answer correct {correct_answers} times.")

def show_equation(operation_symbol, correct_answer, first_number, second_number):
        user_answer = int(input(f"{first_number} {operation_symbol} {second_number}= "))
        if user_answer == correct_answer:
            print("CORRECT!")
            return 1
        else:
            print("Try again!")
            print(f"{first_number} {operation_symbol} {second_number} {correct_answer}")
            return 0
    print(f"You tried {count} times and got the answer correct {correct_answers} times.")

if __name__ == "__main__":
    lowest = int(input("Sisesta väikseim täisarv, mida kasutada:"))
    highest = int(input("Sisesta suurim täisarv, mida kasutada:"))
    count = int(input("Sisesta tehete arv: "))
    practice_adding(lowest,highest,count)








