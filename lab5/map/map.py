def square_all(list):
   output = [x**2 for x in range(len(list))] 
   return output

def add_n_all(list, n):
   output = []
   i = 0
   while i < len(list):
      sum = list[i] + n
      output.append(sum)
      i+=1
   return output
def even_or_odd_all(list):
   output = []
   for i in range(len(list)):
      if(list[i]%2 == 0):
         list.append(True)
      else: 
         list.append(False)
   return output
   
      
   