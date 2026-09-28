
e = 0
p = 0

for number in range(101):
    e += number if number%2 == 0 else 0
    p += number if number%2 != 1 else 0

print(f"This is even sum {e}. This is odd sum {p}")

import sys
from pathlib import Path

# go up one level from one/ → project/
sys.path.append(str(Path(__file__).resolve().parent.parent))

from data.countries import country_f
from data.countries_data import lol


countr = country_f()

for item in countr:
    if 'land' in item:
        print(item)


info = lol()

languages = dict()
for item in info:
    languages_spoken = item.get("languages")
    if not languages_spoken: continue
    for language in languages_spoken:
        if(languages.get(language)):
            languages[language] +=1
        else:
            languages[language] = 1

print(f"The total number of the languages is {len(languages)}")

for key, item in languages.items():
    print(f"There are {item} people that speak {key}")


top10 = sorted(languages.items(), key = lambda kv: kv[1], reverse=True)[:10]

print(top10)


top10_population = sorted(info, key= lambda kv: kv['population'], reverse=True)[:10]

for item in top10_population:
    print(item['population'], " In the ", item['name'])