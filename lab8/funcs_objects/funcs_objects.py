import math
from objects import *

def distance(points, points2):
   return math.sqrt((points.x + points2.x)**2 + (points.y - points2.y)**2)
   
def circles_overlap(circle, circle2):
   return distance(circle.center, circle2.center) < circle.radius+circle2.radius
   

   
   