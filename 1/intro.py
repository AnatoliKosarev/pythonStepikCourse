str_count = input()
result = []

if str_count and str_count.isdigit():
    int_count = int(str_count)
    for v in range(int_count):
        value = input()
        if value.lstrip('-').isdigit():
            result.append(int(value))

print(sum(result))
