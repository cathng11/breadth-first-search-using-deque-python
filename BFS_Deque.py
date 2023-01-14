from collections import deque
def findQueue(n, matrix,initialState):
    explored = [0 for i in range(n)]
    result = []
    frontier = deque([initialState]) 
    explored[initialState] = 1
    node = frontier.popleft() 
    result.append(node)
    while True:
        for x in range(0, len(explored)):
            if (int(matrix[node][x]) == 1 and int(explored[x]) == 0):
                explored[x] = 1
                frontier.append(x)
        if len(frontier) == 0:
            break
        else:
            node = frontier.popleft()
            result.append(node)
    queue = []
    for i in range(0, len(result)):
        queue.append(numToAlpha(result[i]))
    print("Queue: ", queue)
    return result


def findOrderOfVisit(queue, goalTest):
    order=[]
    for index, value in enumerate(queue):
        if value == goalTest:
            for i in range(0, index+1):
                order.append(numToAlpha(queue[i]))
            break
    print("Order of visit: ",order)


def numToAlpha(result):
    switcher = {
        0: "S",
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G",
        8: "H",
    }
    return switcher.get(result, "Empty")


def alphaToNum(arg):
    switcher = {
        "S": 0,
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5,
        "F": 6,
        "G": 7,
        "H": 8,
    }
    return switcher.get(arg, "Empty")


with open(r'./Input.txt') as fl:
    line = fl.read().splitlines()
matrix = [[0 for i in range(int(line[0]))] for j in range(int(line[0]))]
for i in range(1, len(line)):
    matrix[i-1] = line[i]
n = int(line[0])

ini = input("Enter initial state: ")
goal = input("Enter goal: ")
ini = ini.upper()
goal = goal.upper()
findOrderOfVisit(findQueue(n, matrix,alphaToNum('S')), alphaToNum('G'))
