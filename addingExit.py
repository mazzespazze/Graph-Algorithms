from mazeExit import *

#it is slightly different from the mazeExit
# 1) We consider also the last tuple of data
# 2) We do not consider the goal "from - to"
# Hence it is here re-coded
def inizialization():
    content,myDict = [x.strip() for x in open("test_file.txt").readlines()],dict()
    dictInitializer(content[0],myDict)
    content = content[1:] #first difference
    dictSetter(myDict,content)  #since it is undirected we need to have both ways connected
    content = reversingNodes(content)
    dictSetter(myDict,content[::-1])# 1 -> 2 means also 2 -> 1
    return myDict

#it simply start from one node. if it is able to
def explorer(d,visited,to_visit):
    visited = visited | to_visit
    if to_visit == set(): return visited
    for x in to_visit:
        for y in d[x]:
            if y not in visited: to_visit = to_visit | set([y]) #adding a node to visit
    to_visit = to_visit - visited
    return explorer(d,visited,to_visit)

def componentsCounter(nodes,nodeDictionary,c):
    if nodes == []: return c
    res = explorer(nodeDictionary,set(),set([nodes[0]]))
    nodes = list(set(nodes) - res)
    return componentsCounter(nodes,nodeDictionary,c+1)

if __name__ == '__main__':
    nodeDictionary = inizialization()
    nodes = nodeDictionary.keys()
    print(componentsCounter(nodes,nodeDictionary,0))
    #for x in nodeDictionary:
    #    print(componentsCounter(nodeDictionary,set(),set([x])))
