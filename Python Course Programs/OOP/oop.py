class Person:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1
    def getName(self):
        print ('Name is %s' %self.name)
    def getAge(self):
        print ('Age is %s' %self.age)
    def returnCount(self):
        return (Person.count)

stu1 = Person('Reza', 25 )
stu1.getName()
stu1.getAge()
print ('Number of Persons: %s' %stu1.returnCount() )