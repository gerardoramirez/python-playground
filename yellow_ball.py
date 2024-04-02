import tkinter as tk


class MovingBallApp:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=400, height=300)
        self.canvas.pack()

        # Calculate the center of the canvas
        self.x = self.canvas.winfo_reqwidth() / 2
        self.y = self.canvas.winfo_reqheight() / 2
        self.ball_radius = 20

        # Create the ball at the center of the canvas
        self.ball = self.create_ball()

        # Bind the mouse movement event to the handler
        self.canvas.bind('<Motion>', self.move_ball)

    def create_ball(self):
        ball = self.canvas.create_oval(self.x - self.ball_radius, self.y - self.ball_radius,
                                       self.x + self.ball_radius, self.y + self.ball_radius,
                                       fill='yellow')
        print(f"Ball created at ({self.x}, {self.y})")  # Debug print
        return ball

    def move_ball(self, event):
        # Move the ball to the right by 10 pixels
        self.canvas.move(self.ball, 10, 0)

        # Update the ball's x position
        self.x += 10

        # Debug print
        print(f"Ball moved to ({self.x}, {self.y})")

        # Prevent the ball from moving out of the canvas
        if self.x > self.canvas.winfo_width():
            self.x = self.ball_radius
            self.canvas.coords(self.ball, self.x - self.ball_radius, self.y - self.ball_radius,
                               self.x + self.ball_radius, self.y + self.ball_radius)


# Create the main window and run the application
root = tk.Tk()
app = MovingBallApp(root)
root.mainloop()
