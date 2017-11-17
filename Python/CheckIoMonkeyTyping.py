
""" 
Mutluhan Boz 17.11.2017
You are given some text potentially including sensible words. 
You should count how many words are included in the given text.
 A word should be whole and may be a part of other word. 
 Text letter case does not matter.
 Words are given in lowercase and don't repeat. 
 If a word appears several times in the text, it should be counted only once.
For example, text - "How aresjfhdskfhskd you?", words - ("how", "are", "you", "hello"). 
The result will be 3.
"""
def count_words(a,b) :
    count= 0 
    i = 0
    bl=list(b)
    a2=a.lower()
    while i < len(bl) :
        if bl[i] in a2 :
            count += 1 
        i += 1
    return count
    


