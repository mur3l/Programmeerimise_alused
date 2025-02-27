print("Item cost:")
# Give a 20% discount

print((25 * 4) * 0.2)

print("Funds to send:", 25 * 4 + 50 / 10 + 10 - 5)
# Koma võimaldab sisestada mitu käsklust

print(57 % 4)
# Kui mitu korda läheb sisse, nt: 3 läheb täielikult ehk tulem on 0 aga neljaga on 1 (Üks jääb üle)

print(30 / 9)  # 3.333...
print(30 // 9)  # 3
# // eemaldab komakoha!

# Variables:
# print("I've had this job for", years, "years and", months, "months")

base_fare = 155
num_of_bags = 2
base_fare = 205 #Muudab alg base fare
total = base_fare * (num_of_bags * 0.75)
print(total)

# Five people traveling
flight_cost = 455
insurance = 19.99
passport = 110
baggage = 45

total = flight_cost + insurance + passport + baggage #Võib ka nii, total = (flight_cost + insurance + passport + baggage) * 5
print("Total cost:", total * 5)

# 4 Variables for ticket prices

adult = 2
children = 2

adult_price = 55
child_price = 27

total = (adult * adult_price) + (children * child_price)
print("Trip total price:", total)

# Resort offers 500 per night, family desires to stay for 1week. There is a promo of 30% off!

price = 500
days = 7

total = (price * days) * 0.7 # * 0.7 = 30% Total hinnast maha!
print("Special price:", total)

# User Data Input:

# Create 3 variables to collect info from a user
# These variables  are first name, country & city
# Print off their information -> ex. Joh Lives in Seattle, USA

first_name = input("Enter your first name: ")
country = input("Enter your countries name: ")
city = input("Enter your cities name: ")

print(first_name, "Lives in", city, ",", country)

# Create 2 variables to gather user information
# 1 car rental price for one day, 1 number of days to rent
# Create a total variable to add these (multiply) 2 variables together
# Print out their total cost -> ex. Total car price: 550

#car_price = 50 #Per day
#days = input("How many days do you wish to rent?: ")
#print(car_price * days) # = 222222222...

rental_price = input("Enter rental price per day: ") #int tekitab sellest numbrid
rental_price = int(rental_price)
days = input("Enter number of days to rent: ") #int tekitab sellest numbrid
days = int(days)
total = rental_price * days
print("Total Car Price:", total)

# Create 3 variables for shipping packages
# A user can enter the weight of 3 packages
# Create a variable to add these 3 variables together
# Offer a 20% discount on shipping weight
# Print off total cost for shipment

weight_1 = input("Enter the weight of the first item:")
weight_1 =int(weight_1)
weight_2 = input("Enter the weight of the second item:")
weight_2 =int(weight_2)
weight_3 = input("Enter the weight of the third item:")
weight_3 =int(weight_3)
total = weight_1 + weight_2 + weight_3
print("Total weight of your items:", total * 0.8)

# Create a user ID
# Collect their name, age
# Their user ID number is 786147
# Convert everything to a string
# Print off their information

name = input("Enter your full name: ")
age = input("Enter your age: ")
id_number = 786147
id_number = str(id_number)

print("Your ID is: ", id_number, name, age)









