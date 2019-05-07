"""Tabs and Panels"""
from bokeh.layouts import row, column
from bokeh.plotting import figure, show
from bokeh.models.widgets import Panel, Tabs


p1 = figure(title='This is plot 1')
p2 = figure(title='This is plot 2')
p3 = figure(title='This is plot 3')
p4 = figure(title='This is plot 4')

first = Panel(child=row(p1, p2), title='first')
second = Panel(child=column(p3, p4), title='second')

layout = Tabs(tabs=[first, second])

show(layout)


