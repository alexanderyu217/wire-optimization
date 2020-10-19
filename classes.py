from utils import*

class Chassis:
    """
    A Chassis object represents one chassis. 
    Edges incident to vertices are stored as (tube, other vertex) sets in a dictionary
    """

    def __init__(self, file, name = "Chassis"):
        """
        The chassis is initalized with all the edges given in spreadsheet FILE.
        name: string
        file: string
        """
        data = get_data(file)
        self.edges = {}
        for i in range(len(data)):
            row = data[i]
            if row[0] == "#":
                pass
            else:
                assert len(row) == 4\
                ,"Please follow input convention. See row {} of {}".format(i, file)
                node1 = row[0]
                tube = row[1]
                tube_length = row[2]
                node2 = row[3]
                self.connect(Node.node(node1), \
                    Tube.tube(tube, tube_length), Node.node(node2))

    def connect(self, node1, tube, node2):
        """
        Connects NODE1 and NODE2 with TUBE.
        node1 and node2: Node objects
        tube: Tube object
        """
        if not self.edges.get(node1):
            self.edges[node1] = {(tube, node2)}
        else:
            self.edges[node1].add((tube, node2))
        if not self.edges.get(node2):
            self.edges[node2] = {(tube, node1)}
        else:
            self.edges[node2].add((tube, node1))
    
    def successors(self, node):
        """
        Finds and returns a list of all (tube, node) edges adjacent to NODE.
        """
        succ = self.edges.get(node)
        if succ:
            return list(succ) 

class Tube:
    """
    The class to represent the tubes of the car chassis
    """

    all = {}

    def __init__(self, name = 'empty', length = 0):
        self.name = name
        self.length = length
        Tube.all[name] = self
    
    def tube(name, length):
        if not Tube.all.get(name):
            Tube(name, length)
            return Tube.all.get(name)
        else:
            return Tube.all.get(name)

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

    all = {}

    def __init__(self, name):
        self.name = name
        Node.all[name] = self

    def node(name):
        if not Node.all.get(name):
            Node(name)
            return Node.all.get(name)
        else:
            return Node.all.get(name)

    def __repr__(self):
        return self.name
    