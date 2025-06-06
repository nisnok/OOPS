class Person:
    name = "anonymous"

    def changeName(self,name):
        self.name = name

p1 = Person()
print(p1.name)