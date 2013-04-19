import random
import math 
 
#left child
def left(i):
    return int(2 * i + 1)
 
#right child
def right(i):
    return int(2 * i + 2)
 
#parent node    
def parent(i):
    return int(math.floor(i / 2))
 
class edge:
    u = 0
    v = 0
    w = 0
 
    def __init__(self, au, av, aw):
        self.u = au
        self.v = av
        self.w = aw
 
class heap_node:
    _object = 0
    _value = 0
 
    def __init__(self,aobject,avalue):
        self._object = aobject
        self._value = avalue
 
'''
    Implementation of a binary minimum heap.
    @notes
    @todo
        Consider replacing _data w/ a more generic structure that allows nodes to have a weight
        and a pointer to a different data structure.
'''
class Minimum_Heap:
    #the main data array
    _data = None
 
    def __init__(self,data):
        self._data = list(data)
        self.build()
 
    #Min. heapify (cascade down from idx down until sub parent nodes are greater than their children)
    def __heapify__(self,idx):
        l = left(idx)
        r = right(idx)
        p = parent(idx)
 
        min = idx
        size = len(self._data)
 
        if l < size and self._data[l]._value < self._data[min]._value:
            min = l
 
        if r < size and self._data[r]._value < self._data[min]._value:
            min = r
 
        if not min == idx:
            tmp = self._data[min]
            self._data[min] = self._data[idx]
            self._data[idx] = tmp
            self.__heapify__(min)
 
    #build min heap
    def build(self):
        size = len(self._data)
        for i in range(int(math.floor(size/2))-1,-1,-1):
            self.__heapify__(i)
 
'''
    Implementation of a min priority queue
'''
class Minimum_Priority_Queue:
    _heap = None
 
    def __init__(self,data):
        self._heap = Minimum_Heap(data)
 
    #Get min w/o destroying nodes
    def min(self):
        return self._heap._data[0]
 
    #Get min, remove root node
    def extract_min(self):
        size = len(self._heap._data)
        if size <= 0:
            return None
        min = self._heap._data[0]
        self._heap._data[0] = self._heap._data[size-1]
        self._heap._data.pop(size-1)
        self._heap.__heapify__(0)
        return min
 
    #insert new value
    def insert(self,key):
        self._heap._data.append(float("inf"))
        self.decrease_key(len(self._data)-1,key)
 
    #decrease existing value
    def decrease_key(self,elem,key):
        if elem < 0 or elem >= len(self._heap._data):
            print "elem",elem,"not in heap data range.  [0 <= ",elem," <= ",len(self._heap._data),"]"
            return
 
        if key > self._heap._data[elem]._value:
            print "new key larger than current key"
            return
 
        self._heap._data[elem]._value = key
 
        i = elem
        #cascade changes upward by swapping parents until child is greater than parent.
        while i > 0 and self._heap._data[parent(i)]._value > self._heap._data[i]._value:
            tmp = self._heap._data[i]
            self._heap._data[i] = self._heap._data[parent(i)]
            self._heap._data[parent(i)] = tmp
            i = parent(i)
 
    def decrease_object(self,obj,key):
        count = 0
        for hn in self._heap._data:
            if hn._object == obj:
                self.decrease_key(count,key)
                return
            count += 1
        print "Object not found in heap"
 
class node:
    _i  = -1
    _w     = 0             #weight
    _adj = None        #adjacent vertices (connected by out edge)
 
    def __init__(self,ai,aw):
        self._i = ai
        self._w = aw
        self._adj = list()
 
#Graph hardcoded to "Intro. to Algorithms Figure 24.6"        
def build_graph():
    G = list()
    G.append(edge(0,1,10))
    G.append(edge(0,2,5))
    G.append(edge(1,2,2))
    G.append(edge(1,3,1))
    G.append(edge(2,1,3))
    G.append(edge(2,3,9))
    G.append(edge(2,4,2))
    G.append(edge(3,4,4))
    G.append(edge(4,0,7))
    G.append(edge(4,3,6))
 
    used = dict()
    V = list()
    E = dict()
 
    for e in G:
        if not e.u in used:
            used[e.u] = True
            V.append(node(len(V),float("inf")))
 
    V[0]._w = 0
 
    V[0]._adj.append(1)
    V[0]._adj.append(2)
 
    V[1]._adj.append(2)
    V[1]._adj.append(3)
 
    V[2]._adj.append(1)
    V[2]._adj.append(3)
    V[2]._adj.append(4)
 
    V[3]._adj.append(4)
 
    V[4]._adj.append(0)
    V[4]._adj.append(3)
 
    for e in G:
        if not V[e.u] in E:
            E[V[e.u]] = dict()
 
        E[V[e.u]][V[e.v]] = e 
 
    return (G,V,E)
 
def dijsktra():
    s = 0         #source
    S = list()    #final weighted vertices
 
    #Initialize Graph
    G,V,E = build_graph()
 
    #Vertices as heap_nodes
    VN = list()
 
    #Convert vertices from our graph in to heap nodes
    for v in V:
        VN.append(heap_node(v,v._w))
 
 
    #Perform initial sort
    Q = Minimum_Priority_Queue(VN)
 
    #Grab first element from queue (the source)
    uq = Q.extract_min()
 
    while not uq == None:
 
        #get original vertex
        u = uq._object
 
        #Add vertex to shorted path set
        S.append(u)
 
        #Loop through adjecent nodes, relax each node.
        for v in E[u]:
            edge = E[u][v]
 
            if u._w + edge.w < v._w:
                v._w = u._w + edge.w
                Q.decrease_object(v,v._w)
 
        print_array(Q._heap._data,"Heap:")
        uq = Q.extract_min()
 
    print "Node Weights:",
    for s in V:
        print s._w
    print ""
 
def print_array(A,Header):
    print Header,
    for node in A:
        print node._value,
    print ""
 
#dijsktra()

#build_graph()

G = graphBuild()

query = open(sys.argv[2], "r").readline()

query = query.strip()
query = query.split(" ")
initial = query[0]
final = query[1]

print shortestPath(G,initial,final)