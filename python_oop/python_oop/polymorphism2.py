class Animal(object): 
  def makeSound(): pass
class Cat(Animal):
  def makeSound(self): print("Meow")
class Dog(Animal):
  def makeSound(self): print("Bow Wow")
  
c = Cat()
d = Dog()
animals = [c, d]
for a in animals:
  a.makeSound()