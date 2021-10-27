import tkinter as tk
from RUNAWAY.animation import Window, Mine, Ball
import time

version = "Test"
window_width = 800
window_height = 600


ball_coords = [(10, 200), (300, 400)]
mine_coords = [(400, 200), (100, 300)]
ball_deltas = [(1, 1), (1, 1)]


class Runaway:
    def __init__(self, version, window_width, window_height):
        self.window = Window.Window(version, window_width, window_height)
        self.canvas = self.window.canvas
        self.balls = [Ball.Ball(self.canvas, ball) for ball in ball_coords]
        self.mines = [Mine.Mine(self.canvas, mine) for mine in mine_coords]
        self.canvas.pack()


    def move_balls(self, ball_deltas):
        for ball in range(len(self.balls)):
            self.balls[ball].move_ball(ball_deltas[ball])
            self.canvas.update()


runaway = Runaway(version, window_width, window_height)
i = 0
while i < 100:
    runaway.move_balls(ball_deltas)
    i += 1
    time.sleep(0.005)
tk.mainloop()



