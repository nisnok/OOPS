class Student:

    college_name = "ABC" 
    name = "anonymous" # class attr

    # default constructors
    # If not defined by us, python auto defines this
    def __init__(self):
        pass

    #static methods work at class level. They do not use self parameter
    @staticmethod
    def hello():
        print("hello")
    # parameterized constructors
    def __init__(self, name,marks):
        self.name = name # obj attr > class attribute
        self.marks = marks
        print("Adding new student to Database")
    
    def welcome(self):
        print("welcome student, ", self.name)
    
    def get_marks(self):
        return self.marks

# In the cases below, the parameters match the other constructor not the first one. 
# Therefore, the second one is called.
s1 = Student("Karan",97)
s1.welcome()
s1.hello()
print(s1.name, s1.marks)

s2 = Student("Arjun",88)
print(s2.name, s2.marks)

print(s2.college_name)

""" class = methods + data (attributes) """
""" OOPS Pillars : 
Abstraction - Hiding implementation details and only showing features to user
Encapsulation - data + methods in a capsule - call class object and use
Polymorphism - 
Inheritance - """
