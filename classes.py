class Chassis:
    """
    A Chassis object represents one chassis. 
    Edges are stored as a tuple of end nodes and their connecting tube.
    """

    def __init__(self, name = "", nodes = []):
        """
        The chassis is initalized with all the nodes, but none are connected.
        """
        self.nodes = nodes
        self.tubes = []
        self.edges = []

    def connect(self, node1, node2, tube):
        """
        Connects NODE1 and NODE2 with TUBE
        """ 
        self.edges.append((node1, node2, tube))

class Tube:
    """
    The class to represent the tubes of the car chassis
    """

    def __init__(self, name = 'empty', length = 0):
        self.name = name
        self.length = length
        Tube.all.append(self)

    def __repr__(self):
        return self.name+'({})'.format(self.length)

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length
        
class Node:
    """
    The class to represent tube intersections of the car chassis
    """

    def __init__(self, name):
        self.name = name
        Node.all.append(self)

    def __repr__(self):
        return self.name

    