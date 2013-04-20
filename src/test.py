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
    
    for line in queries:
        line = line.rstrip()
        query = line.split(" ")
        if query[0] == 'print':
            print printGraph()
        elif query[0] == 'path':
            print path(query)
        elif query[0] == 'reachable':
            print reach()
        elif query[0] == 'vertexup':
            verUp = updateGraph()
            verUp.vertexUp(query[1])
        elif query[0] == 'vertexdown':
            verDown = updateGraph()
            verDown.vertexDown(query[1])
        elif query[0] == 'edgeup':
            edgUp = updateGraph()
            edgUp.edgeUp(query[1],query[2])
        elif query[0] == 'edgedown':
            edgDown = updateGraph()
            edgDown.edgeDown(query[1],query[2])
        elif query[0] == 'addedge':
            add = updateGraph()
            add.addEdge(query[1],query[2],query[3])
        else:
            delete = updateGraph()
            delete.deleteEdge(query[1],query[2])

def printGraph():
    
    temp = " "
    
    for vertex in verList:
        print vertex[0]
        for edge in edgList:
            if edge[0] == vertex[0]:
                temp = " " + edge[1] + " " + edge[2]
                if edge[3] == 'DOWN':
                    temp += " " + edge[3]
                    print temp
                else:
                    print temp

def path(input):
    
    source = input[1]
    destination = input[2]
    vertexQueue = PriorityQueue()
    vertexQueue.put(source)

def reach():
    
    temp = " "
    
    for vertex in verList:
        if vertex[1] == 'UP':
            print vertex[0]
            for edge in edgList:
                if edge[0] == vertex[0] and edge[3] == 'UP':
                    temp = "  " + edge[1]
                    print temp
                else:
                    continue
        else:
            continue

class Vertex:
    
    def __init__(self,name,status):
        self.name = name
        self.status = status
    
    def setStatus(self,name,status):
        
        for record in verList:
            if record[0] == name:
                record[1] = status
            else:
                continue
    
    def getStatus(self,name):
        
        for record in verList:
            if record[0] == name:
                return record[1]
            else:
                continue
    
    def adjVertices(self,name):
        
        adjVerticesList = []
        
        for record in initialGraph:
            if record[0] == name or record[1] == name:
                if record[0] == name and record[1] not in adjVerticesList:
                    adjVerticesList += record[1]
                elif record[0] not in adjVerticesList:
                    adjVerticesList += record[0]
                else:
                    continue
            else:
                continue
        
        return adjVerticesList

class Edge:
    
    def __init__(self,tailVertex,headVertex,transmit_time,edgeStatus):
        self.tailVertex = tailVertex
        self.headVertex = headVertex
        self.transmit_time = transmit_time
        self.edgeStatus = edgeStatus
    
    def setStatus(self,tailVertex,headVertex,edgeStatus):
        
        for record in edgList:
            if record[0] == tailVertex and record[1] == headVertex:
                record[3] = edgeStatus
            else:
                continue
    
    def getStatus(self,tailVertex,headVertex,edgeStatus):
        
        for record in edgList:
            if record[0] == tailVertex and record[1] == headVertex:
                return edgeStatus
            else:
                continue
    
    def getEdge(self,tailVertex,headVertex):
        
        for record in initialGraph:
            if tailVertex == record[0] and headVertex == record[1]:
                return record
            else:
                continue

class updateGraph(Vertex,Edge):
    
    def addEdge(self,tailVertex,headVertex,transmit_time):
        
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
    
    def deleteEdge(self,tailVertex,headVertex):
        
        currEdge = [tailVertex,headVertex]
        
        for record in edgList:
            if record[:-2] == currEdge:
                edgList.remove(record)
                break
            else:
                continue
    
    def edgeDown(self,tailVertex,headVertex):
        
        list1 = Edge()
        
        for record in edgList:
            if record[0] == tailVertex and record[1] == headVertex:
                list1.setStatus(tailVertex,headVertex,'DOWN')
            else:
                continue
    
    def edgeUp(self,tailVertex,headVertex):
        
        list1 = Edge()
        
        for record in edgList:
            if record[0] == tailVertex and record[1] == headVertex:
                list1.setStatus(tailVertex,headVertex,'UP')
            else:
                continue
    
    def vertexDown(self,vertexName):
        
        list1 = Vertex()
        
        for record in verList:
            if record[0] == vertexName:
                list1.setStatus(vertexName,'DOWN')
            else:
                continue
    
    def vertexUp(self,vertexName):
        
        list1 = Vertex()
        
        for record in verList:
            if record[0] == vertexName:
                list1.setStatus(vertexName,'UP')
            else:
                continue


output()