class Student(object):
    # 学员信息： 姓名 性别 电话
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name},{self.gender},{self.tel}'

# aa = Student('aa', 'nv', 111)
# print(aa)
