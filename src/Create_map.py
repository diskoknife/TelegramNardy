class Create_map:
    def __init__(self, desk_length=23, white=15, black=15):
        self.desk_length = desk_length
        self.white = white
        self.black = black


    def create_map(self):
        matr = [[0 for i in range(self.desk_length)] in range(2)]
        return matr

    def write_map(self):
        with open('map', 'w') as f:
            f.write(self.create_map())

# TODO:split an existing matrix as a 2 lists