n = int(input())

parents = {}
for _ in range(n):
    a = input().split()
    parents[a[0]] = [] if len(a) == 1 else a[2:]


def is_parent(child, parent):
    if child == parent:
        return True

    for p in parents[child]:
        if is_parent(p, parent):
            return True

    return False


q = int(input())
for _ in range(q):
    a, b = input().split()
    print("Yes" if is_parent(b, a) else "No")


#=============================================================================
# n = int(input())
#
# parents = {}
# for _ in range(n):
#     a = input().split()
#     parents[a[0]] = [] if len(a) == 1 else a[2:]
#
#
# def is_parent(child, parent):
#     return child == parent or any(map(lambda p: is_parent(p, parent), parents[child]))
#
#
# q = int(input())
# for _ in range(q):
#     a, b = input().split()
#     print("Yes" if is_parent(b, a) else "No")


#=============================================================================
# class_count = int(input())
# class_dict = {}
#
# for _ in range(class_count):
#     class_info = input().split(' : ')
#     class_name = class_info[0]
#     class_parent = list(class_info[1].split()) if len(class_info) > 1 else []
#
#     if class_name in class_dict:
#         class_dict[class_name].extend(class_parent)
#
#     class_dict[class_name] = class_parent
#
# query_count = int(input())
#
#
# def search_for_parent(class_graph, child, parent, path=[]):
#     path = path + [child]
#
#     if child == parent:
#         return path
#
#     if child not in class_graph:
#         return None
#
#     for node in class_graph[child]:
#         if node not in path:
#             new_path = search_for_parent(class_graph, node, parent, path)
#             if new_path:
#                 return new_path
#
#     return None
#
#
# for _ in range(query_count):
#     query_class_parent, query_class_child = input().split()
#
#     found_path = search_for_parent(class_dict, query_class_child, query_class_parent)
#
#     if found_path:
#         result = 'Yes'
#     else:
#         result = 'No'
#
#     print(result)
