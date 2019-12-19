lowerbound = 100000
upperbound = 999999

# My range was all 6-digit numbers so no need to check for that
# We also only iterate the range, so no need for filtering that out

# Part 1
def neverGetsLower(number : int):
    currentMax = 0

    for i in range(6):
        currentPlace = number // 10**(5-i) % 10

        if currentPlace < currentMax:
            return False
        
        currentMax = currentPlace
    return True

def haveRepeat(number : int):
    for i in range(5):
        if number // 10**(5-i) % 10 == number // 10**(4-i) % 10:
            return True
    return False

assert(neverGetsLower(111111))
assert(haveRepeat(111111))
assert(False == neverGetsLower(223450))
assert(haveRepeat(223450))
assert(neverGetsLower(123789))
assert(False == haveRepeat(123789))

numberOfCorrectPasswords = 0
for i in range(lowerbound, upperbound + 1):
    if neverGetsLower(i) and haveRepeat(i):
        numberOfCorrectPasswords += 1

print("Part 1:", numberOfCorrectPasswords)

# Part 2
def haveLimitedRepeat(number : int):
    for i in range(5):
        if number // 10**(5-i) % 10 == number // 10**(4-i) % 10:
            if i < 4: # Can there be any after?
                if number // 10**(5-i) % 10 != number // 10**(3-i) % 10:
                    if i > 0: # can there be any before?
                        if number // 10**(5-i) % 10 != number // 10**(6-i) % 10:
                            return True
                    else:
                        return True
            else: 
                if number // 10**(5-i) % 10 != number // 10**(6-i) % 10:
                    return True
    return False

numberOfCorrectPasswords = 0
for i in range(lowerbound, upperbound + 1):
    if neverGetsLower(i) and haveLimitedRepeat(i):
        numberOfCorrectPasswords += 1

print("Part 2:", numberOfCorrectPasswords)