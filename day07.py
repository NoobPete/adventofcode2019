from typing import List
from typing import Set

inputFile = open("input07.txt", "r")
input = list(map(int, inputFile.read().split(",")))

## Part 1
def computer(code : List[int], inputs: List[int] = []) -> List[int]:
    def readMem(position : int):
        mode = code[pc] // 10**(1 + position) % 10
        if mode == 0:
            return code[code[pc+position]]
        elif mode == 1:
            return code[pc+position]
        raise Exception('Unexpected parameter mode: {}'.format(code[pc]))

    def writeMem(position : int, item : int):
        mode = code[pc] // 10**(1 + position) % 10
        if mode == 0:
            code[code[pc+position]] = item
        elif mode == 1:
            code[pc+position] = item
        else:
            raise Exception('Unexpected parameter mode: {}'.format(code[pc]))

    pc = 0
    outputs = []

    while (True):
        cmd = code[pc] % 100
        if cmd == 1: # p3 = p1 + p2
            writeMem(3, readMem(1) + readMem(2))
            pc = pc + 4
        elif cmd == 2: # p3 = p1 * p2
            writeMem(3, readMem(1) * readMem(2))
            pc = pc + 4
        elif cmd == 3: # p1 = input
            writeMem(1, inputs[0])
            inputs = inputs[1:]
            pc = pc + 2
        elif cmd == 4: # output = p1
            outputs.append(readMem(1))
            pc = pc + 2
        elif cmd == 5: # if p1 != 0 then pc = p2
            if (readMem(1) != 0):
                pc = readMem(2)
            else: 
                pc = pc + 3
        elif cmd == 6: # if p1 == 0 then pc = p2
            if (readMem(1) == 0):
                pc = readMem(2)
            else: 
                pc = pc + 3
        elif cmd == 7: # p3 = (if p1 < p2 then 1 else 0)
            if (readMem(1) < readMem(2)):
                writeMem(3, 1)
            else: 
                writeMem(3, 0)
            pc = pc + 4
        elif cmd == 8: # p3 = (if p1 == p2 then 1 else 0)
            if (readMem(1) == readMem(2)):
                writeMem(3, 1)
            else: 
                writeMem(3, 0)
            pc = pc + 4
        elif cmd == 99:
            return code, outputs
        else:
            raise Exception('Unexpected instruction while running: {}'.format(code[pc]))

def testBiggestThrust(possibleValues : List[int], ampIn : int = 0) -> Set[int]:
    resultSet = set()

    if len(possibleValues) == 0:
        resultSet.add(ampIn)
    else:
        for i in possibleValues:
            ampOut = computer(input.copy(), [i, ampIn])[1][0]
            filteredList = [e for e in possibleValues if i != e]
            resultSet = resultSet.union(testBiggestThrust(filteredList, ampOut))
    
    return resultSet

print("Part 1:", max(testBiggestThrust([0, 1, 2, 3, 4])))
