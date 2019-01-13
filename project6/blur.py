#blur.py
import sys
import copy
def command_args():
   output = []
   blur = 4
   if(len(sys.argv) < 2):
      print("Usage python blur.py <image> <OPTIONAL: reach>")
      imgname = ""
      exit()
   elif(len(sys.argv) >= 2):
      imgname = sys.argv[1]
      try: 
          if(len(sys.argv) == 3):
            blur = int(sys.argv[2])
          imgfile = open(imgname, 'r')
      except: 
         print("Unable to open <", imgname,">")
         imgname = ''
         exit()
   output.append(imgname)
   output.append(blur)
   return output

class Pixel():
   def __init__(self, r, g, b, x, y):
      self.r = r
      self.g = g
      self.b = b
      self.x = x
      self.y = y
   def __eq__(self, other):
      return self.r == other.r and self.g == other.g and self.b == other.b
   def __str__(self):
      return ""+str(self.r)+""+str(self.g)+""+str(self.b)
def blur():
   pixelList = []
   commandlist = []
   commandlist = command_args()
   name = commandlist[0]
   imgfile = open(name, 'r')
   blur = commandlist[1]
   #print(blur)

   lines = imgfile.readlines()
   #make a list of lists with each one containing the rgb values
   rgbList = copy.deepcopy(lines[3:])
   rgbList = list([rgbList[x:x+3] for x in range(0, len(rgbList), 3)])

   file = open("blurred.ppm", "w")
   file.write(str(lines[0]))
   file.write(str(lines[1]))
   file.write(str(lines[2]))

   rows = 0 
   columns = 0
   coordinates = lines[1].split()
   width = int(coordinates[0])
   height = int(coordinates[1])

   for i in rgbList:
      columns+=1
      if(columns>=int(coordinates[0])):
         rows+=1
         columns = 0
      #pixel = PixelList()
      pixel = Pixel(i[0], i[1], i[2], columns, rows)
      pixelList.append(pixel)
      #
      
   for pixel in pixelList:
      x = pixel.x
      y = pixel.y
      minx = max(0, x-blur)
      maxx = min(width-1, x+blur)
      miny = max(0, y-blur)
      maxy = min(height-1, y+blur)

      rtotal = 0
      gtotal = 0
      btotal = 0
      count = 0

      for row in range(miny, maxy+1):
         for col in range(minx, maxx+1):
            index = row*width+col
            tempPixel = pixelList[index]
            rtotal = rtotal+int(tempPixel.r)
            gtotal = gtotal+int(tempPixel.g)
            btotal = btotal+int(tempPixel.b)
            count+=1

      raverage = (rtotal/count)
      gaverage = (gtotal/count)
      baverage = (btotal/count)
      file.write(str(int(raverage))+'\n'+str(int(gaverage))+"\n"+str(int(baverage))+"\n")

def main():
   blur()

if __name__ == '__main__':
   main()