"""

Here is the core of game. All controllers must link to this file.

"""


class Desk(list):
    def __init__(self, white="White", black="Black", size=23, figure_count=15):
        super().__init__()
        self.figure_count = figure_count
        self.size = size
        self.black = black
        self.white = white

    def create_desk(self):
        desk = list(
            [['None'] for i in range(self.size)]
        )
        desk[0] = [self.white for i in range(self.figure_count)]
        desk[12] = [self.black for i in range(self.figure_count)]
        return desk

    @staticmethod
    def print_desk(current_desk):
        print(current_desk[len(current_desk):len(current_desk)//2:-1])
        print(current_desk[0:len(current_desk)//2])


desk = Desk()
current_desk = desk.create_desk()
print(current_desk)
desk.print_desk(current_desk)
