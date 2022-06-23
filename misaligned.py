global last_pair_number;
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            # returning last pairnumber to check if it's 25
    return len(major_colors) * len(minor_colors),i * 5 + j


result,last_pair_number = print_color_map()
assert(result == 25)
# including testcase to check if its following 1 based index
assert(last_pair_number == 25)
print("All is well (maybe!)\n")
