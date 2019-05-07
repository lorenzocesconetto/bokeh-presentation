"""Configurando a aparencia da linha e sobrepondo desenhos"""
from bokeh.io import output_file, show
from bokeh.plotting import figure

plot = figure(x_axis_label='Dados de X', y_axis_label='Dados de Y')

plot.line([1, 2, 3, 4, 5], [8, 6, 5, 2, 3], color='#44aa99', alpha=.6, line_width=3)
plot.circle_x([1, 2, 3, 4, 5], [8, 6, 5, 2, 3], fill_color='#ffffff', color='#aa4499', alpha=.5, size=16)

output_file('line.html')

show(plot)



