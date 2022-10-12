from copy import deepcopy

# class Airplane() is also OK 
class Airplane(object): 
  id = 0 # class variable
  def __init__(self, speed = 0, altitude = 0, rollAngle = 0, pitchAngle = 0, yawAngle = 0):
    self.speed = speed
    self.altitude = altitude
    self.rollAngle = rollAngle
    self.pitchAngle = pitchAngle
    self.yawAngle = yawAngle
  def __str__(self):
    return f"Speed: {self.speed} ..."
  def __eq__(self, other):
    return self.speed == other.speed

  def fly(self):
    print("I'm flying")
    
a = Airplane(speed = 100)
b = a
print(a == b) # True as same reference
b.speed = 500
print(a.speed) # 500 

a = Airplane(speed = 100)
b = deepcopy(Airplane(speed = 100))
print(a == b) # False
b.speed = 500
print(a.speed) # 100