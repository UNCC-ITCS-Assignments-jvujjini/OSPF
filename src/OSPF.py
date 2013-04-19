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

def verticesList():
        
        vers = []
        
        for record in initialGraph:
            if record[0] not in vers or record[1] not in vers:
                if record[0] not in vers:
                    vers.append(record[0])
                    continue
                else:
                    vers.append(record[1])
            else:
                continue
        
        for record in vers:
            record.append('UP')
            
        return vers


initialGraph = graphBuild()
verList = verticesList()
edgList = initialGraph
    
class Vertex:
    
    def __init__(self,name,status):
        self.name = name
        self.status = status
    
    def setStatus(self,name,status):
        self.status = status
    
    def getStatus(self,name,status):
        return self.status
    
    def verticesList(self):
        
        verList = []
        
        for record in initialGraph:
            if record[0] not in verList or record[1] not in verList:
                if record[0] not in verList:
                    verList.append(record[0])
                    continue
                else:
                    verList.append(record[1])
            else:
                continue
        
        for record in verList:
            record.append('UP')
            
        return verList

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
    
    def setStatus(self,edgeStatus):
        self.edgeStatus = edgeStatus
    
    def getStatus(self):
        return self.edgeStatus
    
    def getEdge(self,tailVertex,headVertex):
        
        for record in initialGraph:
            if tailVertex == record[0] and headVertex == record[1]:
                return record
            else:
                continue

class updateGraph(Vertex,Edge):
    
    def addEdge(self,tailVertex,headVertex,transmit_time):
        
        edges = Edge.edgeList()
        edgeStatus = 'UP'
        currEdge = [tailVertex,headVertex,transmit_time,edgeStatus]
        
        for record in edges:
            if currEdge[:-2] == record[:-2]:
                if currEdge[2] == record[2]:
                    break
                else:
                    initialGraph.append(currEdge)
                    break
                break
            else:
                while currEdge not in initialGraph:
                    currEdge.append(transmit_time,edgeStatus)
                    initialGraph.append(currEdge)
                break
    
    def deleteEdge(self,tailVertex,headVertex):
        
        edges = Edge.edgeList()
        currEdge = edges.getEdge(tailVertex,headVertex)
        
        while len(currEdge) != 0:
            for record in edges:
                if record[-2] == currEdge[-2]:
                    initialGraph.remove(record)
                    break
                else:
                    continue
    
    def edgeDown(self,tailVertex,headVertex):
        
        edges = Edge.edgeList()
        currEdge = edges.getEdge(tailVertex,headVertex)
        
        while len(currEdge) != 0:
            for record in edges:
                if record == currEdge:
                    record.setStatus('EDOWN')
                    break
                else:
                    continue
    
    def edgeUp(self,tailVertex,headVertex):
        
        for record in initialGraph:
            if tailVertex == record[0] and headVertex == record[1]:
                record.setStatus('UP')
                break
            else:
                continue
    
    def vertexDown(self,vertexName):
        
        vertices = Vertex.verticesList()
        
        for record in vertices:
            if vertexName == record[0] or vertexName == record[1]:
                Vertex.setStatus(vertexName,'DOWN')
            else:
                continue
    
    def vertexUp(self,vertexName):
        
        vertices = Vertex.verticesList()
        
        for record in vertices:
            if vertexName == record[0] or vertexName == record[1]:
                record.setStatus(vertexName,'UP')
            else:
                continue
    
    
    
class OSPF:
    
    def Dijkstra(self):
        return 0
    def shortestPath(self):
        return 0
    def 