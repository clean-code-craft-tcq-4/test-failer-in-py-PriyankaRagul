def size(cms):
    if cms not in range(15,50): # if shoulder size is out of range 
        return None
    elif cms <= 38:
        return 'S'
    elif cms > 38 and cms <= 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(38) == 'S')
assert(size(5) == None)  # testcase for invalid scenario
assert(size(38) == 'L')
assert(size(40) == 'M')
assert(size(42) == 'M')
assert(size(42) == 'L')
assert(size(43) == 'L')
assert(size(55) == None) #testcase for invalid scenario
assert(size(-5) == None) #testcase for invalid scenario
print("All is well (maybe!)\n")
