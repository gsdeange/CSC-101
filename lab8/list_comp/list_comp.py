import funcs_objects

def distance_all(points):
   return [funcs_objects.distance(x) for x in points]
   
def are_in_first_quadrant(points):  
   return [x for x in points if x.x > 0 and x.y > 0]
