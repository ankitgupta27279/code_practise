# class DemoClass:
#     """
#         This is a sample class which I am creating for understanding this class n objects
#     """
#     num=10

#     def sum(self):
#         print("hello sample program")


# print(DemoClass.__doc__)
# obj=DemoClass()
# print(obj.numf)
# obj.sum()


class Employee:
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.email=first+'.'+last+'@company.com'
        self.pay=pay

    def get_full_name(self):
        return f"{self.first} {self.last}"


emp_1=Employee('Corey', 'Schafer', 5000)
emp_2=Employee('Test', 'User', 60000)

# print(emp_1)
# print(emp_2)

# emp_1.first='Corey'
# emp_1.last='Schafer'
# emp_1.email='corey.schafer@company.com'
# emp_1.pay=5000


# emp_2.first='Test'
# emp_2.last='User'
# emp_2.email='test.user@company.com'
# emp_2.pay=60000


# print(emp_1.email)
# print(emp_2.email)
print(emp_1.get_full_name())
print(emp_2.get_full_name())

# print("{} {}".format(emp_1.first, emp_1.last))
# print(f"{emp_1.first} {emp_1.last}")

print(Employee.get_full_name(emp_1))
print(Employee.get_full_name(emp_2))

