from Queue import PriorityQueue
from collections import namedtuple
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

verList = verticesList()
edgList = initialGraph

tempList = []
    
for record in edgList:
    temp = (record[0],record[1],float(record[2]))
    tempList.append(temp)

#print verList
#print edgList

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
    
    #source = input[1]
    #destination = input[2]
    #vertexQueue = PriorityQueue()
    #vertexQueue.put(source)

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
            while currEdge not in edgList:
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

Graph = namedtuple('Graph', 'src, des, time')
buf = float('inf')

class ShortestPath():
    def __init__(self, edgs):
        self.edgs = edgs1 = [Graph(*rec) for rec in edgs]
        self.verts = set(sum(([rec.src, rec.des] for rec in edgs1), []))
 
    def dij(self, source, destination):
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