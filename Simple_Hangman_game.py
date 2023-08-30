
#Simple hangman Game

import random

listword=["eman","aya","ibithal","azoz"]

choic_name=random.choice(listword)
#aprint(choic_name)
length= len(choic_name)
 
blanck=[]
for i in range(length):
    blanck +="_"

print (*blanck)
numtry=10


while numtry>0 and "_" in blanck:
  tryletter=input("enter any letter:")
  if tryletter in choic_name:
    for i in range(length):
        if choic_name[i] == tryletter:
            blanck[i] = tryletter
        print(*blanck)
        if ("_" not in  blanck):
           print("done")
           

  else :
   numtry-=1
   if numtry==0:
       print("faild")
    

   
    
    

   
 




  

