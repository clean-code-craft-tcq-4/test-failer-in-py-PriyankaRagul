def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
#checking if 38 cm comes under S or M or L
assert(size(38) == 'S')
assert(size(38) == 'M')
assert(size(38) == 'L')
assert(size(40) == 'M')
#checking if 42 cm comes under  M or L
assert(size(42) == 'M')
assert(size(42) == 'L')
assert(size(43) == 'L')
print("All is well (maybe!)\n")
