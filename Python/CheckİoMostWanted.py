def checkio(text):
## returns most repeated letter
    charList='abcdefghijklmnopqrstuvwxyz' # Chars to find
    text=text.lower()                     # Setting text to low chars
    
    # Looping chars
    i=0         # index
    total=0     # Total chars found
    mainChar='' # Char most repeated
    while i<len(charList) and total<len(text):
        char=charList[i]
        i+=1
        counts=text.count(char)
        total+=counts
        if (mainChar == '' or counts > maxRepeats):
            mainChar=char
            maxRepeats=counts

    return mainChar


print(checkio("Mutluhan Boz"))
