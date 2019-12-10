#########
#Classes#
#########

class n_t(object):
    def __init__(self, node, tube = []):
        self.node = node
        self.tube = tube

    def __repr__(self):
        if self.tube:
            return self.node.name + ' --> ' + self.tube.name + ' --> '
        return self.node.name

class Tube(object):
    def __init__(self, name = 'empty', length = 0):
        self.name = name
        self.length = length

    def __repr__(self):
        return self.name+'({})'.format(self.length)

class Intersection(object):
    """The class for all nodes in the tube map. 
    Each intersection of the tubes is a node and each exit point is a node.
    """
    type = 'intersection'
    count = 0

    def __init__(self, name, connected_nodes=[]):
        for node in connected_nodes:
            assert isinstance(the_node(node), Intersection), \
                'Connected nodes must be is instances of the intersection class.'
            assert isinstance(tube_of_node(node), Tube), \
                'Tubes must be instances of tube class'
        self.name = name
        self.connected_nodes = []
        Intersection.count += 1

        # appends nodes in the connected_nodes list to self.connected_nodes #
        # if the node already exists, don't do anything #
        for node in connected_nodes:
            if node not in self.connected_nodes:
                self.connected_nodes.append(node)

        # makes sure current node is in each of its connected nodes' self.connected_nodes list#
        for node in self.connected_nodes:
            if n_t(self, tube_of_node(node)) not in the_node(node).connected_nodes:
                the_node(node).connected_nodes.append(n_t(self,tube_of_node(node)))

    def __repr__(self):
        return self.name

##############
#Constructors#
##############

def the_node(some_node_and_tube):
    return some_node_and_tube.node

def tube_of_node(some_node_and_tube):
    return some_node_and_tube.tube

def node_connect(node1, node2, tube):
    if n_t(node2, tube) not in node1.connected_nodes:
        node1.connected_nodes.append(n_t(node2, tube))
    if n_t(node1, tube) not in node2.connected_nodes:
        node2.connected_nodes.append(n_t(node1, tube))



