import os
os.system('cls')


def all_path(graph,start,end,path = []):
    path = path+[start]
    if start == end:
        return[path]
    if start not in graph:
        return[]
    paths=[]
    for node in graph[start]:
        if not node in path:
            newpath = all_path(graph,node,end,path)
            for newpaths in newpath:
                paths.append(newpaths)
    return paths

# Bentuk print dari path
def displayBlock(paths):
    for i in range(len(paths)):
        print('Path : ', i+1, " = ",paths[i])

# mencari semua jalur
def find_AllEdge(graph):
    ListEdge = []
    for keys in graph.keys():
        if graph[keys] !=[]:
            for value in graph[keys]:
                temp = keys + '=>' + value
                ListEdge.append(temp)
    return ListEdge

# jalur pendek
def shorttest_path(graph,start,end,path = []):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shorttest = None
    for node in graph [start]:
        if node not in path:
            newpath =  shorttest_path(graph,node,end,path)
            if newpath:
                if not shorttest or len(newpath) < len(shorttest):
                    shorttest = newpath
    return shorttest

def find_ListShorttestPath(Allpath,ShorttestPath):
    ListShorttest = []
    for path in Allpath:
        if len(path) == len(ShorttestPath):
            ListShorttest.append(path)
    return ListShorttest

graphSembarang = {
    'A' : ['C','D'],
    'B' : ['C', 'E'],
    'C' : ['A','B','D','E'],
    'D' : ['C', 'E'],
    'E' : ['C','B'],
    'F' : []
}

# mencari jalur A ke E 
listAll_Path = all_path(graphSembarang, 'A', 'E')
displayBlock(listAll_Path)

print()

#mencari semua jalur
SemuaEdge = find_AllEdge(graphSembarang)
displayBlock(SemuaEdge)

print()

# mencari jalur terpendek
ShortPath = shorttest_path(graphSembarang,'A','E')
ListShorttestPath = find_ListShorttestPath(listAll_Path,ShortPath)

print('\nShorttest Path dan Alternative Raoute')
displayBlock(ListShorttestPath)

