import os

result_dirs = []

for cur_dir, _, files in os.walk('main'):
    for file_name in files:
        if file_name.endswith('.py'):
            result_dirs.append(cur_dir)
            break

result_dirs.sort()

with open('result_dirs.txt', 'w') as out:
    out.writelines('\n'.join(result_dirs))
