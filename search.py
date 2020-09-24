import classes

class SearchAgent:
    """
    Search agent responsible for generating efficient wire paths.
    """
    def __init__(self, chassis):
        self.chassis = chassis
    
    def bfs_unweighted(self, start, end):
        return []

    def dijkstra(self, start, end):
        return []
    
    def successors(self, node):
        """
        Finds and returns a list of all nodes adjacent to NODE.
        """
        adjacent = []
        for edge in self.chassis.edges:
            if node in edge:
                for elem in edge:
                    if (elem is not node) and not (type(elem) == classes.Tube):
                        adjacent.append(elem)
        return adjacent