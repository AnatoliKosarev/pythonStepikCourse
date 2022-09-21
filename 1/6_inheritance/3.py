class A:
    pass


class B(A):
    pass


class C:
    pass


class D(C):
    pass


class E(B, C, D):
    pass


"""
if higher parent goes before its' kid - error
here: C is D's parent but goes before D in E inheritance, first should be D, then C
"""
print(E.mro())
