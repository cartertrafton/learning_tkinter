# first tkinter project
# based on "Learn Tkinter in 20 minutes" by Teacher of Computing on YouTube
# link: https://www.youtube.com/watch?v=_lSNIrR1nZU

from tkinter import *

# exit function
def close_window():
    window.destroy()
    exit()

# key down / click function
def click():
    entered_text=textentry.get()    # collect text from text entry box
    output.delete(0.0, END)
    try:
        definition = my_dictionary[entered_text]
    except:
        definition = "sorry, idk what u mean"
    output.insert(END, definition)

#### main
window = Tk()
window.title("my first tkinter project: title")
window.configure(background="black")

#### my photo
photo1 = PhotoImage(file="image.gif")
Label (window, image=photo1, bg="blue") .grid(row=0, column=0, sticky=W)

# create label
Label (window, text="Enter a word: ", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)

# create a text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)

# add a submit button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=W)

# create another label
Label (window, text="\nDefinition", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

# create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# dictionary
my_dictionary = {
    'hello':'whats up', 'test':'test', 'tkinter':'GUI'
    }

# exit label
Label (window, text="click to exit", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

# exit button
Button(window, text="EXIT", width=14, command=close_window) .grid(row=7, column=0, sticky=W)

##### run main loop
window.mainloop()