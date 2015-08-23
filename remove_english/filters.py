__author__ = 'AmirPouya'
import re
def isArabic(seq):
    counter=0
    reg=re.compile(ur'[\u0627-\u0700]')
    return isLang(seq,reg)

def isFarsi(seq):
    return isArabic(seq)



def isLang(seq,regex):
    counter=0
    for char in seq:
        if(regex.match(char)):
            counter+=1
    if(counter>len(seq)/2):
        return True
    else:
        return False
