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
        edges.append([edge[1],edge[0],edge[2]])
        
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

#print verList
#print edgList

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
    
    queries = open(sys.argv[2], "r").readlines()
    input = []
    
    for line in queries:
        line = line.rstrip()
        input.append(line)
    
    for line in input:
        line = line.split(" ")
        if line[0] == 'print':
            print printGraph()
        elif line[0] == 'path':
            print path(line)
        elif line[0] == 'reachable':
            print reach()
        elif line[0] == 'vertexup':
            vertexUp(line[1])
        elif line[0] == 'vertexdown':
            vertexDown(line[1])
        elif line[0] == 'edgeup':
            edgeUp(line[1],line[2])
        elif line[0] == 'edgedown':
            edgeDown(line[1],line[2])
        elif line[0] == 'addedge':
            addEdge(line[1],line[2],line[3])
        else:
            deleteEdge(line[1],line[2])

def printGraph():
    
    temp = " "
    temp1 = " "
    
    for vertex in verList:
        temp1 = vertex[0]
        if vertex[1] == 'DOWN':
            temp1 += " " + 'DOWN'
            f.write(temp1)
        else:
            f.write(temp1)
        f.write('\n')
        for edge in edgList:
            if edge[0] == vertex[0]:
                temp = "  " + edge[1] + " " + edge[2]
                if edge[3] == 'DOWN':
                    temp += " " + edge[3]
                    f.write(temp)
                    f.write('\n')
                else:
                    f.write(temp)
                    f.write('\n')
    
    f.write('\n')

def path(input):
    
    source = input[1]
    destination = input[2]
    vertexQueue = PriorityQueue()
    vertexQueue.put(source)

def reach():
    
    temp = " "
    
    for vertex in verList:
        if vertex[1] == 'UP':
            f.write(vertex[0])
            f.write('\n')
            for edge in edgList:
                if edge[0] == vertex[0] and edge[3] == 'UP':
                    temp = "  " + edge[1]
                    f.write(temp)
                    f.write('\n')
                else:
                    continue
        else:
            continue
        
    f.write('\n')

def addEdge(tailVertex,headVertex,transmit_time):
        
    edgeStatus = 'UP'
    currEdge = [tailVertex,headVertex,transmit_time,edgeStatus]
        
    for record in edgList:
        if currEdge[:-2] == record[:-2]:
            if currEdge[2] == record[2]:
                break
            else:
                record[2] = transmit_time
                break
            break
        else:
            while currEdge not in initialGraph:
                edgList.append(currEdge)
            break
    
def deleteEdge(tailVertex,headVertex):
        
    currEdge = [tailVertex,headVertex]
        
    for record in edgList:
        if record[:-2] == currEdge:
            edgList.remove(record)
            break
        else:
            continue
    
def edgeDown(tailVertex,headVertex):
            
    for record in edgList:
        if record[0] == tailVertex and record[1] == headVertex:
            record[3] = 'DOWN'
        else:
            continue
    
def edgeUp(tailVertex,headVertex):
           
    for record in edgList:
        if record[0] == tailVertex and record[1] == headVertex:
            record[3] = 'UP'
        else:
            continue
    
def vertexDown(vertexName):
        
    for record in verList:
        if record[0] == vertexName:
            record[1] = 'DOWN'
        else:
            continue
    
def vertexUp(vertexName):
        
    for record in verList:
        if record[0] == vertexName:
            record[1] = 'UP'
        else:
            continue

f = open(sys.argv[3], 'w')
output()
f.close()