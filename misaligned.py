global last_pair_number;
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            lengthOfColors=len(minor_colors)
            pairNumber=i * lengthOfColors + j+1
            print(f'{pairNumber:<3} | {major:<7} | {minor}')
            # returning last pairnumber to check if it's 25
    return len(major_colors) * len(minor_colors),pairNumber

result,last_pair_number = print_color_map()
assert(result == 25)
# including testcase to check if its following 1 based index
assert(last_pair_number == 25)
print("All is well (maybe!)\n")
