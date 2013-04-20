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

print verList
print edgList

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

reach()