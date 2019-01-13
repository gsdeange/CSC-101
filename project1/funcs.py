# Project 1
#
#Name: Garrett DeAngelis
# Intstructor: P. Hatalsky
# Section: 12

import math

#converts pounds to kilograms
def poundsToKG(pounds):
   kilograms = pounds*0.453592
   return kilograms

# return the mass of each object
def getMassObject(object):
   if(object == 't'):
      return 0.1
   elif(object == 'p'):
      return 1.0
   elif(object == 'r'):
      return 3.0
   elif(object == 'g'):
      return 5.3
   elif(object == 'l'):
      return 9.07
   else:
      return 0.0

 #return the velocity of the object
def getVelocityObject(distance):
   velocityObject = math.sqrt((9.8*distance)/2)
   return velocityObject

#return the velocity of the skater
def getVelocitySkater(massSkater, massObject, velObject):
   velocitySkater = (massObject*velObject)/(massSkater)
   return velocitySkater




