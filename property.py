class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.math = math
        self.chem = chem
        self.perc = str((self.phy + self.chem + self.math)/3) + '%' # doesnt change if we change any of the above values, which causes issues
    
    def calcPerc(self):
        self.perc = str((self.phy + self.chem + self.math)/3) + '%'
    
    # instead of defining a function like the one above, we can use property decorator.
    # property decorator is used on any method in the class to use it as a property.
    
    @property
    def calcPerc(self):
        return str((self.phy + self.chem + self.math)/3) + '%'
        

    

s1 = Student(98,97,96)
s1.calcPerc()
print(s1.perc)

s1.phy = 87
print(s1.perc)
s1.calcPerc()
print(s1.perc)

