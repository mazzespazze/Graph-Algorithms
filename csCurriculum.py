from mazeExit import *

def inizialization():
    content,myDict = [x.strip() for x in open("test_file.txt").readlines()],dict()
    dictInitializer(content[0],myDict)
    content = content[1:]
    dictSetter(myDict,content)  #it is a directed graph
    return myDict

def cycleFinder(d,visited, to_visit,c=0):
    if visited & to_visit != set(): return (1,set())
    if to_visit == set(): return (0,visited)
    tmp = set()
    for x in to_visit:
        visited = visited | set([x])
        tmp = tmp | set([x])
        for y in d[x]:
            to_visit = to_visit | set([y])
    to_visit = to_visit - tmp
    return cycleFinder(d,visited,to_visit,c+1)


if __name__ == '__main__':
    myDict = inizialization()
    print(myDict)
    l = set(myDict.keys())
    while True:
        s,tmp = cycleFinder(myDict,set(),set([list(l)[0]]))
        l = l - tmp
        if s == 1: break # there is a cycles
        elif l == set():
            s = 0
            break
    print(s)
