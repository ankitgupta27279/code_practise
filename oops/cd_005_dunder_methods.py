class Employee:

    num_of_emps=0
    raise_amount=1.04

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=self.first+"."+self.last+"@company.com"
        Employee.num_of_emps+=1

    def get_full_name(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)
        # self.pay=int(self.pay*Employee.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay=emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


class Developer(Employee):
    # pass
    raise_amount=1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) # this also works fine
        self.prog_lang=prog_lang

    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.get_full_name(), self.email)

    def __add__(self, other):
        return self.pay+other.pay

    def __len__(self):
        return len(self.get_full_name())


dev_1=Developer("Corey", "Schafer", 5000, "Python")
dev_2=Developer("Test", "User", 60000, "Java")

# print(dev_1)
print(repr(dev_1))
print(dev_1.__repr__())
print(str(dev_1))
print(dev_1.__str__())

print(dev_1+dev_2)
print(len(dev_1))
