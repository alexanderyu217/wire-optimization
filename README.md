# Wire Path Optimization Project

## inputs:
1. upload a chassis data sheet under the chassis folder and follow the proper input conventions. See B20 for sample
2. for bulk pathfinding, upload an input data sheet under the paths folder and follow proper input conventions. see wire_input.xlsx for sample

## commands:
 1. individual paths:
     `python3 run.py -ind -[search type] [filepath to chassis] [start node] [end node]`
 2. bulk pathfinding:
     `python3 run.py -bulk -[search type] [filepath to chassis] [filepath to input sheet]`

## saving wire paths:
 - add a `> [output destination]` after the command to save the file path(s)