numList = []
def sum(numList):
   sum = 0
   for i in numList:
      sum+=i
   return sum
def index_of_smallest(numList):
   if(len(numList) <= 0):
      return -1
   smallest = numList[0]
   smallindex = 0
   for i in range(len(numList)):
      if(numList[i] < smallest):
         smallest = numList[i]
         smallindex = i

   return smallindex
