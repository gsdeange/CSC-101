# Project 2 - Moonlander
#
# Name: Garrett DeAngelis
#Instructor: Hatalsky

def showWelcome():
   print()
   print("Welcome aboard the Lunar Module Flight Simulator")
   print()
   print("   To begin you must specify the LM's initial altitude")
   print("   and fuel level. To simulate the actual LM use")
   print("   values of 1300 meters and 500 liters, respectively.")
   print()
   print("   Good luck and may the force be with you!")
   print()
   
def getFuel():
   
   i = 1
   while i > 0:
      fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
      if(fuel > 0):
         return fuel
         break
      else:
         print("ERROR: Amount of fuel must be positive, please try again")
    

def getAltitude():
   i = 1
   while i > 0:
      altitude = int(input("Enter the initial altitude of the LM (in meters): "))
      if(altitude >= 1 and altitude <= 9999):
         return altitude  
         break
      else:
         print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again")
		 
   

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
   if(elapsedTime == 0):
      print("LM state at retrorocket cutoff")
   elif(altitude <= 0):
      print()
      print("LM state at landing/impact")
   print("Elapsed Time:     " , elapsedTime, "s")
   print("        Fuel:    " ,fuelAmount, "l")
   print("        Rate:     " ,fuelRate, "l/s")
   print("    Altitude:    %0.2f" % altitude, "m")
   print("    Velocity:     %0.2f" % velocity, "m/s")
   
def getFuelRate(currentFuel):
   i = 1
   while i > 0:
      fuelrate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
      if(fuelrate >= 0 and fuelrate <= 9 and fuelrate <= currentFuel):
         
         break
      elif(fuelrate >= currentFuel):
         
         return currentFuel
      else: 
         print("ERROR: Fuel rate must be between 0 and 9, inclusive")
         print()
   return fuelrate
   
 
def updateAcceleration(gravity, fuelRate):
   acceleration = gravity*((fuelRate/5)-1)
   return acceleration
	
def updateAltitude(altitude, velocity, acceleration):
   newAltitude = abs(altitude) + velocity + (acceleration/2)
   if(newAltitude>0):
      return abs(newAltitude)
   else: 
      return 0

def updateVelocity(velocity, acceleration):
   newVelocity = velocity+acceleration
   if(newVelocity == 0):
      newVelocity = abs(newVelocity)
   return newVelocity

def updateFuel(fuel, fuelRate):
   newFuel = fuel - fuelRate
   return newFuel

def displayLMLandingStatus(velocity):
   if(velocity <= 0 and velocity >= -1):
      print("Status at landing - The eagle has landed!")
   elif(velocity <= -1 and velocity >= -10):
      print("Status at landing - Enjoy your oxygen while it lasts!")
   elif(velocity <= -10):
      print("Status at landing - Ouch - that hurt!")
