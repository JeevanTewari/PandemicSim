# to run:
# python csvGen.py & python 2dplot.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from multiprocessing import Process
import csv, random, time, os

def animate(i):
	data = pd.read_csv('data.csv')
	x = data['day']
	y1 = data['healthy']
	y2 = data['infected']
	y3 = data['removed']

	plt.cla()
	plt.plot(x, y1, label = 'healthy')
	plt.plot(x, y2, label = 'infected')
	plt.plot(x, y3, label = 'removed')

	plt.legend(loc = 'upper left')
	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 100)
plt.show()

## use tkinter to automate the script and make it interactive?
## have popup summary showing percent unaffected, removed population etc.
## if mortality rate is this --> number of dead is this?