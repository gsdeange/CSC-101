

class Points():
   def __init__(self, x, y):
      self.x = x
      self.y = y
   def __eq__(self, other):
      return self.x == other.x and self.y == other.y
	  
class Circle():
   def __init__(self, points, radius):
       self.center = points
       self.radius = radius
	   

	   
	   


 

     
      