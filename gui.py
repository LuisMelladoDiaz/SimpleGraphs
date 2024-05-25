import tkinter as tk
import math

from circle import Circle
from segment import Segment


class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Drawing Tool")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.draw_mode = tk.StringVar(value="circle")
        self.circle_count = 0

        self.setup_ui()
        self.draw_grid()
        self.add_legend()

        self.circles = []
        self.segments = []
        self.start_circle = None
        self.dragged_circle = None
        

        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)


    def setup_ui(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        draw_circle_btn = tk.Radiobutton(toolbar, text="Draw Circle", variable=self.draw_mode, value="circle")
        draw_circle_btn.pack(side=tk.LEFT)

        draw_segment_btn = tk.Radiobutton(toolbar, text="Draw Segment", variable=self.draw_mode, value="segment")
        draw_segment_btn.pack(side=tk.LEFT)
    
    def add_legend(self):
        legend_text = "Left click -> Draw Node/Edge\nRight Click -> Move Node \nDouble Right Click -> Rename Node\nMouse Wheel Click -> Change Color"
        legend_label = tk.Label(self.root, text=legend_text, anchor="se", justify="right", bg="lightgrey", fg="black")
        legend_label.pack(side=tk.RIGHT, padx=10, pady=10)

    def draw_grid(self):
        for i in range(0, 800, 20):
            self.canvas.create_line(i, 0, i, 600, fill="lightgray")
        for i in range(0, 600, 20):
            self.canvas.create_line(0, i, 800, i, fill="lightgray")

    def on_canvas_click(self, event):
        x, y = self.snap_to_grid(event.x, event.y)
        if self.draw_mode.get() == "circle":
            self.circle_count += 1
            circle_name = f"Circulo {self.circle_count}"
            self.draw_circle(x, y, 30, circle_name)
        elif self.draw_mode.get() == "segment":
            self.handle_segment_mode(x, y)
    

    def on_canvas_drag(self, event):
        if self.dragged_circle:
            x, y = self.snap_to_grid(event.x, event.y)
            self.move_circle(x, y)

    def on_canvas_release(self, event):
        self.dragged_circle = None

    def snap_to_grid(self, x, y):
        grid_size = 20
        return (x // grid_size) * grid_size, (y // grid_size) * grid_size

    def draw_circle(self, x, y, radius, name, color="black"):  
        circle = Circle(self.canvas, x, y, radius, name, self.root, color)
        self.circles.append(circle)


    def handle_segment_mode(self, x, y):
        for circle in self.circles:
            if self.is_within_circle(circle, x, y):
                if not self.start_circle:
                    self.start_circle = circle
                else:
                    if self.start_circle != circle:
                        segment = Segment(self.canvas, self.start_circle, circle)
                        self.segments.append(segment)
                        self.start_circle.segments.append(segment)
                        circle.segments.append(segment)
                        self.start_circle = None
                        break

    def is_within_circle(self, circle, x, y):
        distance = math.sqrt((circle.x - x) ** 2 + (circle.y - y) ** 2)
        return distance <= circle.radius

    def move_circle(self, x, y):
        self.dragged_circle.move(x, y)