import tkinter as tk

class Segment:
    def __init__(self, canvas, circle1, circle2, root, weight=0, color="black"):
        self.canvas = canvas
        self.circle1 = circle1
        self.circle2 = circle2
        self.color = color
        self.weight = weight
        self.direction = "none"  # States: "none", "to_origin", "to_destination", "bidirectional"
        self.canvas_id = self.canvas.create_line(circle1.x, circle1.y, circle2.x, circle2.y, fill=color, width=2)
        
        # Calculate text position
        self.text_x = (self.circle1.x + self.circle2.x) / 2
        self.text_y = (self.circle1.y + self.circle2.y) / 2
        
        # Adding rectangle for the background
        self.rect_id = self.canvas.create_rectangle(self.text_x - 30, self.text_y - 10, 
                                                    self.text_x + 30, self.text_y + 10, 
                                                    fill="black")
        # Adding text for the weight
        self.text_id = self.canvas.create_text(self.text_x, self.text_y, 
                                               text=f"weight: {self.weight}", fill="white")

        self.editing_weight = False
        self.edit_segment_weight = tk.Entry(root, bg="black", fg="white")

        self.bind_events(root)

    def bind_events(self, root):
        self.canvas.tag_bind(self.canvas_id, "<Button-2>", lambda event, segment=self: self.on_wheel_click(event, segment))
        self.canvas.tag_bind(self.canvas_id, "<Enter>", lambda event, segment=self: self.on_enter(event, segment))
        self.canvas.tag_bind(self.canvas_id, "<Leave>", lambda event, segment=self: self.on_leave(event, segment))
        self.canvas.tag_bind(self.canvas_id, "<Double-Button-3>", lambda event: self.on_segment_double_right_click(event))
        
        self.edit_segment_weight.bind("<Return>", self.update_segment_weight)
        self.edit_segment_weight.bind("<FocusOut>", self.update_segment_weight)

        self.root_click_handler = root.bind("<Button-1>", self.on_root_click)

    def on_root_click(self, event):
        if not self.editing_weight:
            return
        if event.widget != self.edit_segment_weight:
            self.update_segment_weight(None)

    def on_wheel_click(self, event, segment):
        directions = ["none", "to_origin", "to_destination", "bidirectional"]
        current_index = directions.index(segment.direction)
        next_index = (current_index + 1) % len(directions)
        segment.direction = directions[next_index]
        segment.update_direction()

    def update_direction(self):
        self.canvas.delete(self.canvas_id)
        self.canvas.delete(self.text_id)
        self.canvas.delete(self.rect_id)
        
        if self.direction == "none":
            self.canvas_id = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, fill=self.color, width=2)
        elif self.direction == "to_origin":
            self.canvas_id = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, fill=self.color, width=2, arrow="last")
        elif self.direction == "to_destination":
            self.canvas_id = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, fill=self.color, width=2, arrow="first")
        elif self.direction == "bidirectional":
            self.canvas_id = self.canvas.create_line(self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y, fill=self.color, width=2, arrow="both")

        # Calculate new text position
        self.text_x = (self.circle1.x + self.circle2.x) / 2
        self.text_y = (self.circle1.y + self.circle2.y) / 2

        # Add background rectangle
        self.rect_id = self.canvas.create_rectangle(self.text_x - 30, self.text_y - 10, 
                                                    self.text_x + 30, self.text_y + 10, 
                                                    fill="black")
        # Add weight text
        self.text_id = self.canvas.create_text(self.text_x, self.text_y, 
                                               text=f"weight: {self.weight}", fill="white")

        self.bind_events(self.edit_segment_weight.master)

    def update(self):
        self.canvas.coords(self.canvas_id, self.circle1.x, self.circle1.y, self.circle2.x, self.circle2.y)
        self.text_x = (self.circle1.x + self.circle2.x) / 2
        self.text_y = (self.circle1.y + self.circle2.y) / 2
        self.canvas.coords(self.text_id, self.text_x, self.text_y)
        self.canvas.coords(self.rect_id, self.text_x - 30, self.text_y - 10, self.text_x + 30, self.text_y + 10)

    def on_enter(self, event, segment):
        self.canvas.itemconfig(self.canvas_id, width=4)
        self.canvas.itemconfig(segment.canvas_id, fill="blue")

    def on_leave(self, event, segment):
        self.canvas.itemconfig(self.canvas_id, width=2)
        self.canvas.itemconfig(segment.canvas_id, fill="black")

    def on_segment_double_right_click(self, event):
        if not self.editing_weight:
            self.edit_segment_weight.delete(0, tk.END)
            self.edit_segment_weight.insert(0, str(self.weight))
            self.edit_segment_weight.place(x=self.text_x-30, y=self.text_y-10, width=60)
            self.edit_segment_weight.focus_set()
            self.editing_weight = True

    def update_segment_weight(self, event):
        if self.editing_weight:
            try:
                new_weight = float(self.edit_segment_weight.get())
                self.weight = new_weight
                self.canvas.itemconfig(self.text_id, text=f"weight: {self.weight}")
            except ValueError:
                pass
            self.edit_segment_weight.place_forget()
            self.editing_weight = False

    def delete(self, segment):
        self.canvas.delete(segment.canvas_id)
        self.canvas.delete(segment.text_id)
        self.canvas.delete(segment.rect_id)

    def __str__(self):
        return f"Node(origin={self.circle1.name}, target={self.circle2.name}, direction={self.direction}, weight={self.weight})"