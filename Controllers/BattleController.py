"""

*Put some description for this file here*

"""
from Battle import Engine
from Battle.Engine import throw_cube, check, available_figures, replace_figure

init = Engine
current_map = Engine.Desk.create_desk()
colors = {
    0: "Black",
    1: "White"
}


# Class which just make sense
def choose_figure(available_figures):
    print("Available figures: ", available_figures)
    position = int(input("\n Enter the position from which you will go:"))
    if position not in available_figures:
        print("Try again")
        choose_figure(available_figures)
    else:
        return position


# I think I shouldn't put all the logic into one func. Pls refactor this
# TODO: REFACTOR ALL THE CONTROLLER CLASS
def round(color: bool):
    cube_a, cube_b = throw_cube()
    round_color = dict.get(colors, color)
    if check(cube_a, cube_b, round_color):
        choose_figure(available_figures(round_color))
        print("You can go to the ")
    else:
        round(color=not color)
