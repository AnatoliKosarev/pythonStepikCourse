s = input()
a = input()
b = input()

counter = 0


def replace_a_with_b(s, a, b):
    global counter

    if a not in s:
        return counter

    if a in s and a in b:
        return 'Impossible'

    s = s.replace(a, b)
    counter += 1

    return replace_a_with_b(s, a, b)


result = replace_a_with_b(s, a, b)

print(result)


# s = input()
# a = input()
# b = input()
#
# if a not in s:
#     print(0)
# elif a in b:
#     print("Impossible")
# else:
#     ans = 0
#     while a in s:
#         s = s.replace(a, b)
#         ans += 1
#
#     print(ans)