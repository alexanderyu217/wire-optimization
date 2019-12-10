#########
#Imports#
#########

from Backend.B20_tube_layout import*
from Backend.xClass import*

##############
#Node Options#
##############

print_string = 'Type in your desired node. Specify left and Right. Ex: Left a -> a_l, Right a -> a_r'

###########
#Functions#
###########

def path_gen(start_node,end_node, count = 0):
    if start_node == end_node:
        yield[n_t(end_node)]
    count += 1
    for sub_pack in start_node.connected_nodes:
        if the_node(sub_pack) and count <= 10:
            for steps in path_gen(the_node(sub_pack), end_node, count):
                paths = [n_t(start_node, tube_of_node(sub_pack))]
                paths.extend(steps)
                yield paths

def path_dis(path):
    distance = 0
    for pack in path:
        if tube_of_node(pack):
            distance += tube_of_node(pack).length
    return distance

####
#UI#
####

while True:
    final_paths = []
    start_node = node_dictionary[str(input('\nStarting node?\n'+print_string+'\n'))]        #Obtaining starting node
    end_node = node_dictionary[str(input('\nEnding node?\n'+print_string+'\n'))]            #Obtaining ending node
    list_of_paths = list(path_gen(start_node,end_node))                 #Generating paths from start_node to end_node
    for path in list_of_paths:                                          #Adds the length of each path to the path
        path.append(path_dis(path))
    disp_type = int(input('\nWhat would you like the path to be optimized by?\n0)Wire Length   1)Number of Tubes Travelled Through\n'))
    if disp_type == 0:
        min_distance = min([path[-1] for path in list_of_paths])
        print('_____________________\nPath: {} to {}'.format(start_node,end_node))
        print('The following path will require wire of length {} inches:'.format(min_distance))
        for path in list_of_paths:
            if path[-1] == min_distance:
                print('\n',path[:-1])
        print('_____________________')
    elif disp_type == 1:
        min_tubes = min([len(sub_path) for sub_path in list_of_paths])
        print('_____________________\nPath:{} to {}'.format(start_node,end_node))
        print('The following paths travel through {} tubes:'.format(min_tubes-2))
        for path in list_of_paths:
            if len(path) == min_tubes:
                print("\n{} inches:".format(path[-1]),path[:-1])
        print('_____________________')