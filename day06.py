inputFile = open("input06.txt", "r")
inputText = list(inputFile.read().split("\n"))

## Part 1
def convertInput(orbits):
    result = {}

    for idx in range(len(orbits)):
        orbit = list(orbits[idx].split(")"))
        result[orbit[1]] = orbit[0]
    
    return result

def checkSumCalcualtor(orbitmap : dict):
    result = 0

    for planet in orbitmap.keys():
        currentPlanet = planet
        while currentPlanet != "COM":
            result += 1
            currentPlanet = orbitmap[currentPlanet]

    return result

testString = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L".split("\n")
testOrbit = convertInput(testString)
assert(checkSumCalcualtor(testOrbit) == 42)

print("Part 1:", checkSumCalcualtor(convertInput(inputText)))

## Part 2
def pointToCOM(point, orbitmap : dict):
    currentPath = []
    while point != "COM":
        currentPath.append(point)
        point = orbitmap[point]
    return currentPath[::-1] # reverses

def distanceToSanta(orbitmap : dict):
    youToCOM = pointToCOM("YOU", orbitmap)
    sanToCOM = pointToCOM("SAN", orbitmap)

    while youToCOM[0] == sanToCOM[0]:
        youToCOM = youToCOM[1:]
        sanToCOM = sanToCOM[1:]

    return len(youToCOM) + len(sanToCOM) - 2

testString2 = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L\nK)YOU\nI)SAN".split("\n")
testOrbit2 = convertInput(testString2)
assert(distanceToSanta(testOrbit2) == 4)

print("Part 2:", distanceToSanta(convertInput(inputText)))