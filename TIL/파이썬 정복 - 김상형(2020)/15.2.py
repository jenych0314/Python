class Human:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")
    
class Student(Human):
    def __init__(self, age, name, stunum):
        super().__init__(age, name)
        self.stunum = stunum

    def intro(self):
        super().intro()
        print("학번: " + str(self.stunum))

    def study(self):
        print("1234")
    
    def __str__(self) -> str:
        return "안녕하세요 %d살 %s입니다." %(self.age, self.name)

kim = Human(29, "개떵이")
kim.intro()

lee = Student(34, "이상해", 930011)
lee.intro()
lee.study()
print(lee)