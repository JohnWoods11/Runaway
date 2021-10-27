import math
from sympy import *
# do batch gradient descent then turn it into stochastic


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def calculate_energy(mine_locs: list, ball_loc: tuple) -> tuple:
    ball_energy = 0
    force_direction = [0, 0]
    for mine_loc in mine_locs:
        distance = calculate_distance(ball_loc[0], ball_loc[1], mine_loc[0], mine_loc[1])
        repulsive_force = 1 / (distance + 1)  # plus 1 because at distance 0 we want max energy (1 / 1 = 1)
        ball_energy += repulsive_force
        x_direction = (ball_loc[0] - mine_loc[0])
        y_direction = (ball_loc[1] - mine_loc[1])
        force_direction[0] += x_direction / abs(ball_loc[0] - mine_loc[0]) * repulsive_force if x_direction != 0 else 0
        force_direction[1] += (ball_loc[1] - mine_loc[1]) * repulsive_force
    ball_energy /= len(mine_locs)
    print(force_direction)
    return ball_energy


def calculate_gradient(mine_locs: list, ball_loc: tuple) -> tuple:
    move_x = (ball_loc[0] + 0.1, ball_loc[1])
    move_y = (ball_loc[0], ball_loc[1] + 0.1)

    fpx = 10 * (calculate_energy(mine_locs, ball_loc) - calculate_energy(mine_locs, move_x))
    fpy = 10 * (calculate_energy(mine_locs, ball_loc) - calculate_energy(mine_locs, move_y))

    gradient = [fpx, fpy]
    print(gradient)
    return gradient


mine_list = [(0, 2), (8, 2)]
ball_location = (-1, 2)


print(calculate_energy(mine_list, ball_location))



