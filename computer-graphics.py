from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk, width=800, height=400)
tk.title("drawing")
canvas.pack()
canvas.create_line(0, 0, 800, 800)
canvas.create_oval(80, 80, 400, 400, fill="red")
canvas.mainloop()