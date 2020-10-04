from tkinter import Tk,Label,Button,Canvas



# changes the colour of the button when clicked on
def include_index():
    if button_index["bg"] != "red":
        button_index["bg"] = "red"                
    else:        
        button_index["bg"] = "green"        
    return button_index   

def include_style():
    if button_style["bg"] != "red":
        button_style["bg"] = "red"                
    else:        
        button_style["bg"] = "green"        
    return button_style

def include_java():
    if button_java["bg"] != "red":
        button_java["bg"] = "red"                
    else:        
        button_java["bg"] = "green"        
    return button_java

def include_robots():
    if button_robots["bg"] != "red":
        button_robots["bg"] = "red"                
    else:        
        button_robots["bg"] = "green"        
    return button_robots
def include_manifest():
    if button_manifest["bg"] != "red":
        button_manifest["bg"] = "red"                
    else:        
        button_manifest["bg"] = "green"        
    return button_manifest
def build():
    pass
def endApp():
    pass


 
# defines variables as listed
appTitle = "App Heading Goes Here"
appDescription = "This app is for anyone who is building a website from complete scratch using HTML and CSS. The app reduces time in the basic setup of file structure by building a common folders and adding blank basic files.\n\nBy default, the files and folders include - index.html, style.css, robots.txt, mainfest.json and img folder."
appInstructions = "Click 'BUILD' for default, or deselect as required."
appQueriesTitle = "Query Container"


# define common button styles

buttBG = "green"
buttFG = "white"
buttFONT = "bold 14"
buttWIDTH = "10"
buttPADX = "10"
rowPADY = "5"

# define canvas colours
textFILL = "green"


# makes the main window
app=Tk()
app.title("Name The App Here")
app.geometry("900x550")
app.configure(bg="#141414")


# Label = App Title - at the top of the frame
labelAppHeading=Label(app,text=appTitle)
labelAppHeading.configure(font=("bold Arial",24))
labelAppHeading.configure(bg="#141414",fg="green",pady=5)


# Label = App Description - under the App Title
labelAppDescription=Label(app,text=appDescription,bg="#141414",fg="lightgrey")
labelAppDescription.config(font=("Arial",12), justify="left")
labelAppDescription.bind('<Configure>', lambda e: labelAppDescription.config(wraplength="800"))


# Label = App Instructions - under the App Description
labelAppInstructions=Label(app,text=appInstructions,bg="#141414",fg="lightgrey")
labelAppInstructions.config(font=("Arial",14))


# labelAppQueries=Label(app)

button_index = Button(app,text="index.html",command=include_index)
button_index.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)

button_style = Button(app,text="style.css",command=include_style)
button_style.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)

button_java = Button(app,text="main.js",command=include_java)
button_java.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)

button_robots = Button(app,text="robots.txt",command=include_robots)
button_robots.configure(bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)

button_manifest = Button(app, text = "manifest.json", command = include_manifest)
button_manifest.configure(bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)

button_exit = Button(app, text = "Exit", command = endApp)
button_exit.configure(bg = "grey", fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)

button_build = Button(app, text = "Build", command = build)
button_build.configure(bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)  


my_canvas = Canvas(app, width=400, height="220", bg="#141414")
my_canvas.update()

# line = root

my_canvas.create_text(140, 20, text="/webSite/", fill="green", font=("bold 20"), anchor="e")
my_canvas.create_line(150, 20, 192, 20, fill="green", width="4")
# line = vertical
my_canvas.create_line(190, 20, 190, 202, fill="green", width="4")




my_canvas.create_line(192, 40, 220, 40, fill=textFILL, width="4")
my_canvas.create_text(230, 40, text="index.html", fill="green", font=("bold 20"), anchor="w") 

my_canvas.create_line(192, 80, 220, 80, fill=textFILL, width="4")
my_canvas.create_text(230, 80, text="style.css", fill=textFILL, font=("bold 20"), anchor="w")

my_canvas.create_line(192, 120, 220, 120, fill=textFILL, width="4")
my_canvas.create_text(230, 120, text="robots.txt", fill=textFILL, font=("bold 20"), anchor="w")

my_canvas.create_line(192, 160, 220, 160, fill=textFILL, width="4")
my_canvas.create_text(230, 160, text="manifest.json", fill=textFILL, font=("bold 20"), anchor="w")

my_canvas.create_line(192, 200, 220, 200, fill=textFILL, width="4")
my_canvas.create_text(230, 200, text="main.js", fill=textFILL, font=("bold 20"), anchor="w")





# option to alter the weight of each column if needed
app.grid_columnconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)
app.grid_columnconfigure(2,weight=1)


# control the layout using grid
labelAppHeading.grid(row=1, column=0, columnspan=3)
labelAppDescription.grid(row=2, column=0, columnspan=3)
labelAppInstructions.grid(row=3, column=0, columnspan=3, pady="30")
button_index.grid(row=4, column=0, pady = rowPADY)
button_style.grid(row=5, column=0, pady = rowPADY)
button_robots.grid(row=6, column=0, pady = rowPADY)
button_manifest.grid(row=7, column=0, pady = rowPADY)
button_java.grid(row=8, column=0, pady = rowPADY)
button_exit.grid(row=9, column=1, pady = rowPADY)
button_build.grid(row=9, column=2, pady = rowPADY)
my_canvas.grid(row=4, column=1, columnspan=2, rowspan=4)


print(button_java["bg"])
if button_java["bg"] == "orange":
    print(button_java["bg"])
app.mainloop()