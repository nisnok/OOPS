class Person:
    name = "anonymous"

    def changeName(self,name):
        self.name = name
        # 1.if I write Person.name = name instead of self.name = name, both p1.ane and Person.name will be rahul in this case.
        # 2.We can write self.__class__.name as well to do the same thing as above.
        # 3. if I keep it same as above, new attribute name will be created for object, which is different from class attribute name.

    # This is another way of doing #1
    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()
p1.changeName("rahul")
print(p1.name)
print(Person.name)

# instance methods take self as an argument.
# static methods cannot modify class state. Used for utility.
# class methods take cls as argument. It is bound to class.