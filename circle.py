import tkinter as tk

class Circle:
    def __init__(self, canvas, x, y, radius, name, root, color="black"):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = radius
        self.name = name
        self.color = color  
        self.canvas_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=self.color, width=3)
        self.text_id = self.canvas.create_text(x, y - radius - 10, text=self.name, fill=self.color)  # Etiqueta de texto encima del círculo
        self.segments = []
        self.editing_name = False

        self.canvas.tag_bind(self.canvas_id, "<Enter>", self.on_enter)
        self.canvas.tag_bind(self.canvas_id, "<Leave>", self.on_leave)
        self.canvas.tag_bind(self.canvas_id, "<Button-3>", self.on_circle_click)
        self.canvas.tag_bind(self.canvas_id, "<B3-Motion>", self.on_circle_drag)
        self.canvas.tag_bind(self.canvas_id, "<Double-Button-3>", self.on_circle_double_right_click)
        self.canvas.tag_bind(self.canvas_id, "<Button-2>", lambda event, circle=self: self.on_wheel_click(event, circle))  # Bind del evento de hacer clic con la rueda del ratón

        self.edit_circle_entry = tk.Entry(root)
        self.edit_circle_entry.bind("<Return>", self.update_circle_name)
        self.edit_circle_entry.bind("<FocusOut>", self.update_circle_name)

    def on_enter(self, event):
        self.canvas.itemconfig(self.canvas_id, width=4)
        self.canvas.itemconfig(self.canvas_id, outline="blue")

    def on_leave(self, event):
        self.canvas.itemconfig(self.canvas_id, width=3)  
        self.canvas.itemconfig(self.canvas_id, outline="black") 

    def on_circle_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_circle_drag(self, event):
        if not self.editing_name:  
            dx = event.x - self.start_x
            dy = event.y - self.start_y

            self.move(self.x + dx, self.y + dy)
            self.start_x = event.x
            self.start_y = event.y

    def move(self, new_x, new_y):
        dx = new_x - self.x
        dy = new_y - self.y
        self.canvas.move(self.canvas_id, dx, dy)
        self.canvas.move(self.text_id, dx, dy) 
        self.x = new_x
        self.y = new_y
        for segment in self.segments:
            segment.update()

    def on_circle_double_right_click(self, event):
        if not self.editing_name:
            self.edit_circle_entry.delete(0, tk.END)
            self.edit_circle_entry.insert(0, self.name)
            self.edit_circle_entry.place(x=self.x - 30, y=self.y - 50, width=60)
            self.edit_circle_entry.focus_set()
            self.editing_name = True

    def update_circle_name(self, event):
        if self.editing_name:
            new_name = self.edit_circle_entry.get()
            if new_name.strip() and new_name != self.name:  # Asegurarse de que el nuevo nombre no esté vacío y sea diferente
                self.name = new_name
                self.canvas.itemconfig(self.text_id, text=new_name)
            self.edit_circle_entry.place_forget()
            self.editing_name = False

    def on_wheel_click(self, event, circle):
        colors = ["red", "blue", "green", "orange", "purple", "black", "cyan", "magenta", "brown", "grey", "yellow", "pink"]
        current_color_index = colors.index(circle.color)
        next_color_index = (current_color_index + 1) % len(colors)
        next_color = colors[next_color_index]
        circle.color = next_color
        self.canvas.itemconfig(circle.canvas_id, fill=circle.color)  

    def delete(self, circle):
        self.canvas.delete(circle.canvas_id)
        self.canvas.delete(circle.text_id)

    def __str__(self):
        return f"Node(name={self.name}, color={self.color})"
