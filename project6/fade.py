import copy
import sys
import math

def command_args():
   if(len(sys.argv) < 4):
      print("Usage python fade.py <image> <row> <column> <radius>")
      imgname = ""
      exit()
   elif(len(sys.argv)== 5):
      imgname = sys.argv[1]
      try: 
         imgfile = open(imgname, 'r')
      except: 
         print("Unable to open <", imgname,">")
         imgname = ''
         exit()
   return imgname

class Pixel():
   def __init__(self, r, g, b):
      self.r = r
      self.g = g
      self.b = b
   def __eq__(self, other):
      return self.r == other.r and self.g == other.g and self.b == other.b
   def __str__(self):
      return ""+str(self.r)+""+str(self.g)+""+str(self.b)

def fade():
   name = command_args()
   imgfile = open(name, 'r')
   inputrows = sys.argv[2]
   inputcolumns = sys.argv[3]
   radius = int(sys.argv[4])

   pixelList = []
   

   lines = imgfile.readlines()
   #make a list of lists with each one containing the rgb values
   rgbList = copy.deepcopy(lines[3:])
   rgbList = list([rgbList[x:x+3] for x in range(0, len(rgbList), 3)])

   file = open("faded.ppm", "w")
   file.write(str(lines[0]))
   file.write(str(lines[1]))
   file.write(str(lines[2]))

   rows = 0
   columns = 0
   coordinates = lines[1].split()

   for i in rgbList:
      pixel = Pixel(i[0], i[1], i[2])
      #modify the pixel or pixels
      # have 2 variables, row and column, that start at zero and with each pixel are incremented 
      # read in the height and width of the picture and when the columns reach the max, increment the 
      #rows and then set the columns back to 0
      #
      columns+=1
      if(columns>=int(coordinates[0])):
         rows+=1
         columns = 0
      distance = get_distance(int(rows), int(columns), int(inputrows), int(inputcolumns))
      scale = (radius-distance)/radius
      if(scale < 0.2):
         scale = 0.2
      pixel.r = int(pixel.r)*scale
      pixel.g = int(pixel.g)*scale
      pixel.b = int(pixel.b)*scale
       


      file.write(str(int(pixel.r))+'\n'+str(int(pixel.g))+"\n"+str(int(pixel.b))+"\n")
      pixelList.append(pixel)

def get_distance(x1, y1, x2, y2):
	return math.sqrt(((y2-y1)**2)+(x2-x1)**2)

def main():
	fade()

if __name__ == '__main__':
   main()