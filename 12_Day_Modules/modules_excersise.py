
def random_user_id():
    import string
    import random
    valid_characters = string.ascii_letters + string.digits
    result = ''
    for _ in range(6):
        character_index = random.randint(0, len(valid_characters) -1)
        result += valid_characters[character_index]

    return result

print(random_user_id())


def rgb_color_gen():
    import random as rand
    return (rand.randint(0, 255), rand.randint(0, 255), rand.randint(0,255))

print(rgb_color_gen())
print(rgb_color_gen())
print(rgb_color_gen())