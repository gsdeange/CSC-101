def are_positive(list):
   output = []
   i = 0
   while i < len(list):
      if(list[i] > 0)
         output.append(i)
      i+=1
   return output	
def are_greater_than_n(list, n):
   output = []
   for i in range(len(list)):
         if(list[i] > n):
		    output.append(i)
   return output
def are_divisible_by_n(list, n):
   output = [x for x in range(len(list)) if x%n == 0]
   return output