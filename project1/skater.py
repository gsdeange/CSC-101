# Project 1
#
#Name: Garrett DeAngelis
# Intstructor: P. Hatalsky
# Section: 12

import funcs_tests
import funcs

def main():
   
   weight = float(input("How much do you weigh (pounds)? "))
   distance = float(input("How far away is your professor (meters)?"))
   item = input(" Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")

   skatermass = funcs.poundsToKG(weight)
   massObj = funcs.getMassObject(item)
   velocityObj = funcs.getVelocityObject(distance)
   velocitySkaterraw = funcs.getVelocitySkater(skatermass, massObj, velocityObj)

   #determining the response based on the returned mass
   massresponse = ""
   if(massObj <= 0.1):
      massresponse = "You're going to get an F!"
   elif(massObj > 0.1 and massObj<= 1.0):
      massresponse = "Make sure your professor is OK"
   elif(massObj > 1.0 and distance < 20):
      massresponse = "How far away is the hospital?"
   elif(massObj > 1.0 and distance >= 20):
      massresponse = "RIP professor."

   
   #converting skater velocity to 3 decimal places
   velocitySkater = round(velocitySkaterraw, 3)
   #determining the response based on the returned velocity
   skaterresponse = ""
   if(velocitySkater < 0.2):
      skaterresponse = "My grandmother skates faster than you!"
   elif(velocitySkater >= 0.2 and velocitySkater< 1.0):
      skaterresponse = ""
   elif(velocitySkater >= 1.0):
      skaterresponse = "Look out for that railing!!!"

   #printing the outputs
   print()
   print("Nice throw!", massresponse)
   print("Velocity of skater:" , velocitySkater, "m/s")
   print(skaterresponse)


if __name__== '__main__':
   main()
      
