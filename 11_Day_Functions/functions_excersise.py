
def is_prime(number):
    print(number)
    for i in range(2, number):
        if number % i == 0:
            print(i)
            return False
    return True

def contains_unique_only(param: list):
    found = dict()
    for item in param:
        if(found.get(item)):
            return False
        else:
            found[item] = True
    return True

def all_same_datatype(param: list):

    for item in param:
        for item_inner in param:
            if type(item) != type(item_inner):
                return False
    return True
items = [[True], [True], [False], [False], [False]]

print(all_same_datatype(items))