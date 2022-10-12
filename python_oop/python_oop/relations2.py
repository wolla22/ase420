class University(object):
  def __init__(self):
    self.departments = []
    
class Department(object):
  def __init__(self, name):
    self.name = name
    
d1 = Department("cs")
d2 = Department("ase")
u = University() # university is composed of departments
u.departments.append(d1)
u.departments.append(d2)
print(u.departments)