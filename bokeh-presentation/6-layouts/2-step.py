"""gridplot"""
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show


p1 = figure(title='This is plot 1')
p2 = figure(title='This is plot 2')
p3 = figure(title='This is plot 3')
p4 = figure(title='This is plot 4')


layout = gridplot(
    [
        [None, p2],
        [p3, p4]
    ]
)

show(layout)


