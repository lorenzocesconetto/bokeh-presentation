"""Hover tool (tip)"""
import numpy as np
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show

hover = HoverTool(tooltips=None, mode='hline')

x = np.random.random(100)
y = np.random.random(100)

plot = figure(tools=[hover, 'crosshair, box_select, lasso_select'])

plot.circle(x, y, hover_color='red', size=15, selection_color='green')

output_file('hover.html')

show(plot)


