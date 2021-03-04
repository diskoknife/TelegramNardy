"""

1. Creating an empty dict
2. Creating desk with 15 white things on the left-bot and 15 black things on the right-top bpx


"""


def create_map(desk_length=23, fis_num=15, black="Black", white="White"):
    desk_tuple = tuple(i for i in range(1, 25))
    desk_array = list("None" for i in range(desk_length))
    desk_array[0] = list(white for i in range(fis_num))
    desk_array[12] = list(black for i in range(fis_num))
    return desk_tuple, desk_array



current_map = create_map()
print(current_map)
