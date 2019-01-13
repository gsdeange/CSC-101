def is_lower_101(character):
   if(97 <= ord(character) <= 122):
      return True
   else:
   	  return False

def char_rot_13(character):
   ascii = ord(character)
   if(character.isalpha):
      if(character.isupper()):
         ascii+=13
         if(ascii > 90):
            diff = ascii-90
            encryption = chr(65+diff)
         else:
            encryption = chr(ascii) 
      else:
         ascii+=13
         if(ascii > 122):
            diff = ascii-122
            encryption = chr(97+diff)
         else:
         	encryption = chr(ascii)
   else:
      print("You have entered in an invalid character")
   return encryption