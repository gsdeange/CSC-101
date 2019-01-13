import sys
def main():
   flagsum = False
   filename = ''
   flag = ''
   try:

      if(len(sys.argv) == 2):
         filename = sys.argv[1]

      elif(len(sys.argv)==3):
         if(sys.argv[2] == "-s"):
            flag = sys.argv[2]
            filename = sys.argv[1]
            flagsum = True
         elif(sys.argv[1] == '-s'):
            flag = sys.argv[1]
            filename = sys.argv[2]
            flagsum = True
         elif(system.argv[2] != '-s'):
            flag = system.argv[2]
      
      file = open(filename, 'r')
   except:
      if(len(sys.argv) == 1):
         print('Usage: [-s] file_name')
      elif(len(sys.argv) == 3):
         if(flag!='-s'):
            print('Usage: [-s] file_name')
            exit()
            
      else:
         print("Unable to open [", filename, ']')
      exit()
     
   lines = file.readlines()
   ints = 0
   floats = 0
   other = 0
   sums = 0
   for i in lines:
      for x in i.split():
         if x.isdigit():
            ints+=1
            sums+=int(x)
         else:
         	try:
         	   float(x)
         	   floats+=1
         	   sums +=float(x)
         	except:
         	   other+=1
         	   
   print("Ints: ", ints)
   print("Floats: ", floats)
   print("Other: ", other)
   if(flagsum):
      print("Sum: ", sums)
 
if __name__ == '__main__':
   main()
   