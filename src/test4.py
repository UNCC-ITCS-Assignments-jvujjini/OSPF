verList = [['Belk', 'UP'], ['Grigg', 'UP'], ['Health', 'UP'], ['Duke', 'UP'], ['Woodward', 'UP'], ['Education', 'UP']]
edgList = [['Belk', 'Grigg', '1.2', 'UP'], ['Grigg', 'Belk', '1.2', 'UP'], ['Belk', 'Health', '0.5', 'UP'], ['Health', 'Belk', '0.5', 'UP'], ['Duke', 'Belk', '0.6', 'UP'], ['Belk', 'Duke', '0.6', 'UP'], ['Belk', 'Woodward', '0.25', 'UP'], ['Woodward', 'Belk', '0.25', 'UP'], ['Woodward', 'Grigg', '1.1', 'UP'], ['Grigg', 'Woodward', '1.1', 'UP'], ['Grigg', 'Duke', '1.6', 'UP'], ['Duke', 'Grigg', '1.6', 'UP'], ['Health', 'Woodward', '0.7', 'UP'], ['Woodward', 'Health', '0.7', 'UP'], ['Health', 'Education', '0.45', 'UP'], ['Education', 'Health', '0.45', 'UP'], ['Woodward', 'Education', '1.3', 'UP'], ['Education', 'Woodward', '1.3', 'UP'], ['Duke', 'Education', '0.3', 'UP'], ['Education', 'Duke', '0.3', 'UP'], ['Woodward', 'Duke', '0.67', 'UP'], ['Duke', 'Woodward', '0.67', 'UP']]


def adjVertex(name):
    
    adjList = []
    
    for record in edgList:
        if record[0] == name and record[3] == 'UP':
            adjList.append(record[1])
    
    for ver in verList:
        if ver[1] == 'DOWN' and ver[0] in adjList:
            adjList.remove(ver[0])
    
    return adjList

print adjVertex('Belk')

print adjVertex('Grigg')



'''for record in edgList:
    if record[0] == 'Belk':
        next = record[1]
        dist = record[2]'''
        