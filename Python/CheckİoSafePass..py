"""
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.
"""
#%%

def checkio(data) : 
   UzunlukCheck=False 
   DigitCheck= False
   UpperCheck= False
   LowerCheck= False
   textlistlow = []
   textlistup = []
   textlistdig = []
   Digits="0123456789"
   lowercase="abcdefghijklmnopqrstuvwxyz"
   uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  
   if len(data) >= 10 :
        UzunlukCheck =True
   for i in range (len(data)) :
        textlistdig.append(data[i]) 
        if textlistdig[i] in Digits : 
          DigitCheck = True 
   for k in range (len(data)) :
        textlistlow.append(data[k]) 
        if textlistlow[k] in lowercase :
          LowerCheck= True
   for l in range (len(data)) :
        textlistup.append(data[l])
        if textlistup[l] in uppercase :
          UpperCheck = True
   
   if DigitCheck == True and UzunlukCheck == True and LowerCheck == True and UpperCheck == True :
       return True
   else :
       return False
   

    
    

 
 
    
            
    
