from urllib.request import *
from json import *
from datetime import *
from operator import *

# GIVEN FUNCTIONS:
# Use these two as-is and do not change them
def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    
   
# Add Earthquake class definition here   
class Earthquake():
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time
   def __eq__(self, other):
      return self.place == other.place and self.mag == other.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == other.time
   def __str__(self):
      return " "+self.place+" "+str(self.mag)+" "+str(self.longitude)+" "+str(self.latitude)+" "+str(self.time)+" "
# Required function - implement me!   
def read_quakes_from_file(filename):
   earthquakes = []
   file = open(filename, "r")
   for line in file:
      input = [x for x in line.split()]
      input[4] = ' '.join(input[4:])
      quake = Earthquake(input[4], float(input[0]), float(input[1]), float(input[2]), int(input[3]))
      earthquakes.append(quake)
   #print(earthquakes[0].place)
   file.close()
   return earthquakes


def print_table(earthquakes):
   #print the table
   print("Earthquakes:")
   print("------------")
   for quake in earthquakes:
      time = time_to_str(int(quake.time))
      print("(", "%0.2f" %quake.mag, ")", "           ", quake.place, "at", time, "(", "%0.3f" %float(quake.longitude), ",", "%0.3f" %float(quake.latitude), ")" )
   print()

def get_options():
   print("Options:")
   print("  (s)ort")
   print("  (f)ilter")
   print("  (n)ew quakes")
   print("  (q)uit")
   print()
   #try:
   choice = input("Choice:")
   #except EOFError:
      #choice = input("Choice:")
   return choice

def sort(earthquakes, choice):
   sortedquakes = []
   if(choice == 'm' or choice == 'M'):
      sortedquakes = sorted(earthquakes, key=lambda quake: quake.mag)
      sortedquakes = sortedquakes[::-1]
      return sortedquakes
   elif(choice == 't' or choice == 'T'):
      sortedquakes = sorted(earthquakes, key=lambda quake: quake.time)
      sortedquakes = sortedquakes[::-1]
      return sortedquakes
   elif(choice == 'l' or choice == 'L'):
      sortedquakes = sorted(earthquakes, key=lambda quake: quake.longitude)
      return sortedquakes
   elif(choice == 'a' or choice == 'A'):
      sortedquakes = sorted(earthquakes, key=lambda quake: quake.latitude)
      return sortedquakes

# Required function - implement me!
def filter_by_mag(earthquakes, low, high):
   filterlist = []
   for quake in earthquakes:
      if(low <= float(quake.mag) <= high):
         filterlist.append(quake)
   return filterlist

# Required function - implement me!
def filter_by_place(earthquakes, word):   
   filterlist = []
   #print(earthquakes)
   for quake in range(len(earthquakes)):
      if word.lower() in earthquakes[quake].place.lower() or word.upper() in earthquakes[quake].place.upper():
         filterlist.append(earthquakes[quake])
   
   return filterlist

# Required function for final part - implement me too!   
def quake_from_feature(feature):
   mag = feature['properties']['mag']
   place = feature['properties']['place']
   time = int(feature['properties']['time']/1000)
   longitude = feature['geometry']['coordinates'][0]
   latitude = feature['geometry']['coordinates'][1]
   quake = Earthquake(str(place), float(mag), float(longitude), float(latitude), int(time))
   return quake
def quit(earthquakes, filename):
   file = open(filename, "w")
   for quake in earthquakes:
      file.write(str(quake.mag)+' '+str(quake.longitude)+' '+str(quake.latitude)+' '+str(quake.time)+' '+str(quake.place)+"\n")
      #file.write("\n")


      



     


   