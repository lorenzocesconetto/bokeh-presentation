"""Desenhando um scatter"""
from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure(x_axis_label='Dados de X', y_axis_label='Dados de Y')

plot.circle_x([1, 2, 3, 4, 5], [8, 6, 5, 2, 3])

show(plot)


