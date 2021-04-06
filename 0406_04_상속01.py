# 부모 클래스
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

# 자식 클래스
class Student(Person):
    # 학생은 적어도 과목, 학생 아이디가 있어야 되는데.. 
    # --> 그래서 상속 받아서 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        # 부모를 가리키는 키워드(base, super)
        # 자기 자신을 가리키는 키워드(self, this)

        # 명시적으로 부모 생성자 호출
        # 또 코딩할 필요 없음 위에거 끌어오기(깔끔)
        Person.__init__(self, name, phoneNumber) 
        self.subject = subject
        self.studentID = studentID

    # 근데 프린트 인포에 2과목이 없어서 짤려서 출력됨
    # 상속 받아서 재정의(덮어쓰기) + 줄 맞춤 주의!!
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(
            self.subject, self.studentID))


p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__) 안에 있는 멤버 변수들을 딕셔너리 형식으로 보여줌
# print(s.__dict__) 하지만 우리는 프린트인포 메서드를 정의했기 때문에 여기선 쓰지 않음
p.printInfo()
s.printInfo()



