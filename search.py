from classes import*
from utils import*

class SearchAgent:
    """
    Search agent responsible for generating efficient wire paths.
    """
    def __init__(self, chassis):
        self.chassis = chassis

    def dijkstra(self, start, goal):
        """
        Finds the shortest length path from start to goal
        """
        explored = {None}
        fringe = PriorityQueue([[start, 0]])
        parents = {}
        dist = {start: 0}
        while not fringe.is_empty():
            node = fringe.pop()
            if node not in explored:
                if node == goal:
                    path = self.gen_path(parents, goal)
                    return path
                explored.add(node)
                succs = self.chassis.successors(node)
                for succ in succs:
                    target = succ[1]
                    tube = succ[0]
                    if target not in explored:
                        if target in dist:
                            if dist[target] > dist[node] + tube.get_length():
                                dist[target] = dist[node] + tube.get_length()
                                parents[target] = (tube, node)
                        else:
                            parents[target] = (tube, node)
                            dist[target] = dist[node] + tube.get_length()
                        fringe.update(target, dist[target])
    
    def gen_path(self, parents, goal):
        path = []
        path.append(goal)
        while parents.get(goal):
            tube = parents[goal][0]
            node = parents[goal][1]
            path.append(tube)
            path.append(node)
            goal = node
        path.reverse()
        return path
    
    def path_dist(self, path):
        length = 0
        for item in path:
            if type(item) == Tube:
                length += item.get_length()
        return length
