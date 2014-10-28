# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    print atMe.myName()
    print newFrob.myName()
    if newFrob.myName() > atMe.myName():
        if atMe.getAfter():
            print 'ma:  ' + atMe.getAfter().myName()
            if newFrob.myName() > atMe.getAfter().myName():
                insert(atMe.getAfter(), newFrob)
                print 'jest'
        else: 
            newFrob.setBefore(atMe)
            atMe.setAfter(newFrob)
    else:
        print 'mniejsze'
        newFrob.setAfter(atMe)
        atMe.setBefore(newFrob)


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
#insert(ruth, martha)
print 'Test:'
for a in (eric, andrew, ruth, fred,  martha):
    before = 'none'
    after = 'none'
    if a.getBefore():
        before = a.getBefore().myName()
    if a.getAfter():
        after = a.getAfter().myName()
    print a.myName() + " Before: " + before + " After: " + after
    
