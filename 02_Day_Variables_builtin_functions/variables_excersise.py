# Day 2: 30 Days of Python programming

first_name = "Arsenii"
last_name = "Nemchenko"
full_name = first_name + " " +  last_name
country = "Ukraine"
city = "Bratislava"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False
rain, feeling, smile = True, "Comfy", "Present"

print("My full name is", full_name)
if rain:
    print("It's raining im feeling", feeling)

print(type(first_name))

print(type(full_name))

print(type(age))

print(type(is_married))

print(type(rain))
print("The length of my full name is", len(full_name))
if len(first_name) > len(last_name):
    print("First name is longer than last name. The length is", len(first_name))
else:
    print("Last name is longer than first name. The length is", len(last_name))

name = input()
print("The inputed name is", name)