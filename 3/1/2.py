s = input()
t = input()

counter = 0


while t in s:
    counter += 1

    i = s.find(t)

    if i + 1 < len(s):
        s = s[i + 1:]
    else:
        break

print(counter)


# s = input()
# t = input()
#
# print(sum(1 for i in range(len(s)) if s.startswith(t, i)))


