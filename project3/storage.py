#loop tests storage

   for i in puzzle:
      for x in i: 
         i[x] = 1
         if(solverFuncs.check_valid(puzzle, cages)):
            x+=1
         else:
            backtracks+=1
            i[x] = 0
            if x > 0:
               i[x-1] +=1
			   
			   
			   
  for  i in puzzle:
      for x in i
      i[0] = 1
      x = 0
      while(solverFuncs.check_cages_valid(puzzle, cages)):
         x+=1
         if(x <= 4):
            i[x] = i[x]+1
      i[x] = 0
      x-=1
      if(x <= 4):
         i[x] = i[x]+1