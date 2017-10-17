import sys
from Structures import Graph
from Launch import Launch
from Problem import Problem
from TreeSearch import *
from GraphSearch import *
from datetime import datetime

if len(sys.argv) != 3:
    print("Invalid number of arguments.")
    exit(0)
    
agent_mode = sys.argv[1]
file_path = sys.argv[2]

item_list = []
link_list = []
launch_list = []

launches = []
graph = Graph()

with open(file_path, 'r') as f:
    for line in f.read().splitlines():
        if line == '':
            continue
        lineType = line[0]
        line = line.split(" ")
        
        if lineType == 'V':
            item_list.append([line[0], float(line[1])])
        elif lineType == 'E':
            link_list.append([line[1], line[2]])
        elif lineType == 'L':
            launch_list.append([datetime.strptime(line[1],'%d%m%Y'), float(line[2]), float(line[3]), float(line[4])])
         
for item in item_list:
    graph.addItem(item[0], item[1])
    
for link in link_list:
    graph.addLink(link[0], link[1])
    
for launch in launch_list:
    launches.append(Launch(launch[0], launch[1], launch[2], launch[3]))  

launches = sorted(launches, key=lambda launch: launch.date)

problem = Problem(graph, launches)
result = graph_uniform(problem)

if result == 'cut':
    print(result)
elif result:
    for node in result.getPath():
        print("L" + str(node.state["LaunchNr"]) + ": " + node.action + " : " + str(node.state["Weight"]))
    print(result.cost)
else:
    print('FAILED')