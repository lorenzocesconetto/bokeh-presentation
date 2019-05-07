"""Configurando label e titulo"""
from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure(title='My title', x_axis_label='Dados de X', y_axis_label='Dados de Y')

show(plot)


