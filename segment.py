class Segment:
    def __init__(self, canvas, circle1, circle2):
        self.canvas = canvas
        self.circle1 = circle1
        self.circle2 = circle2
        self.canvas_id = self.canvas.create_line(circle1.x, circle1.y, circle2.x, circle2.y, fill="black", width=2)

    def update(self):
        self.canvas.coords(self.canvas_id, self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y)