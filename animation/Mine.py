import tkinter as tk


class Mine:
    def __init__(self, canvas, mine_coord: tuple[int, int]) -> None:
        """Initialise mine at given coordinates"""
        self.x1 = mine_coord[0] - 2
        self.x2 = mine_coord[1] - 2
        self.y1 = mine_coord[0] + 2
        self.y2 = mine_coord[1] + 2
        self.canvas = canvas
        self.mine = canvas.create_rectangle(self.x1, self.x2, self.y1, self.y2, fill="red")