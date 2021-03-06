inputFile = open("input02.txt", "r")
input = list(map(int, inputFile.read().split(",")))

## Part 1
def computer(code):
    pc = 0

    while (True):
        cmd = code[pc]

        if cmd == 1:
            code[code[pc+3]] = code[code[pc+1]] + code[code[pc+2]]
        elif cmd == 2:
            code[code[pc+3]] = code[code[pc+1]] * code[code[pc+2]]
        elif cmd == 99:
            break
        else:
            raise Exception('Unexpected instruction while running: {}'.format(code[pc]))
        pc = pc + 4

    return code

assert(computer([1,0,0,0,99]) == [2,0,0,0,99])
assert(computer([2,3,0,3,99]) == [2,3,0,6,99])
assert(computer([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
assert(computer([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])

computerInput = input.copy()
computerInput[1] = 12
computerInput[2] = 2

print("Part 1:", computer(computerInput)[0])

## Part 2

for noun in range(100):
    for verb in range(100):
        testInput = input.copy()
        testInput[1] = noun
        testInput[2] = verb
        if computer(testInput)[0] == 19690720:
            print("Part 2:", 100 * noun + verb)

print("Finished")