# source: "Matplotlib Charts With Tkinter - Python Tkinter GUI Tutorial" by Codemy.com on YouTube
# LINK: 	https://youtu.be/8exB6Ly3nx0

from tkinter import *
from PIL import ImageTk, ImageTk
import numpy as np
import matplotlib.pyplot as plt

# setting up tkinter
root = Tk()
root.title('Title goes here')
root.geometry("400x200")


def graph():
	# generate random data with numPy
	house_prices = np.random.normal(200000, 25000, 5000)
	# call matplotlib
	plt.hist(house_prices, 50)
	plt.show()

# button generates graph in seperate window
my_button = Button(root, text="Text 1 goes here", command=graph)
my_button.pack()

# main loop
root.mainloop()
