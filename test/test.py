from tkinter import Tk, Label, Button

class firstGUI:
    def __init__(self, master):
        self.master = master
        master.title("testing tkinter")

        self.label = Label(master, text="first GUI")
        self.label.pack()

        self.greet_button = Button(master, text="hello", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="world", command=master.quit)
        self.close_button.pack()

    def greet(self):
        print("hello world")

root = Tk()
my_gui = firstGUI(root)
root.mainloop()
