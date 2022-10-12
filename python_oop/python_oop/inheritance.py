class Animal(object):
  def __init__(self, name = "", sex = "", age = 0, weight = 0, color = ""):
    self.name = name; self.sex = sex; self.age = age
    self.weight = weight; self.color = color
  def breathe(self): pass 
  def eat(self, food): pass
  def run(self, destination): pass
  def sleep(self, hours): pass
  
class Cat(Animal):
  def __init__(self, name = "", sex = "", age = 0, weight = 0, color = "", isNasty = True):
    super().__init__(name = name, sex = sex, age = age, weight = weight, color = color)
    self.isNasty = isNasty
  def meow(self):
    print("Meow")
    
class Dog(Animal):
  def __init__(self, name = "", sex = "", age = 0, weight = 0, color = "", bestFriend = "Human"):
    super().__init__(name = name, sex = sex, age = age, weight = weight, color = color)
    self.bestFriend = bestFriend
  def bark(self):
    print("Bow Wow")
    
a = Animal("animal")
print(a)
c = Cat(name = "Mimi", sex = "female", age = 3, weight = 7, color = "brown")
print(c)
d = Dog(name = "Max", sex = "female", age = 1, weight = 2, color = "white", bestFriend = "Cat")
print(d)
c.meow() 
d.bark()