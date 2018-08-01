def dictSetter(d,l):
    for x in l:
        tmp = x.split(' ')
        if int(tmp[0]) in d.keys():
            d[int(tmp[0])] = d[int(tmp[0])] | set([int(tmp[1])])
        else:
            d[int(tmp[0])] = set([int(tmp[1])])
    return d

#Worst case it cheks every node for the number of nodes - 2 times, so all the nodes
#with the exception of itself and the goal, minus all the visited nodes.
#Same for every other node. Complexity speaking: O(|Nodes| * |Nodes - 2|) - |Visited|
def verifyExit(visited, to_visit, goal, dic):
    if goal in to_visit: return 1
    else:
        visited = visited | to_visit
        for x in to_visit:
            for y in dic[x]:
                if y not in visited: to_visit = to_visit | set([y])
        to_visit = to_visit - visited
        if to_visit == set(): return 0
        return verifyExit(visited, to_visit, goal, dic)

#it inizializes the dictionary according to the number of nodes, each at None
def dictInitializer(l,d):
    for x in range(int(l.split(" ")[0].strip())): d[x+1] = set()

#it reverses the strings inside the list: ["1 2", "3 4"] = ["2 1", "4 3"]
reversingNodes = lambda l: list(map(lambda x: x[::-1], l))

#it opens the file, inizializes the node lists and the dictionary with the correct
# set up
def inizialization():
    content,myDict = [x.strip() for x in open("test_file.txt").readlines()],dict()
    dictInitializer(content[0],myDict)
    content = content[1:len(content)-1]
    _from,_to = content[-1].split(" ")[0],content[-1].split(" ")[1]
    dictSetter(myDict,content)  #since it is undirected we need to have both ways connected
    content = reversingNodes(content)
    dictSetter(myDict,content[::-1])# 1 -> 2 means also 2 -> 1
    return myDict, int(_from.strip()), int(_to.strip())

if __name__ == "__main__":
    nodeDictionary,_from,_to = inizialization()
    print(verifyExit(set(),set([_from]),_to,nodeDictionary))
