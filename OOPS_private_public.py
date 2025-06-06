class Account:

    # private variables and methods are marked by __ and are only accessible within the class
    __name = "anonymous"

    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)
    
    def __hello(self):
        print("hello person!")

    def welcome(self):
        self.__hello()

    

acc1 = Account("12345","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())
print(acc1.welcome())