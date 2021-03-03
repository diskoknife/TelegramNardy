null_dict = {}


def create_map(desk_length=23, fis_num=15, black="Black", white="White"):
    for i in range(desk_length):
        null_dict.setdefault(i+1, None)
    null_dict[1] = [white for j in range(fis_num)]
    null_dict[13] = [black for k in range(fis_num)]
    return null_dict