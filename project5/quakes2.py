import quakeFuncs
def main():
   earthquakes = []
   #read the file
   earthquakes = quakeFuncs.read_quakes_from_file("quakes.txt")
   #target = open("test_output.txt", 'w')
   #for i in earthquakes:
   #   string = " ", i.mag, " ", i.place, ' ', i.longitude, ' ', i.latitude, ' ', i.time
   #   target.write(str(string))
   #program loop
   i = 1
   while i > 0:
      print()
      #print the chart
      quakeFuncs.print_table(earthquakes)
      #print/get options
      choice = quakeFuncs.get_options()
      if(choice == 's' or choice == 'S'):
         #sort function
         sort = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ")
         earthquakes = quakeFuncs.sort(earthquakes, sort)
      elif(choice == 'f' or choice == "F"):
          #filter function
          filter = input("Filter by (m)agnitude or (p)lace? ")
          if(filter == 'm' or filter == 'M'):
             lowerbound = float(input("Lower bound: "))
             upperbound = float(input("Upper bound: "))
             earthquakes = quakeFuncs.filter_by_mag(earthquakes, lowerbound, upperbound)
          elif(filter == 'p' or filter == 'P'):
             search = input("Search for what string? ")
             earthquakes = quakeFuncs.filter_by_place(earthquakes, search)
      elif(choice == 'n' or choice == "N"):
          #new quakes options
          new = False
          json = quakeFuncs.get_json("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")
          for i in range(len(json['features'])):
             catch = False
             quake = quakeFuncs.quake_from_feature(json["features"][i])
             if not quake in earthquakes:
                earthquakes.append(quake)
                #catch = True
                new = True
                #print("bananfannannanannannana")
          if new:
             print("New quakes found!!!")

      elif(choice == 'q' or choice == "Q"):
          #quit function
         quakeFuncs.quit(earthquakes, "quakes.txt")
         exit()

if __name__ == '__main__':
   main()