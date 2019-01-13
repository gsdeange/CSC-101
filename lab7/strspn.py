def my_strspn(str1, str2):
   output = []
   count = 0
   for i in str1:
      if i in str2:
         count+=1
      else:
      	break    
   return count



def main():
   str1 = input("Enter in string 1: ")
   str2 = input("Enter in string 2: ")
   print(my_strspn(str1, str2))



if __name__ == '__main__':
   main()
