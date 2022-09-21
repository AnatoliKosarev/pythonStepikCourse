# 1
objects = [1, True, 2, 1, 2, 3, 4, 'qwewe']

n = len(objects)
ans = n
for i in range(n):
    for j in range(i):
        if id(objects[i]) == id(objects[j]):
            ans -= 1
            break

print(ans)

# 2
print(len(set([id(v) for v in objects])))
