def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    bTuple = ()
    for index in range(len(aTup)):
        if not index % 2:
            bTuple += aTup[index:index+1]
    return bTuple

print oddTuples(('I', 'am', 'a', 'test', 'tuple'))