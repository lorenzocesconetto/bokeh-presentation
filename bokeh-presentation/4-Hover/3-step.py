"""Hover Tool tips"""
import numpy as np
from bokeh.sampledata.iris import flowers
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.models import HoverTool
from bokeh.plotting import figure, output_file

hover = HoverTool(
    mode='vline',
    tooltips=[('species name', '@species'),
              ('petal length', '@petal_length'),
              ('sepal length', '@sepal_length'),
              ])

plot = figure(tools=[hover, 'crosshair, box_select, lasso_select'])

data_source = ColumnDataSource(flowers)

plot.circle_cross(x='petal_length', y='sepal_length', legend='species', source=data_source, size=10)
plot.legend.location = 'top_left'

output_file('hover.html')

show(plot)
