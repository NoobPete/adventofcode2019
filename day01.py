inputFile = open("input01.txt", "r")
input = list(map(int, inputFile.read().split("\n")))

## Part 1
def fuelCalculator(mass):
    return mass//3 - 2

assert(fuelCalculator(12) == 2)
assert(fuelCalculator(14) == 2)
assert(fuelCalculator(1969) == 654)
assert(fuelCalculator(100756) == 33583)


print("Part 1:", sum([fuelCalculator(i) for i in input]))

## Part 2
def fuelFuelCalculator(mass):
    fuel = mass//3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuelFuelCalculator(fuel)

assert(fuelFuelCalculator(12) == 2)
assert(fuelFuelCalculator(1969) == 966)
assert(fuelFuelCalculator(100756) == 50346)

print("Part 2:", sum([fuelFuelCalculator(i) for i in input]))