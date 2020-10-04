from tkinter import *

root = Tk()
root.geometry("800x500")
root.configure(bg="#141414")

my_canvas = Canvas(root, width=300, height="300", bg="white")
my_canvas.pack(pady="20")


# line = root
my_canvas.create_line(10, 20, 42, 20, fill="red", width="4")
# line = vertical
my_canvas.create_line(40, 20, 40, 162, fill="red", width="4")

my_canvas.create_line(40, 40, 60, 40, fill="red", width="4")
my_canvas.create_text(70, 40, text="index.html", fill="red", font=("bold 20"), anchor="w")

my_canvas.create_line(40, 80, 60, 80, fill="red", width="4")
my_canvas.create_text(70, 80, text="style.css", fill="red", font=("bold 20"), anchor="w")

my_canvas.create_line(40, 120, 60, 120, fill="red", width="4")
my_canvas.create_text(70, 120, text="robots.txt", fill="red", font=("bold 20"), anchor="w")

my_canvas.create_line(40, 160, 60, 160, fill="red", width="4")
my_canvas.create_text(70, 160, text="manifest.json", fill="red", font=("bold 20"), anchor="w")


root.mainloop()