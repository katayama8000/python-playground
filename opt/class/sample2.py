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

# クラス変数
# クラス変数はクラス定義の中で定義された変数
# クラス変数はインスタンス変数とは異なり、
# インスタンスごとに値が異なるものではなく、
# クラスごとに値が共有されるもの

class D:
    x = 10
    def __init__(self):
        print("D.__init__")
    def d(self):
        print("D.d")

d = D()
print(d.x)
d.x = 20
print(d.x)
print(D.x)

# スタッティックメソッド
class E:
    @staticmethod
    def e():
        print("E.e")

E.e()

# 特殊メソッド
# 特殊メソッドは、特定のイベントが発生したときに自動的に呼び出されるメソッド

class F:
    def __init__(self):
        print("F.__init__")    
    def __del__(self):
        print("F.__del__")

f = F()
del f



