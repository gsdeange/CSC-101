import funcs
def main():
   #take in the string
   string = input()
   print()
   puzzle = funcs.get_puzzle(string)
   #get the search words
   searchwords = funcs.get_words()
   print("   Puzzle: ")
   print()
   for i in range(len(puzzle)):
         rowstring = ''.join(puzzle[i])
         print(rowstring)



   #print(searchwords)
   #print("The words found are:")
   print()
   for i in searchwords:
      index = funcs.check_all(puzzle, i)
      if(index != 0):
         print(i,":" "word not found")
         #print("word: ", i, "row: ",  "column: ", index)

   
if __name__ == '__main__':
   main()



 

  






