from csCurriculum import *

#fewest edges first approach: FEF
if __name__ == '__main__':
    content,myDict = [x.strip() for x in open("test_file.txt").readlines()],dict()
    myDict = inizialization()
    print(sorted(myDict.keys(), key = lambda x: len(myDict[x])))
