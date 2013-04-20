from collections import namedtuple

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
 
edjList = ShortestPath([('Belk', 'Grigg', 1.2),  ('Grigg', 'Belk', 1.2),  ('Belk', 'Health', 0.5), ('Health', 'Belk', 0.5),
               ('Duke', 'Belk', 0.6), ('Belk', 'Duke', 0.6), ('Belk', 'Woodward', 0.25),  ('Woodward', 'Belk', 0.25),
               ('Woodward', 'Grigg', 1.1), ('Grigg', 'Woodward', 1.1), ('Grigg', 'Duke', 1.6), ('Duke', 'Grigg', 1.6),
               ('Health', 'Woodward', 0.7), ('Woodward', 'Health', 0.7), ('Health', 'Education', 0.45), 
               ('Education', 'Health', 0.45), ('Woodward', 'Education', 1.3), ('Education', 'Woodward', 1.3),
               ('Duke', 'Education', 0.3), ('Education', 'Duke', 0.3), ('Woodward', 'Duke', 0.67), ('Duke', 'Woodward', 0.67)])

print edjList.dij("Belk", "Education")