# Wire Path Optimization Project
 
As a member of Berkeley's Formula Racing team, I was tasked with the job of optimizing our process of laying out the wire harness of the car. Hours are lost from manually laying the wires out on previous cars for measurement. Having only 1 computer science course (CS61A at UC Berkeley), I utilized the concept of recursion and objected oriented programming that I learned in class to create this wire path optimization program. The program, depending on the tube chassis layout of the car, will determine the most efficient path for a wire to follow. The most efficient path can either follow the shortest path or the path of least tubes travelled through depending on user preference. 

Backend Files:

xClass.py 			
	- All the classes and constructors used in the program
	
B20_tube_layout.py 	
	- The specific layout of the tubes in our 2020 car chassis frame, modeled using the 		classes and constructors of xClass.py
	
	
Frontend Files:

Individual_Pathfinder.py
	- UI for selecting individual paths for the wire to follow

Bulk_Pathfinder.py
	-Program to optimize the path of all the listed paths in wire_input.xlsx

wire_output.txt
	-The output of the paths for the wires in wire_input.xlsx to follow
