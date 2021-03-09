"""

Here is the core of game. All controllers must link to this file.

"""
import random


class Desk(list):
    # Desk is a list of fixed size (maybe we should use NumPy to change list to array)
    # Class of Desk are initialize just once by a game
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
        desk[0] = [[self.white] for i in range(self.figure_count)]
        desk[12] = [[self.black] for i in range(self.figure_count)]
        return desk

    # This method must paint desk like 2 similar and mirrored parts
    # Just like in real game
    @staticmethod
    def print_desk(current_desk):
        print(current_desk[24:11:-1])
        print(current_desk[0:12])


def throw_cube():
    cube_a = random.randint(1, 7)
    cube_b = random.randint(1, 7)
    return cube_a, cube_b


# First of all, this function check ability to move on the first threw up cube
# After it starts check_b which checks ability to move figure to position by second threw up cube
# This func must be called before every round and after every cube threw
def check(cube_a: int, cube_b: int, round_color, current_desk):
    def check_a():
        for i in range(len(current_desk)):
            if round_color in current_desk[i]:
                if (round_color or 'None') in current_desk[i + cube_a]:
                    return True
        return False

    def check_b():
        for i in range(len(current_desk)):
            if round_color in current_desk[i]:
                if (round_color or 'None') in (current_desk[i + cube_b] or current_desk[i + cube_b + cube_a]):
                    return True
        return False

    return check_a() and check_b()


"""Actually, func in the top and in the bot do the same functions. Maybe later I'll mind how to unite them"""


# Add  available figures into list to give choice to the player
def available_figures(current_color):
    positions = []
    for i in range(len(current_desk)):
        if current_color in current_desk[i]:
            if (current_color or 'None') in (current_desk[i + cube_b] or current_desk[i + cube_a]):
                positions += i


# This is complete function to replace the figure. Also we need split functions to throw and to put
def replace_figure(threw_fig: int, position: int, current_desk: list):
    if current_desk[position] == 'None':
        current_desk[position] = current_desk[threw_fig][-1]
    else:
        current_desk[position].append(current_desk[threw_fig][-1])


if __name__ == '__main__':
    desk = Desk()
    current_desk = desk.create_desk()
    desk.print_desk(current_desk)
    ### Round 1:
    cube_a, cube_b = throw_cube()
    check(cube_a, cube_b, "White", current_desk)
    replace_figure(0, cube_a, current_desk)  # Actually, it's just a test throw.
    desk.print_desk(current_desk)  # Real replace will be call
    print(len(current_desk))  # from Controller class
