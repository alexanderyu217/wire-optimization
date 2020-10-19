import sys
import utils
import classes
import search

args = (sys.argv)[1:]
flags = {"-ind":1, "-bulk":0}
err = "Please use the formats: -ind -[search type] [filepath to chassis]"\
        + " [start node] [end node]; -bulk -[search type] [filepath to chassis]"\
        + " [filepath to input sheet]"
err2 = "Make sure you follow input conventions"

try:
    chassis = classes.Chassis(args[2])
    search_agent = search.SearchAgent(chassis)
    search_types = {"-dijkstra": search_agent.dijkstra}
    search_algo = search_types[args[1]]
except:
    print(err)
       
if flags[args[0]]:
    try:
        start = classes.Node.node(args[3])
        goal = classes.Node.node(args[4])
        path = search_algo(start, goal)
        print("\n",path)
        print("Length: ", search_agent.path_dist(path),"\n")
    except:
        print(err)
else:
    try:
        inputs = utils.get_data(args[3])
    except:
        print(err)
    try:
        print("---------------------")
        for row in inputs:
            if row[0] != "Wire Name":
                name = row[0]
                start = classes.Node.node(row[1])
                goal = classes.Node.node(row[2])
                path = search_algo(start, goal)
                print("---------------------")
                print(name)
                print("\n",path,"\n")
                print("Length: ", search_agent.path_dist(path))
                print("---------------------")
        print("---------------------")
    except:
        print(err2)
