#groups.py
def groups_of_3(list):
   return [list[x:x+3] for x in range(0, len(list), 3)]  
def main():
   list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
   list = groups_of_3(list)
   print(list)
if __name__ == '__main__':
   main()