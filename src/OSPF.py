from Queue import PriorityQueue
from collections import namedtuple
import sys

def graphBuild():
    '''Build the Graph onto a List from 
    the First Argument which takes a file input'''
    
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
    '''Maintains a List of Unique Vertices on the 
    Graph on a List. Also Maintains the status of the Vertices'''
    
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

verList = verticesList()
edgList = initialGraph

tempList = []

'''tempList is a List of tuples which is given 
as a graph input to the shortestPath Class'''
    
for record in edgList:
    temp = (record[0],record[1],float(record[2]))
    tempList.append(temp)

#print verList
#print edgList

def output():
    
    '''Takes the Second Command Line File as input and 
    splits it and feeds to each function properly to get 
    the right output'''
    
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
            print path(line[1],line[2])
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
    
    '''Prints the Graph to a file with the status of 
    each node if its DOWN'''
    
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

def path(source,destination):
    
    '''implements the shortest path function using Dijkstra's Algorithm'''
    
    result = ShortestPath(tempList)
    final = result.dij(source,destination)
    print final
    calc = len(final)
    calc1 = 0
    
    for edge in tempList:
        for n in range(1,calc):
            if final[n-1] == edge[0] and final[n] == edge[1]:
                calc1 += edge[2]

    for temp in final:
        f.write(temp + " ")
    f.write(str(calc1))
    f.write('\n\n') 

def reach():
    
    '''Prints all the Reachable Vertices from each node,
     prints them only if they are UP'''
    
    
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
    
    '''Provides the functionality to add new edges to the graph'''
        
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
            while currEdge not in edgList:
                edgList.append(currEdge)
            break
    
def deleteEdge(tailVertex,headVertex):
    
    '''Provides the functionality to remove edges from the Graph'''
        
    currEdge = [tailVertex,headVertex]
        
    for record in edgList:
        if record[:-2] == currEdge:
            edgList.remove(record)
            break
        else:
            continue
    
def edgeDown(tailVertex,headVertex):
    
    '''Updates the status of an edge to DOWN if it is 
    not available currently'''
            
    for record in edgList:
        if record[0] == tailVertex and record[1] == headVertex:
            record[3] = 'DOWN'
        else:
            continue
    
def edgeUp(tailVertex,headVertex):
    
    '''Brings an Edge back UP that is DOWN'''
           
    for record in edgList:
        if record[0] == tailVertex and record[1] == headVertex:
            record[3] = 'UP'
        else:
            continue
    
def vertexDown(vertexName):
    
    '''Updates the Status of a node that is not currently available to DOWN'''
        
    for record in verList:
        if record[0] == vertexName:
            record[1] = 'DOWN'
        else:
            continue
            
def vertexUp(vertexName):
    
    '''Updates the Status of a node from DOWN to UP 
    which is currently made available'''
        
    for record in verList:
        if record[0] == vertexName:
            record[1] = 'UP'
        else:
            continue                

Graph = namedtuple('Graph', 'src, des, time')
buf = float('inf')

class ShortestPath():
    
    '''This class is used to compute the Shortest Path between two nodes'''
    
    def __init__(self, edgs):
        self.edgs = edgs1 = [Graph(*rec) for rec in edgs]
        self.verts = set(sum(([rec.src, rec.des] for rec in edgs1), []))
 
    def dij(self, source, destination):
        
        '''Dijkstra's Algorithm implementation to compute the shortest Path'''
        
        dist = {vertex: buf for vertex in self.verts}
        prev = {vertex: None for vertex in self.verts}
        dist[source] = 0
        ver = self.verts.copy()
        nex = {vertex: set() for vertex in self.verts}
        for src, des, time in self.edgs:
            nex[src].add((des, time))
 
        while ver:
            x = min(ver, key=lambda vertex: dist[vertex])
            ver.remove(x)
            if dist[x] == buf or x == destination:
                break
            for y, cost in nex[x]:
                temp = dist[x] + cost
                if temp < dist[y]:                                  # Relax (u,v,a)
                    dist[y] = temp
                    prev[y] = x

        path, x = [], destination
        while prev[x]:
            path.insert(0, x)
            x = prev[x]
        path.insert(0, x)
        return path

f = open(sys.argv[3], 'w')
output()
f.close()