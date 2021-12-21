class kmu:
    name = ''
    age = 0
    id = 0
    phone = ''

    def __init__(self, name, age, id, phone):
        self.name = name
        self.age = age
        self.id = id
        self.phone = phone
    
    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.age, self.id, self.phone)

class kmuStudent(kmu):
    parentPhone = ''
    
    # def __init__(self, name, age, id, phone, parentPhone):
    #     self.name = name
    #     self.age = age
    #     self.id = id
    #     self.phone = phone
    #     self.parentPhone = parentPhone
    
    def __init__(self, name, age, id, phone, parentPhone):
        super().__init__(name, age, id, phone)
        self.parentPhone = parentPhone

    # def __str__(self):
    #     return '{} {} {} {} {}'.format(self.name, self.age, self.id, self.phone, self.parentPhone)
    
    def __str__(self):
        return super(kmuStudent, self).__str__() + ' {}'.format(self.parentPhone)

class kmuPro(kmu):
    major = ''

    def __init__(self, name, age, id, phone, major):
        super().__init__(name, age, id, phone)
        self.major = major
    
    def __str__(self):
        return super(kmuPro, self).__str__() + ' {}'.format(self.major)

class kmuScholarship(kmu):
    Scholarship = 0

    def __init__(self, name, age, id, phone, Scholarship):
        super().__init__(name, age, id, phone)
        self.Scholarship = Scholarship
    
    def __str__(self):
        return super(kmuScholarship, self).__str__() + ' {}'.format(self.Scholarship)

student = kmuStudent('JYC', 20, 2021, '010-XXXX-XXXX', '010-ABCD-EFGH')
print(student)

pro = kmuPro('JYC', 20, 2021, '010-XXXX-XXXX', 'SE')
print(pro)

Scholarship = kmuScholarship('JYC', 20, 2021, '010-XXXX-XXXX', 100000000)
print(Scholarship)