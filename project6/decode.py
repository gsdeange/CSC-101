#decode.py
import copy
import sys

def command_args():
   if(len(sys.argv)==1):
      print("Usage python decode.py <image>")
      exit()
   elif(len(sys.argv)==2):
      imgname = sys.argv[1]
      try: 
         imgfile = open(imgname, 'r')
      except: 
         print("Unable to open <", imgname,">")
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
def decode():
   pixelList = []
   imgname = command_args()
   imgfile = open(imgname, 'r')

   lines = imgfile.readlines()
   rgbList = copy.deepcopy(lines[3:])
   rgbList = list([rgbList[x:x+3] for x in range(0, len(rgbList), 3)])
   #rgbList = rgbList[:-1]

   file = open("decoded.ppm", "w")
   file.write(str(lines[0]))
   file.write(str(lines[1]))
   file.write(str(lines[2]))

   for i in rgbList:
      pixel = Pixel(i[0], i[1], i[2])
      pixel.r = int(pixel.r)*10
      if(pixel.r > 255):
         pixel.r = 255
         pixel.g = 255
         pixel.b = 255
      else:
         pixel.g = pixel.r
         pixel.b = pixel.r
      file.write(str(pixel.r)+'\n'+str(pixel.g)+"\n"+str(pixel.b)+"\n")
      pixelList.append(pixel)

   

   #for i in pixelList:
    #  i[0] = int(i[0])*10
      #print(i[0])
      #print(i[2])
    #  if(i[0]>=255):
   #      i[0] = 255
         
    #  i[1] = i[0]
     # i[2] = i[0]
      
 #  print(pixelList)
   #combine pixel list back together
   #print(len(pixelList))
   #spots = sum(pixelList, [])
   #outputList.append(spots)
   #file = open("decoded.ppm", "w")
   #file.write(str(lines[0]))
   #file.write(str(lines[1]))
   #for i in pixelList:
   #   file.write(str(i[0])+"\n")
   #   file.write(str(i[1])+"\n")
   #   file.write(str(i[2])+"\n")

   #print(outputList)

def main( ):
   decode()
if __name__ == '__main__':
   main()




   



