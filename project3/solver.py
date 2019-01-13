import solverFuncs
puzzle = []
cages = []

def main():
   #gets the number of cages/information
   cages = solverFuncs.get_cages()
   #print(cages)
   
   #create the default puzzle list
   for i in range(5):
      puzzle.append(solverFuncs.listmaker(5))

   backtracks = 0 
   x = 0
   row = 0
   col = 0
   checks = 0
   puzzle[0][0] = 0
   while (row < 5):	 
      puzzle[row][col]+=1
      checks+=1
      if(solverFuncs.check_valid(puzzle, cages)):
         if(col < 4):  
            col += 1
         else:
            col = 0
            row+=1
         
      elif(puzzle[row][col] == 5):
         #check to see if you need to backtrack
         while(puzzle[row][col] == 5):
		    #backtrack
            backtracks+=1
            puzzle[row][col] = 0
            #if(col > 0):
            col = col-1
            if(col < 0):
               row = row-1
               col = 4
		 
      # puzzle[row][col]+=1
   #print(cages)
   print()
   print("---Solution---")
   print()
   for i in puzzle:
      for x in range(0, 5):
         print(i[x],'', end='')
      print()

   print("checks: ", checks, " backtracks: ", backtracks)	  
             
      
 
   
if __name__ == "__main__":
    main()