# class Airplane() is also OK 
class Airplane(object): 
  id = 0 # class variable
  def __init__(self, speed = 0, altitude = 0, rollAngle = 0, pitchAngle = 0, yawAngle = 0):
    self.speed = speed
    self.altitude = altitude
    self.rollAngle = rollAngle
    self.pitchAngle = pitchAngle
    self.yawAngle = yawAngle

  def fly(self):
    print("I'm flying")
    
a = Airplane()
a.fly()

# It's possible, but violating encapsulation
a.speed = 100 
print(a.speed)

# class variable can be modified by any objects
b = Airplane()
b.id = 10
print(a.id)