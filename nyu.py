# class student:
#     def __init__(self,Fullname, marks):
#         self.name = Fullname
#         self.marks=marks
#         print("Adding the new student in the data base")
#
#     def hello(self):
#         print ("welcome Student", self.name)
#
#     def get_marks(self):
#         return self.marks
#
#
# s1 = student("Rajat",22)
# print(s1.name)
# s2 = student("Rahul", 25)
# s2.hello()
# s1.hello()
#
# print(s1.get_marks())



#
# class students:
#     def __init__(self, name,marks):
#         self.name=name
#         self.marks=marks
#
#     @staticmethod
#     def hello():
#         print("Hello")
#
#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name,"your average score is: ",sum/3)
# s1= students("Rajat",[25,20,30])
# s1.hello()
# s1.get_avg()






class Account:
    def __init__(self,bal,acc):
        self.balance =bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total Balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs." ,amount, "was credited")
        print("Total Balance = ",self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)