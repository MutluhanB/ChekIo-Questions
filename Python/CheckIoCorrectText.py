## Capitalize first letter of a given text and adds dot to the end. 18.11.17
import string
def correct_sentence(a):
    if a[-1] != "." :
      text =a+"{x}".format(x=".") 
    else :
      text=a
    return text.capitalize()
