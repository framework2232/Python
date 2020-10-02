from tkinter import Tk,Frame,Label,Button

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




# makes the main window
mainwindow=Tk()
mainwindow.title("Name The App Here")
mainwindow.geometry("700x550")

# make main frame (inside main window)
mainframe=Frame(mainwindow,bg="#141414")
mainframe.pack(fill="both", expand=True)
mainwindow.update()

# Label = App Title - at the top of the frame - responsive
labelAppTitle=Label(mainframe,text=appTitle,bg="#141414",fg="green",pady=5)
labelAppTitle.config(font=("bold Arial",24))
labelAppTitle.bind('<Configure>', lambda e: labelAppTitle.config(wraplength=labelAppTitle.winfo_width()))
labelAppTitle.pack(fill="x")

# Label = App Description - under the App Title - responsive
frameAppDescription=Frame(mainframe,bg="#141414")
labelAppDescription=Label(frameAppDescription,text=appDescription,bg="#141414",fg="lightgrey",justify="left")
labelAppDescription.config(font=("Arial",12))
labelAppDescription.bind('<Configure>', lambda e: labelAppDescription.config(wraplength=labelAppDescription.winfo_width()))
labelAppDescription.pack(fill="both",padx=30,pady=0)
frameAppDescription.pack(fill="x")

# Label = App Instructions - under the App Description - responsive
frameAppInstructions=Frame(mainframe,bg="#141414")
labelAppInstructions=Label(frameAppInstructions,text=appInstructions,bg="#141414",fg="lightgrey")
labelAppInstructions.config(font=("Arial",14))
labelAppInstructions.bind('<Configure>', lambda e: labelAppInstructions.config(wraplength=labelAppInstructions.winfo_width()))
labelAppInstructions.pack(fill="both",padx=5,pady=20)
frameAppInstructions.pack(fill="x")

# FRAME = Lower frame - beneith the App Instructions
# lowerframe=Frame(mainframe)
# labelAppQueries=Label(lowerframe,bg="#141414")
# labelAppQueries.pack(fill="both")
# lowerframe.pack(fill="both")

# Label = App Queries - left hand side of app
frameAppQueries=Frame(mainframe,bg="#141414")
# labelAppQueries=Label(frameAppQueries)
button_index = Button(frameAppQueries,text="index.html",command=include_index,bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
button_style = Button(frameAppQueries,text="style.css",command=include_style,bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
button_robots = Button(frameAppQueries,text="robots.txt",command=include_robots,bg=buttBG,fg=buttFG,font=buttFONT,width=buttWIDTH,padx=buttPADX)
button_manifest = Button(frameAppQueries, text = "manifest.json", command = include_manifest, bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)
button_exit = Button(frameAppQueries, text = "Exit", command = build, bg = "grey", fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)
button_build = Button(frameAppQueries, text = "Build", command = build, bg = buttBG, fg = buttFG, font=buttFONT, width = buttWIDTH, padx = buttPADX)


frameAppQueries.pack(fill="x")


frameAppQueries.grid_columnconfigure(0,weight=1)
frameAppQueries.grid_columnconfigure(1,weight=2)
frameAppQueries.grid_columnconfigure(2,weight=1)

button_index.grid(row=1, column=0, pady = rowPADY)
button_style.grid(row=2, column=0, pady = rowPADY)
button_robots.grid(row=3, column=0, pady = rowPADY)
button_manifest.grid(row=4, column=0, pady = rowPADY)
button_exit.grid(row=5, column=1, pady = rowPADY)
button_build.grid(row=5, column=2, pady = rowPADY)



mainwindow.mainloop()