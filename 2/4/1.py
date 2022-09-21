from linecache import getline

line_counter = sum(1 for line in open('test.txt'))

with open('test.txt') as f, open('copy_rev_test.txt', 'w') as w:
    for _ in f:
        w.write(getline('test.txt', line_counter))
        line_counter -= 1


# with open('test.txt') as f, open('copy_rev_test.txt', 'w') as w:
#     lines = []
#     for line in f:
#         lines.append(line.rstrip())
#
#     lines = '\n'.join(lines[::-1])
#
#     w.write(lines)


# with open('test.txt') as f, open('copy_rev_test.txt', 'w') as w:
#     lines = f.readlines()
#     lines[0] = lines[0].rstrip()
#     lines[-1] = lines[-1] + '\n' if '\n' not in str(lines[-1]) else lines[-1]
#     w.writelines(reversed(lines))
