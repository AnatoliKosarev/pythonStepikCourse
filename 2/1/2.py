class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, __object) -> None:
        if is_negative_int(__object):
            raise NonPositiveError

        super(PositiveList, self).append(__object)


def is_negative_int(value):
    try:
        int_value = int(value)
    except ValueError:
        return False
    else:
        if int_value <= 0:
            return True
    return False


test = PositiveList([1,2,3,-4])
test.append('qwe')
print(test)
