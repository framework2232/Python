from tkinter import *

my_window = Tk()
my_window.title('Building a Basic Website Structure')

# make window full page.
width_value = my_window.winfo_screenwidth()
height_value = my_window.winfo_screenheight()
my_window.geometry("%dx%d+0+0" % (width_value, height_value))

# if checkboxes are checked or not and what to do if they are checked
def show():  
    if var_checkbox_index.get() == 1:
        myResult = Label(my_window, text = "index.html")
        myResult.pack()

    if var_checkbox_style.get() == 1:
        myResult = Label(my_window, text = "style.css")
        myResult.pack()

    if var_checkbox_robots.get() == 1:
        myResult = Label(my_window, text = "robots.txt")
        myResult.pack()

    if var_checkbox_manifest.get() == 1:
        myResult = Label(my_window, text = "manifest.json")
        myResult.pack()
    

# declare variables as intergers
var_checkbox_index = IntVar() 
var_checkbox_style = IntVar()
var_checkbox_robots = IntVar()
var_checkbox_manifest = IntVar()


mainTitle = Label (my_window, text = "Basic Website Structure", font = "bold 32")

# define checkboxes and default as selected
checkbox_index      = Checkbutton(my_window, text = "index.html", variable = var_checkbox_index, font="24" )
checkbox_index.select()
checkbox_style      = Checkbutton(my_window, text = "style.css", variable = var_checkbox_style, font="24" )
checkbox_style.select()
checkbox_robots     = Checkbutton(my_window, text = "robots.txt", variable = var_checkbox_robots, font="24" )
checkbox_robots.select()
checkbox_manifest   = Checkbutton(my_window, text = "manifest.json", variable = var_checkbox_manifest, font="24" )
checkbox_manifest.select()


myButton    = Button(my_window, text = "Show Selection", command = show, bg = "green", fg = "white", font = "bold")

        
# display items on the screen
mainTitle.pack()
checkbox_index.pack()
checkbox_style.pack()
checkbox_robots.pack()
checkbox_manifest.pack()
myButton.pack()


my_window.mainloop()