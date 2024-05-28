import tkinter as tk
import math
import csv
from tkinter import filedialog
from circle import Circle
from graph_converter import draw_graph
from segment import Segment


class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Drawing Tool")
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.draw_mode = tk.StringVar(value="edit")  # Set the default mode to "edit"
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

    def on_save(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            with open(filename, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)

                for circle in self.circles:
                    writer.writerow(['NODE', circle.name, circle.color])
                
                for segment in self.segments:
                    writer.writerow(['EDGE', segment.circle1.name, segment.circle2.name, segment.direction, segment.weight])

            draw_graph(filename)


    def setup_ui(self):
        toolbar = tk.Frame(self.root)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        draw_circle_btn = tk.Radiobutton(toolbar, text="Draw Node", variable=self.draw_mode, value="circle", command=lambda: self.change_cursor("tcross"))
        draw_circle_btn.pack(side=tk.LEFT)

        draw_segment_btn = tk.Radiobutton(toolbar, text="Draw Edge", variable=self.draw_mode, value="segment", command=lambda: self.change_cursor("plus"))
        draw_segment_btn.pack(side=tk.LEFT)

        delete_btn = tk.Radiobutton(toolbar, text="Delete", variable=self.draw_mode, value="delete", command=lambda: self.change_cursor("circle"))
        delete_btn.pack(side=tk.LEFT)

        edit_btn = tk.Radiobutton(toolbar, text="Edit", variable=self.draw_mode, value="edit", command=lambda: self.change_cursor("arrow"))
        edit_btn.pack(side=tk.LEFT)

        button = tk.Button(toolbar, text="SAVE", command=lambda: self.on_save())
        button.pack(side=tk.LEFT)


    def change_cursor(self, cursor_type):
        self.root.config(cursor=cursor_type)
    
    def add_legend(self):
        legend_text = "Left click -> Draw Node/Edge\nRight Click -> Move Node \nDouble Right Click -> Change name/weight\nMouse Wheel Click -> Change Color/Direction"
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
        elif self.draw_mode.get() == "delete":
            self.handle_delete_mode(x, y)
        elif self.draw_mode.get() == "edit":
            pass

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
                        segment = Segment(self.canvas, self.start_circle, circle, self.root)
                        self.segments.append(segment)
                        self.start_circle.segments.append(segment)
                        circle.segments.append(segment)
                        self.start_circle = None
                        break

    def handle_delete_mode(self, x, y, tolerance=20):
        for circle in self.circles:
            distance = math.sqrt((circle.x - x) ** 2 + (circle.y - y) ** 2)
            if distance <= circle.radius + tolerance:
                self.delete_circle(circle)
                return
        for segment in self.segments:
            if self.is_on_segment(segment, x, y):
                self.delete_segment(segment)
                return

    def is_within_circle(self, circle, x, y):
        distance = math.sqrt((circle.x - x) ** 2 + (circle.y - y) ** 2)
        return distance <= circle.radius

    def is_on_segment(self, segment, x, y):
        # Check if point (x, y) is close to the line segment
        x1, y1 = segment.circle1.x, segment.circle1.y
        x2, y2 = segment.circle2.x, segment.circle2.y
        distance = self.point_to_segment_distance(x, y, x1, y1, x2, y2)
        return distance < 20 #threshold
    
    def point_to_segment_distance(self, px, py, x1, y1, x2, y2):
        # Calcula la magnitud de la línea
        line_mag = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        # Si la magnitud de la línea es casi cero, la distancia es infinita (no hay segmento)
        if line_mag < 1e-6:
            return float('inf')
        
        # Calcula la proyección del punto (px, py) en la línea
        u = ((px - x1) * (x2 - x1) + (py - y1) * (y2 - y1)) / (line_mag ** 2)
        
        # Asegúrate de que la proyección esté dentro del segmento [0, 1]
        u = max(0, min(1, u))
        
        # Calcula las coordenadas del punto proyectado en la línea
        ix = x1 + u * (x2 - x1)
        iy = y1 + u * (y2 - y1)
        
        # Calcula la distancia desde el punto (px, py) al punto proyectado (ix, iy)
        distance = math.sqrt((px - ix) ** 2 + (py - iy) ** 2)
        
        return distance

    def delete_circle(self, circle):
        self.circles.remove(circle)
        for segment in circle.segments[:]:
            self.delete_segment(segment)
        circle.delete(circle)

    def delete_segment(self, segment):
        self.segments.remove(segment)
        segment.delete(segment)

    def move_circle(self, x, y):
        self.dragged_circle.move(x, y)

