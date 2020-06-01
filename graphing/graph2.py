# source: matplotlib's example "Embedding in Tk"
# LINK: https://matplotlib.org/3.1.0/gallery/user_interfaces/embedding_in_tk_sgskip.html

import tkinter as tk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np


root = tk.Tk()
root.wm_title("Testing Matplotlib in Tk")

canvas = tk.Canvas(root, height=500, width=500)
canvas.pack()
example_frame = tk.Frame(root, bg='white')
example_frame.place(relx=0.1, rely=0.1, relwidth=0.4, relheight=0.4)

# matplotlib graph
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

# tk canvas packed into frame
graph = FigureCanvasTkAgg(fig, master=example_frame)  # A tk.DrawingArea.
graph.draw()
graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def _quit():
    root.quit()
    root.destroy()



button = tk.Button(master=root, text="Quit", command=_quit)
button.pack(side=tk.BOTTOM)

tk.mainloop()
