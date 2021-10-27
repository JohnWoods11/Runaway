import tkinter as tk


def create_window(version: str, window_width: int, window_height: int):
    window = tk.Tk()
    window.title(version)
    window.geometry(f'{window_width}x{window_height}')
    return window


def create_canvas(window):
    canvas = tk.Canvas(window)
    canvas.configure(bg="White")
    canvas.pack(fill="both", expand=True)
    return canvas


class Window:
    def __init__(self, version: str, width: int, height: int) -> None:
        self.window = create_window(version, width, height)
        self.canvas = create_canvas(self.window)
