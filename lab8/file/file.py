file = open("in.txt", "r")
count = 0
for line in file:
   print("Line", count, "(", len(line), "chars): ", line, end="")
   count+=1
print()