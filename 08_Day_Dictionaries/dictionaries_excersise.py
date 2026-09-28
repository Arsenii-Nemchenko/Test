

dog = {'name': "Archie", 'color': "brown", 'breed': "IDK", "legs": 3, "age": 5}
student = {'first_name': "Arsenii", 'last_name': "Nemchenko", 
           'gender': "male", 'age': 20, "skills": ["Java", "Python", "php"],
           'marital_status': "free", "country": "Ukraine",
           "city": "Bratislava", "address": "Myru 1"}

print(f"The length of the dictionary is {len(student)}")
print(f"The length of the dictionary is {len(dog)}")

print(f"The type is {type(student.get("skills"))}")
print(dog.keys())
print(dog.values())

del dog["name"]
student['skills'].pop(0)
print(student)