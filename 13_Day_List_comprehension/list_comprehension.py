
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [number for number in numbers if number<=0]
print(filtered_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattened_list = [number for inner in list_of_lists for number in inner]
print(flattened_list)


result = [(i, 1, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)] 
for item in result:
    print(item)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], 
             [('Norway', 'Oslo')]]

comprehended_list =[
    [country, country[:3].upper(), city] for sub_list in countries for country, city in sub_list
]


print(comprehended_list)
"""[['FINLAND','FIN', 'HELSINKI'], 
 ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
"""