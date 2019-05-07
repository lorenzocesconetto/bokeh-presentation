"""Example of bokeh application with callback and widget"""
import numpy as np
from bokeh.layouts import column
from bokeh.plotting import figure
from bokeh.models import Slider
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource

######################################
# Create Plots and Widgets
######################################
num = 300
source = ColumnDataSource(
    {
        'x': np.random.random(num),
        'y': np.random.random(num)
    }
)

p = figure()
p.circle(x='x', y='y', source=source, size=5)
slider = Slider(start=100, end=1000, step=10, value=num, title='num of points')

######################################
# Create Call Backs
######################################
def callback(attr, old, new):
    num = slider.value
    source.data = {'x': np.random.random(num), 'y': np.random.random(num)}
slider.on_change('value', callback)

######################################
# Arrange plots and widgets in a layout
######################################
layout = column(slider, p)

curdoc().add_root(layout)


