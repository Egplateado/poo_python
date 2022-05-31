class A():
    def primera(self):
        return "\n Esta es la clase A\n"
class B():
    def segunda(self):
        return "Esta es la clase B\n"
class C(A , B):
    pass

c = C()
print(c.primera())
print(c.segunda())

