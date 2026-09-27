import random

names = ['Ado', 'Emilia', 'Yui', 'Beatrice', 'Rem', 'Ram', 'Ren', 'Aiko']

print('Length is', len(names))

first = 0
middle = (len(names))//2
last = len(names)-1
print(f"First {names[first]} Middle is {names[middle]} and last is {names[last]}")


mixed_data_types = ["Arsenii", 20, 180.1, "Married", {"Money" : False}, "Myru 1"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies, " It has", len(it_companies), " companies")

it_companies.append("Kadokava")

middle_it = len(it_companies)//2
it_companies.insert(middle_it, "Comma")

print(it_companies)

what_to_change = random.randint(0, 8)

print(it_companies[what_to_change].upper())

it_companies[what_to_change] = it_companies[what_to_change].upper()

print(it_companies)

it_companies.extend(["#; "])


print("F yes") if it_companies.index("Facebook")!= -1 else print("F no")

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)
