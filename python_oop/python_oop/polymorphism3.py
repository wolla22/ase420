class Animal(object): 
  def makeSound(): pass
class FourLegged(object):
  def run(self, destination): pass
class OxygenBreather(object):
  def breathe(self): pass
  
class Cat(Animal, FourLegged, OxygenBreather):
  def run(self, destination):
    print(f"I run to {destination}")
  def breathe(self):
    print("I breathe")
    
c = Cat()
c.run("NKU")
c.breathe()