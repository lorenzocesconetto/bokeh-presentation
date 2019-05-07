"""Utilizando o numpy p/ desenhar"""
from bokeh.io import output_file, show
from bokeh.plotting import figure
import numpy as np


plot = figure(x_axis_label='Angle (radians)', y_axis_label='Sin(X) + Error')

x = np.linspace(start=0, stop=10, num=1000)
y = np.sin(x) + np.random.random(1000) * 0.2

plot.line(x, y, color='#44aa99', alpha=.6, line_width=1)

output_file('line.html')

show(plot)



