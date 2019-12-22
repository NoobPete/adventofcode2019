inputFile = open("input05.txt", "r")
input = list(map(int, inputFile.read().split(",")))

## Part 1
def computer(code, inputs = []):
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

assert(computer([1,0,0,0,99])[0] == [2,0,0,0,99])
assert(computer([2,3,0,3,99])[0] == [2,3,0,6,99])
assert(computer([2,4,4,5,99,0])[0] == [2,4,4,5,99,9801])
assert(computer([1,1,1,4,99,5,6,0,99])[0] == [30,1,1,4,2,5,6,0,99])

assert(computer([3,0,4,0,99], [10])[1] == [10])

print("Part 1:", computer(input.copy(), [1])[1])

## Part 2

assert(computer([3,9,8,9,10,9,4,9,99,-1,8], [8])[1] == [1])
assert(computer([3,9,8,9,10,9,4,9,99,-1,8], [24])[1] == [0])

assert(computer([3,9,7,9,10,9,4,9,99,-1,8], [24])[1] == [0])
assert(computer([3,9,7,9,10,9,4,9,99,-1,8], [8])[1] == [0])
assert(computer([3,9,7,9,10,9,4,9,99,-1,8], [4])[1] == [1])

assert(computer([3,3,1108,-1,8,3,4,3,99], [8])[1] == [1])
assert(computer([3,3,1108,-1,8,3,4,3,99], [24])[1] == [0])

assert(computer([3,3,1107,-1,8,3,4,3,99], [24])[1] == [0])
assert(computer([3,3,1107,-1,8,3,4,3,99], [8])[1] == [0])
assert(computer([3,3,1107,-1,8,3,4,3,99], [4])[1] == [1])

assert(computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [0])[1] == [0])
assert(computer([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [34])[1] == [1])

assert(computer([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [0])[1] == [0])
assert(computer([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [34])[1] == [1])

longCode = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
            1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
            999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

assert(computer(longCode, [7])[1] == [999])
assert(computer(longCode, [8])[1] == [1000])
assert(computer(longCode, [9])[1] == [1001])

print("Part 2:", computer(input.copy(), [5])[1])