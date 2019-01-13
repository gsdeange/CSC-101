
def listmaker(num):
   zeros = [0]*num
   return zeros
 
def check_valid(puzzle, cages):
   checkcages = check_cages_valid(puzzle, cages)
   checkcolumns = check_columns_valid(puzzle)
   checkrows = check_rows_valid(puzzle)
   if(checkcages and checkcolumns and checkrows):
      return True
   else: 
      return False
def check_cages_valid(puzzle, cages):
   spots = sum(puzzle, [])
   for i in cages:
      zeros = 0
      total = int(i[0])
      cellnum = int(i[1])
      cagesum = 0
      for spot in i[2:]:
        cagesum+=spots[spot]
        if(spots[spot] == 0):
           zeros+=1
		   
      if(zeros > 0):
         if(cagesum >= total):
            return False
      else:
         if(cagesum != total):
            return False 

   return True
	     
def check_columns_valid(puzzle):
   tempList = []
   tempList1 = []
   tempList2 = []
   tempList3 = []
   tempList4 = []
   tempList5 = []
   for i in puzzle: 
      tempList1.append(i[0])
      tempList2.append(i[1])
      tempList3.append(i[2])
      tempList4.append(i[3])
      tempList5.append(i[4])
   #print(len(i))
      
   tempList.append(tempList1)
   tempList.append(tempList2)
   tempList.append(tempList3)
   tempList.append(tempList4)
   tempList.append(tempList5)
   
   for i in tempList:
      for x in range(0,5): 
         num = i[x]
         if(i.count(num) > 1 and num > 0):
            return False
   return True
   
def check_rows_valid(puzzle):
   for i in puzzle:
      for x in range(0, 5):
         num = i[x]
         if(i.count(num) > 1 and num > 0):
            return False
   return True
         
def get_cages():
   cages = []
   cagenum = int(input("Number of cages: "))
   for i in range(cagenum):
      print("Cage number", i, ":", end='')
      response = input().split()
      #response[0] = string(response[0])
      #print(response)
      #response = iresponse))
      response = [int(x) for x in response]
      cages.append(response)
      
   return cages
 