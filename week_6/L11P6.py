class Queue(object):
    
    def __init__(self):
        self.vals = []

    def insert(self, e):
        self.vals.append(e)
    
    def remove(self):
        try:
            return self.vals.pop(0)
        except:
            raise ValueError('Empty queue')
        

queue = Queue()
queue.insert(5)
queue.insert(6)
print queue.remove()
queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()
