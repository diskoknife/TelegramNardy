class Create_map:
    def __init__(self, desk_length=23):
        self.desk_length = desk_length

    def create_map(self):
        matr = [[0 for i in range(self.desk_length)] in range(2)]
        return matr

    def write_map(self, fis_num=15, black = "Black", white = "White"):
        line_sequence = {}
