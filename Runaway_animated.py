import tkinter as tk
from RUNAWAY.animation import Window, Mine, Ball
import time

_version = "Test"
_window_width = 800
_window_height = 600


_ball_coords = [(10, 200), (300, 400)]
_mine_coords = [(400, 200), (100, 300)]
_ball_deltas = [(1, 1), (1, 1)]


class Runaway:
    def __init__(self, version: str, window_width: int, window_height: int,
                 ball_coords: list[tuple[int, int]], mine_coords: list[tuple[int, int]]) -> None:
        self.window = Window.Window(version, window_width, window_height)
        self.canvas = self.window.canvas
        self.balls = [Ball.Ball(self.canvas, ball) for ball in ball_coords]
        self.mines = [Mine.Mine(self.canvas, mine) for mine in mine_coords]
        self.canvas.pack()

    def move_balls(self, ball_deltas: list) -> None:
        for ball in range(len(self.balls)):
            self.balls[ball].move_ball(ball_deltas[ball])
            self.canvas.update()


runaway = Runaway(_version, _window_width, _window_height, _ball_coords, _mine_coords)
i = 0
while i < 100:
    runaway.move_balls(_ball_deltas)
    i += 1
    time.sleep(0.005)
tk.mainloop()



