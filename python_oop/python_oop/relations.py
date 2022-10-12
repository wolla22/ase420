class Professor(object):
  def callStudent(self, student):
    print(f"Hello {student.name}")
  def getSalary(self, salary):
    print(f"I use ${salary.amount}")
    
class Student(object):
  def __init__(self, name):
    self.name = name
    
s = Student("John")
p = Professor()
p.callStudent(s)

class Salary(object):
  def __init__(self, amount):
    self.amount = amount
    
s = Salary(1000)
p.getSalary(s)