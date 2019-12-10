#########
#Imports#
#########

from Backend.B20_tube_layout import*
from Backend.xClass import*
from xlrd import*

#####################
#Optimization Method#
#####################

disp_type = int(input('\nWhat would you like the path to be optimized by?\n0)Wire Length   1)Number of Tubes Travelled Through\n'))

########################################
#Source Spreadsheet and Output txt File#
########################################

xl_in = open_workbook('wire_input.xlsx')
worksheet = xl_in.sheet_by_index(0)
output = open('wire_output.txt', 'w+')

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

for row in range(worksheet.nrows):
    if row != 0:
        print(str(worksheet.cell_value(row,0)))
        final_paths = []
        start_node = node_dictionary[str(worksheet.cell_value(row,1))]            #Obtaining starting node
        end_node = node_dictionary[str(worksheet.cell_value(row,2))]        #Obtaining ending node
        list_of_paths = list(path_gen(start_node,end_node))                 #Generating paths from start_node to end_node
        for path in list_of_paths:                                          #Adds the length of each path to the path
            path.append(path_dis(path))

        if disp_type == 0:
            min_distance = min([round(path[-1],2) for path in list_of_paths])
            output.write('_____________________\n{} Path: {} to {}'.format(str(worksheet.cell_value(row,0)),start_node,end_node))
            output.write('\nThe following path will require wire of length {} inches:'.format(min_distance))
            for path in list_of_paths:
                if round(path[-1],2) == min_distance:
                    output.write('\n\n{}'.format(path[:-1]))
            output.write('\n_____________________\n\n\n')
        elif disp_type == 1:
            min_tubes = min([len(sub_path) for sub_path in list_of_paths])
            output.write('_____________________\n{} Path:{} to {}'.format(str(worksheet.cell_value(row,0)),start_node,end_node))
            output.write('\nThe following paths travel through {} tubes:'.format(min_tubes-2))
            for path in list_of_paths:
                if len(path) == min_tubes:
                    output.write("\n\n{} inches: {}".format(round(path[-1],2),path[:-1]))
            output.write('\n_____________________\n\n\n')

print('\n\nDONE!\n\n')