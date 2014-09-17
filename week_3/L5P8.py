
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    print aStr
    if len(aStr) == 0:
        return False
    elif len(aStr) == 1:
        return (aStr == char)
    else:
        #c = aStr[int(len(aStr)/2): int(len(aStr)/2+1)]
        c = aStr[int(len(aStr)/2)]
        if c == char:
            return True
        elif c > char:
            return isIn(char, aStr[:int(len(aStr)/2)])
        else:
            return isIn(char, aStr[int(len(aStr)/2):])


#print isIn('m', 'ccdmpw')
print isIn('k', 'klnnoorvz')