class PriorityQueue:
    """
    An implementation of the priority queue.
    """

    def __init__(self):
        self.data = []
    
    def push(self, data, priority):
        if self.is_empty():
            self.data.append([data, priority])
        else:
            for i in range(len(self.data)):
                if priority < self.data[i][1]:
                    self.data.insert(i, [data, priority])
                    return

    def pop(self):
        return self.data.pop(0)[0]

    def is_empty(self):
        return not len(self.data)

    def top(self):
        return self.data[0][0]