#1
def closest_mod_5(x):
    if x <= 5:
        return 5

    while True:
        if x % 5 == 0:
            return x
        else:
            x += 1

#2
# def closest_mod_5(x):
#     return x if x % 5 == 0 else closest_mod_5(x + 1)


print(closest_mod_5(-1))
