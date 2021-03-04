"""

1. Creating an empty dict
2. Creating desk with 15 white things on the left-bot and 15 black things on the right-top bpx


"""

null_dict = {}


def create_map(desk_length=23, fis_num=15, black="Black", white="White"):
    for i in range(desk_length):
        null_dict.setdefault(i + 1, None)
    null_dict[1] = [white for j in range(fis_num)]
    null_dict[13] = [black for k in range(fis_num)]
    return null_dict


class Desk:
    create_map()
