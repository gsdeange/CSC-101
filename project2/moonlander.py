import landerFuncs

def main():
   i = 1
   elapsedtime = 0
   velocity = 0.00
   fuelRate = 0
   acceleration = -1.62

   landerFuncs.showWelcome()
   altitude = landerFuncs.getAltitude()
   fuel = landerFuncs.getFuel()
   print()
   
   landerFuncs.displayLMState(elapsedtime, altitude, velocity, fuel, fuelRate)

   while altitude > 0:
      elapsedtime = elapsedtime+1
      if(fuel > 0):
         fuelRate = landerFuncs.getFuelRate(fuel)
         fuel = landerFuncs.updateFuel(fuel, fuelRate)
      else:
         fuelRate = 0
		 
      acceleration = landerFuncs.updateAcceleration(1.62, fuelRate)
      altitude = landerFuncs.updateAltitude(altitude, velocity, acceleration)
      velocity = landerFuncs.updateVelocity(velocity, acceleration)
      if(fuel > 0):
         landerFuncs.displayLMState(elapsedtime, altitude, velocity, fuel, fuelRate)
	   
      if(fuel == 0 and altitude!=0):
         print("OUT OF FUEL - Elapsed Time: ", elapsedtime, "Altitude: %0.2f" % altitude, "Velocity: %0.2f"% velocity)
   
   if(fuel <= 0):
      landerFuncs.displayLMState(elapsedtime, altitude, velocity, fuel, fuelRate)
   landerFuncs.displayLMLandingStatus(velocity)

if __name__ == "__main__":
    main()
