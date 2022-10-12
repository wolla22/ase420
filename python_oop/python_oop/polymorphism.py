class Animal(object): pass
class Cat(Animal):
  def meow(self): print("Meow")
class Dog(Animal):
  def bark(self): print("Bow Wow")
  
c = Cat()
d = Dog()
animals = [c, d]
for a in animals:
  if type(a) == Cat: a.meow()
  else: a.bark() 