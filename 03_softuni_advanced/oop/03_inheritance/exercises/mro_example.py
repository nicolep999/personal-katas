class A:

    def hi(self):
        return "from class a Hi"


class B(A):
    def hi(self):
        return "from class b Hi"


class D:
    def hi(self):
        return "from D"


class C(B, D):
    pass


c = C()
print(c.hi())
print(C.__mro__)
