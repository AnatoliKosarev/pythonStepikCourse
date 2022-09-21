class_count = int(input())
class_dict = {}

for _ in range(class_count):
    class_info = input().split(':')
    class_name = class_info[0].strip()
    class_parent = list(class_info[1].strip().split()) if len(class_info) > 1 else []

    if class_name in class_dict:
        class_dict[class_name].extend(class_parent)
    else:
        class_dict[class_name] = class_parent

query_count = int(input())
class_except_stack = []


def is_parent(child, parent):
    if child == parent:
        return True

    for p in class_dict[child]:
        if is_parent(p, parent):
            return True

    return False


def class_not_needed_catch(class_to_check):

    for class_in_stack in class_except_stack:
        if is_parent(class_to_check, class_in_stack):
            return True

    return False


for _ in range(query_count):
    class_to_catch = input()

    if class_except_stack and class_not_needed_catch(class_to_catch):
        print(class_to_catch)

    class_except_stack.append(class_to_catch)
