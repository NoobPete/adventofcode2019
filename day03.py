inputFile = open("input03.txt", "r")
lines = list(inputFile.read().split("\n"))

## Part 1
class Wire:
    direction = ""
    length = 0

    def __init__(self, data):
        self.direction = data[0]
        self.length = int(data[1:])
    
    def getXMul(self):
        if self.direction == "L":
            return -1
        elif self.direction == "R":
            return 1
        else:
            return 0

    def getYMul(self):
        if self.direction == "D":
            return -1
        elif self.direction == "U":
            return 1
        else:
            return 0

def convertInput(lines):
    for idx, l in enumerate(lines):
        wires = list(lines[idx].split(","))
        lines[idx] = [Wire(i) for i in wires]
    return lines

lines = convertInput(lines)

def applyDirectionToPoint(point, direction : Wire):
    return (point[0]+direction.getXMul()*direction.length, point[1]+direction.getYMul()*direction.length)

def distance(point1, point2):
    return abs(point1[0]-point2[0]) + abs(point1[1]-point2[1])

def intersection(linePos1, direction1 : Wire, linePos2, direction2 : Wire):
    endPoint1 = applyDirectionToPoint(linePos1, direction1)
    endPoint2 = applyDirectionToPoint(linePos2, direction2)

    # Check parrallel
    if direction1.getXMul() * direction2.getXMul() == 1 and linePos1[1] == linePos2[1]:
        xleft = max(min(linePos1[0], endPoint1[0]), min(linePos2[0], endPoint2[0]))
        xright = min(max(linePos1[0], endPoint1[0]), max(linePos2[0], endPoint2[0]))
        return [(i, linePos1[1]) for i in range(xleft, xright + 1)]
    if direction1.getYMul() * direction2.getYMul() == 1 and linePos1[0] == linePos2[0]:
        ydown = max(min(linePos1[1], endPoint1[1]), min(linePos2[1], endPoint2[1]))
        yup = min(max(linePos1[1], endPoint1[1]), max(linePos2[1], endPoint2[1]))
        return [(linePos1[0], i) for i in range(ydown, yup + 1)]

    # Check non-parrallel
    if direction1.getXMul() != 0:
        minx = min(linePos1[0], endPoint1[0])
        maxx = max(linePos1[0], endPoint1[0])

        if linePos2[0] >= minx and linePos2[0] <= maxx:
            miny = min(linePos2[1], endPoint2[1])
            maxy = max(linePos2[1], endPoint2[1])

            if linePos1[1] >= miny and linePos1[1] <= maxy:
                return [(linePos2[0],linePos1[1])]
    else: 
        miny = min(linePos1[1], endPoint1[1])
        maxy = max(linePos1[1], endPoint1[1])

        if linePos2[1] >= miny and linePos2[1] <= maxy:
            minx = min(linePos2[0], endPoint2[0])
            maxx = max(linePos2[0], endPoint2[0])

            if linePos1[0] >= minx and linePos1[0] <= maxx:
                return [(linePos1[0],linePos2[1])]
    
    return []
    

def findBestClosetsCrossingPoint(lines):
    currentBasePosition = (0,0)
    currentBestCrossingPoint = None
    currentBestCrossingPointDistance = None

    for w in lines[0]:
        tempPosition = (0,0)
        for w2 in lines[1]:
            intersections = intersection(currentBasePosition, w, tempPosition, w2)
            for p in intersections:
                if p != (0,0) and (currentBestCrossingPoint == None or currentBestCrossingPointDistance > distance(p, (0,0))):
                    currentBestCrossingPoint = p
                    currentBestCrossingPointDistance = distance(p, (0,0))
            tempPosition = applyDirectionToPoint(tempPosition, w2)
        currentBasePosition = applyDirectionToPoint(currentBasePosition, w)

    return currentBestCrossingPoint

testInput0 = convertInput(list("R8,U5,L5,D3\nU7,R6,D4,L4".split("\n")))
testInput1 = convertInput(list("R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83".split("\n")))
testInput2 = convertInput(list("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split("\n")))

assert(distance(findBestClosetsCrossingPoint(testInput0), (0,0)) == 6)
assert(distance(findBestClosetsCrossingPoint(testInput1), (0,0)) == 159)
assert(distance(findBestClosetsCrossingPoint(testInput2), (0,0)) == 135)

print ("Part 1:", distance(findBestClosetsCrossingPoint(lines), (0,0)))

## Part 2
def findBestLeastLineCrossingPoint(lines):
    currentBasePosition = (0,0)
    currentBestCrossingPoint = None
    currentBestCrossingPointDistance = None

    lineSoFar = 0
    for w in lines[0]:
        tempPosition = (0,0)
        tempLineSoFar = 0
        for w2 in lines[1]:
            intersections = intersection(currentBasePosition, w, tempPosition, w2)
            for p in intersections:
                totalLineLength = lineSoFar + tempLineSoFar + distance(p, currentBasePosition) + distance(p, tempPosition) # distance(current, temp) should also work for the last two
                if p != (0,0) and (currentBestCrossingPoint == None or currentBestCrossingPointDistance > totalLineLength):
                    currentBestCrossingPoint = p
                    currentBestCrossingPointDistance = totalLineLength
            tempPosition = applyDirectionToPoint(tempPosition, w2)
            tempLineSoFar = tempLineSoFar + w2.length
        currentBasePosition = applyDirectionToPoint(currentBasePosition, w)
        lineSoFar = lineSoFar + w.length

    return currentBestCrossingPointDistance

assert(findBestLeastLineCrossingPoint(testInput0) == 30)
assert(findBestLeastLineCrossingPoint(testInput1) == 610)
assert(findBestLeastLineCrossingPoint(testInput2) == 410)

print ("Part 2:", findBestLeastLineCrossingPoint(lines))