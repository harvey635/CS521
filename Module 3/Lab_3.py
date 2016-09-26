class Parent:
    def __init__(self):
        self.greeting = "Hi, I'm a parent object."


class ChildA(Parent):
    def __init__(self):
        super().__init__()
        self.greeting = "Hi, I'm a child object"


class ChildB(Parent):
    pass

p = Parent()
print(p.greeting)

ca = ChildA()
print(ca.greeting)

cb = ChildB()
print(cb.greeting)
