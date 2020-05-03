# python program to create a Text Editor

# import everything from tkinter
from tkinter import *
# to open dialog box when required
from tkinter import filedialog


# function to save the file
def saveFile():
    f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if f is None:
        return
    try:
        textUserWrote = str(content.get(1.0, END))
        f.write(textUserWrote)
    except:
        print("Cannot save the file")
    finally:
        f.close()


# function to open a file
def openFile():
    try:
        t = filedialog.askopenfile(mode="r", title="Select File",
                                   filetypes=[("All Files", "*.*")])
        content.insert(END, t.read())
    except:
        print("Cannot load the file")
    finally:
        if t:
            t.close()


# function to close the window
def closeWindow():
    window.destroy()


# create a GUI window
window = Tk()
# give title to the window
window.title("MyTextEditor")

# create a menu
mainMenu = Menu(window)
# config the menu
window.config(menu=mainMenu)

# create an instance of menu
fileMenu = Menu(mainMenu)
# add it to main menu
mainMenu.add_cascade(label="File", menu=fileMenu)
# create a pull-down menu and add it to the file menu
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
# separate open and save sub menus of the file menu from close by a separator
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=closeWindow)
mainMenu.add_command(label="Help")

# textbox where user can see and write into
content = Text(window, width=100)

# display it at a particular position in the table
content.grid(row=0, column=0, padx=5, pady=5)

# display the window
window.mainloop()