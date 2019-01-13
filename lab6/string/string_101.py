def str_rot_13(word):
   encryption = ""
   for i in word: 
      ascii = ord(i)
      if(i.isalpha):
         if(i.isupper()):
            ascii+=13
            if(ascii > 90):
               diff = ascii-90
               encrpt = chr(64+diff)
            else:
               encrypt = chr(ascii) 
         else:
            ascii+=13
            if(ascii > 122):
               diff = ascii-122
               encrypt = chr(96+diff)
            else:
         	   encrypt = chr(ascii)
      else:
         print("You have entered in an invalid character")
      encryption += encrypt

   return encryption


def str_translate_101(word, a, b):
   translated = ""
   for i in word: 
      if(i == a):
         translated+=str(b)
      else:
         translated+=str(i)
   return translated
   