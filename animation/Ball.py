import tkinter as tk


class Ball:
    """Ball that can be placed on a canvas and moved"""

    def __init__(self, canvas, ball_coord: tuple[int, int]) -> None:
        """Initialise ball at given coordinates"""
        self.x1 = ball_coord[0] - 3
        self.x2 = ball_coord[1] - 3
        self.y1 = ball_coord[0] + 3
        self.y2 = ball_coord[1] + 3
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.x2, self.y1, self.y2, fill="blue")

    def move_ball(self, deltas: tuple[int, int]) -> None:
        """Move ball in x and y direction"""
        delta_x = deltas[0]
        delta_y = deltas[1]
        self.canvas.move(self.ball, delta_x, delta_y)

