"""

Here is the core of game. All controllers must link to this file.

"""
import random


class Figure:
    def __init__(self, color, position):
        self.position = position
        self.color = color

    def move(self, step):
        self.position += step


class PositionIterator:
    def __iter__(self):
        return self

    def __init__(self, counter=1):
        self.counter = counter

    def __next__(self):
        if self.counter < self.size:
            self.counter += 1
            return 1
        else:
            self.counter = 1


class Desk:
    def __init__(self, size=24, figure_count=15):
        self.size = size
        self.figure_count = figure_count

    def create_desk(self):
        current_desk = []
        for i in range(self.size):
            current_desk += ['None']
        return current_desk

    def put_figures(self, black=None, white=None):
        for i in range(self.figure_count):
            white += Figure("White", 1)
            black += Figure("Black", 13)
            current_desk[0] += white.color
            current_desk[12] += black.color

    def output(self, current_map):
        print(current_map[len(current_map)+1:len(current_map)//2-1:-1])
        print(current_map[0:len(current_map)//2])


def throw_cube():
    cube_a = random.randint(1, 7)
    cube_b = random.randint(1, 7)
    return cube_a, cube_b


# First of all, this function check ability to move on the first threw up cube
# After it starts check_b which checks ability to move figure to position by second threw up cube
# This func must be called before every round and after every cube threw
"""def check(cube_a: int, cube_b: int, round_color, current_desk):
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

    return check_a() and check_b()"""


"""Actually, func in the top and in the bot do the same functions. Maybe later I'll mind how to unite them"""


# Add  available figures into list to give choice to the player
def available_figures(current_color):
    positions = []
    for i in range(len(current_desk)):
        if current_color in current_desk[i]:
            if (current_color or 'None') in (current_desk[i + cube_b] or current_desk[i + cube_a]):
                positions += i


# This is complete function to replace the figure. Also we need split functions to throw and to put


if __name__ == '__main__':
    desk = Desk()
    current_desk = desk.create_desk()
    desk.put_figures()
    desk.output(current_desk)
    print(current_desk)
    """### Round 1:
    cube_a, cube_b = throw_cube()
    check(cube_a, cube_b, "White", current_desk)
    replace_figure(0, cube_a, current_desk)  # Actually, it's just a test throw.
    desk.print_desk(current_desk)  # Real replace will be call
    print(len(current_desk))  # from Controller class"""
