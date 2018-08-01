def dictInitializer(a,l):
    for x in l:
        tmp = x.split(' ')
        if int(tmp[0]) in a.keys():
            a[int(tmp[0])] = a[int(tmp[0])] | set([int(tmp[1])])
        else:
            a[int(tmp[0])] = set([int(tmp[1])])
    return a

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

if __name__ == "__main__":
    content = [x.strip() for x in open("test_file.txt").readlines()]
    to_dict = content[1:len(content)-1]
    a = dictInitializer(dict(),content[1:len(content)-1])
    to_dict = [x[::-1] for x in to_dict]
    a = dictInitializer(a,to_dict)
    var = content[len(content)-1].split(' ')
    print(verifyExit(set(),set([int(var[0])]),int(var[1]),a))
