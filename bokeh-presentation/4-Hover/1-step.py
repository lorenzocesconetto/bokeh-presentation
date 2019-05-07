"""Selection color"""
import numpy as np
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file, show

x = np.random.random(100)
y = np.random.random(100)

plot = figure(tools='crosshair, box_select, lasso_select')

plot.circle(x, y, size=15, selection_color='green')

output_file('hover.html')

show(plot)




