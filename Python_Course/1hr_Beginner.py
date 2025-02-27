#""" print() """
print("Murel on väga hea!")
print("It's really good")

#""" variable """ (Kood {} sees)
#string (Karakterid kas "" või '' sees ehk "Tauno Tippi")
full_name = "Tauno Tippi"

print(f"Hello, {full_name}")

#integer (Täis numbrid ehk 25 mitte 25.5)
full_name = "Tauno Tippi"
age = 25

print(f"Hello, {full_name}")
print(f"You are {age} years old.")

#float (Numbrid mis sisaldavad koma kohta)
full_name = "Tauno Tippi"
age = 25
gpa = 3.2

print(f"Hello, {full_name}")
print(f"You are {age} years old.")
print(f"Your gpa is {gpa}.")

#boolean (True or False, peab algama suure tähega, if/is jne)
full_name = "Tauno Tippi"
age = 25
gpa = 3.2
is_student = True #või is_student = False

print(f"Hello, {full_name}")
print(f"You are {age} years old.")
print(f"Your gpa is {gpa}.")
print(f"Are you a student?: {is_student}")

is_student = False #või True

if is_student:
    print("You are a student.")

else:
    print("You are not a student.")


#""" arithmetic """ (arvutamine, +(addition), -(substraction), *(multiplication), /(division),
# //(integeri division[returns an integer]), %(remainder))
friends = 5

friends = friends + 1 #(või 2, 3 jne)
friends = friends - 1
friends = friends * 4
friends = friends / 2 #(tagastab "float" numbri ehk koma kohaga)
friends = friends //2 #(tagastab ümardatud arvu mis on lähim sisestatud ehk 2'ele)


print(friends)



