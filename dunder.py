class Complex:
    def __init__(self, real, img ):
        self.real = real
        self.img = img
    
    def showNum(self):
        print(self.real, "i +", self.img, "j")
    
    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    # dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1,3)
num1.showNum()

num2 = Complex(2,4)
num2.showNum()

num3 = num1 + num2
num3.showNum()


