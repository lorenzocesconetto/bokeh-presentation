"""ColumnDataSource é o objeto que o Bokeh utiliza p/ se comunicar com o JS, HTML."""
from bokeh.io import show
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers
from bokeh.models import ColumnDataSource
import numpy as np

data_source = ColumnDataSource({'x': np.random.random(100) * 8, 'y': np.random.random(100) * 8})
data_source_2 = ColumnDataSource(flowers)

p = figure()

p.triangle(x='x', y='y', source=data_source, color='red', alpha=.8, size=7)
p.x(x='petal_length', y='sepal_length', source=data_source_2, alpha=.8, size=10)

show(p)



