class A:
   def foo(self):
      print("A")

class B(A):
   pass

class C(A):
   def foo(self):
      print("C")

class D:
   def foo(self):
      print("D")

class E(B, C, D):
   pass

E().foo()
"""current -> parents from left to right then higher parent if higher parent class doesn't have kids which we didn't 
check, then next parent to right
so here: current -> B -> C because both have same parent A -> A, because A doesn't have anymore unchecked kids -> D -> object
"""
print(E.mro())
