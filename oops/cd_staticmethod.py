class Student:
    @staticmethod
    def exam_pattern(self):
        print("this is a static method")

    def attendance(self):
        print("this is an instance method")


stu=Student()
stu.attendance()
# stu.exam_pattern(10)
Student.exam_pattern(10)
