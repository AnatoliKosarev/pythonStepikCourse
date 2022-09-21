def mod_checker(x, mod=0):
    return lambda y: y % x == mod

mod_3 = mod_checker(3)

print(mod_3(3)) # True
print(mod_3(4)) # False

mod_3_1 = mod_checker(3, 1)
print(mod_3_1(4)) # True

lower = ''
offset = ''
upper = ''
a = ''

a[lower + offset : upper + offset]
a[lower + offset:upper + offset]

a[lower : : upper]

a[lower+offset : upper+offset]

a[lower:upper], a[lower:upper:], a[lower::step]
