"""row and column"""
from bokeh.layouts import row, column
from bokeh.plotting import figure, show


p1 = figure(title='This is plot 1')
p2 = figure(title='This is plot 2')
p3 = figure(title='This is plot 3')
p4 = figure(title='This is plot 4')

row_1 = row(p1, p2)
row_2 = row(p3, p4)

layout = column(row_1, row_2)

show(layout)


