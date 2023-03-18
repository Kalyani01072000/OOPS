class Student:
    def __init__(self):
        self.__name = None
        self.__rollNumber = None
        
    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name
        
    def getRollNumber(self):
        return self.__rollNumber
        
    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber
s = Student()

s.setName("John Doe")
s.setRollNumber(1234)

print(s.getName())         # Output: John Doe
print(s.getRollNumber())   # Output: 1234

