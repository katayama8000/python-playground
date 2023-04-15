# クラスの多重継承
class A:
    def __init__(self):
        print("A.__init__")
    def a(self):
        print("A.a")

class B:
    def __init__(self):
        print("B.__init__")
    def b(self):
        print("B.b")

class C(A, B):
    def __init__(self):
        print("C.__init__")
    def c(self):
        print("C.c")

c = C()
c.a()
c.b()
c.c()