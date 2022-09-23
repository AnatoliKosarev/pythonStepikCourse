from xml.etree import ElementTree


root = ElementTree.fromstring(input())

result_dict = {'red': 0, 'green': 0, 'blue': 0}
cost = 1


def get_children_cost(root, cost):
    result_dict[root.get('color')] += cost

    for child in root:
        get_children_cost(child, cost+1)


get_children_cost(root, cost)

print(' '.join(str(result_dict[cube]) for cube in result_dict))
