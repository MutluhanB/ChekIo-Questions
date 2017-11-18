import string
def correct_sentence(a):
    if a[-1] != "." :
      text =a+"{x}".format(x=".") 
    else :
      text=a
    return text.capitalize()