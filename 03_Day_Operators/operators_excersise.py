

age = 20
height = 1.79
'''
base  = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
'''
python = 'python'
dragon = 'dragon'

if len(python) > len(dragon):
    print("Python > dragonsddddsds")
else:
    print("No")

sent = "I hope this course is not full of jargon."
if "jargon" in sent:
    print("I'm in")

print("there is on in python", "on" in python)
print("there is on in dragon", "on" in dragon)

age = int(input("Enter how many years have you lived:"))
age_in_seconds = age*365*24*60*60
print("You have lived for", age_in_seconds, "seconds")

values = [1, 1, 1, 1, 1]
for i in range(0, 5):
    values[0] = i+1
    values[2] = i+1
    values[3] = (i+1)**2
    values[4] = (i+1)**3
    print(*values, sep=' ')