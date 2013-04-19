from Queue import PriorityQueue
import sys

def graphBuild():
    
    edge = []
    edges = []
    
    inputGraph = open(sys.argv[1], "r").readlines()
    
    for line in inputGraph:
        line = line.rstrip()
        edge = line.split(" ")
        edges.append(edge)
        
    for record in edges:
        record.append('UP')
    
    return edges

initialGraph = graphBuild()

def verticesList():
        
        ver = []
        vers = []
        
        for record in initialGraph:
            if record[0] not in ver or record[1] not in ver:
                if record[0] not in ver:
                    ver.append(record[0])
                    continue
                else:
                    ver.append(record[1])
            else:
                continue
        
        for record in ver:
            vers.append([record,'UP'])
            
        return vers

def call():
    return 0

verList = verticesList()
edgList = initialGraph

print verList
print edgList



"""print
path Belk Education
edgedown Health Education
path Health Education
vertexdown Belk
path Health Education
print
reachable
edgeup Health Education 
vertexup Belk
deleteedge Duke Education
path Belk Education
path Education Belk
addedge Education Atkins 0.25
addedge Woodward Education 0.6
path Belk Atkins
print"""

def output():
    
    queries = inputGraph = open(sys.argv[2], "r").readlines()
    
    for line in queries:
        query = line.split(" ")
        if query[0] == 'print':
            print printGraph()
        elif query[0] == 'path':
            print path(query)
        elif query[0] == 'reachable':
            print reach()
        elif query[0] == 'vertexup':
            call()
        elif query[0] == 'vertexdown':
            call()
        elif query[0] == 'edgeup':
            call()
        elif query[0] == 'edgedown':
            call()
        elif query[0] == 'addedge':
            call()
        else:
            call()

def printGraph():
    return 0

def path(input):
    
    source = input[1]
    destination = input[2]
    vertexQueue = PriorityQueue()
    vertexQueue.put(source)

def reach():
    return 0