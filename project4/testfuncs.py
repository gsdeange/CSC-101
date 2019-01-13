import funcs
def listmaker(num):
   zeroes = [0]*num
   return zeroes

def get_puzzle(string):
   puzzleList = []
   for j in range(10):
      puzzleList.append(listmaker(10))
   count = 0
   i = 0
   while i < (len(puzzleList)):
      for x in range(len(puzzleList[i])):
         puzzleList[i][x] = string[count]
         count+=1
         if(count%10 == 0):
            i+=1
   return puzzleList
def make_columns(puzzle):
   tempList = []
   tempList1 = []
   tempList2 = []
   tempList3 = []
   tempList4 = []
   tempList5 = []
   tempList6 = []
   tempList7 = []
   tempList8 = []
   tempList9 = []
   tempList9 = []
   tempList10 = []
   for i in puzzle: 
      tempList1.append(i[0])
      tempList2.append(i[1])
      tempList3.append(i[2])
      tempList4.append(i[3])
      tempList5.append(i[4])
      tempList6.append(i[5])
      tempList7.append(i[6])
      tempList8.append(i[7])
      tempList9.append(i[8])
      tempList10.append(i[9])  
   tempList.append(tempList1)
   tempList.append(tempList2)
   tempList.append(tempList3)
   tempList.append(tempList4)
   tempList.append(tempList5)
   tempList.append(tempList6)
   tempList.append(tempList7)
   tempList.append(tempList8)
   tempList.append(tempList9)
   tempList.append(tempList10)
   return tempList

def main():
   test = get_puzzle("WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU")
   print(make_columns(test))
if __name__ == '__main__':
   main()