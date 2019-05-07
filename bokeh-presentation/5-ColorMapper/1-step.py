"""Color accordingly to class and Bokeh built-in Palettes"""
from bokeh.models import CategoricalColorMapper, ColumnDataSource
from bokeh.palettes import Magma
from bokeh.sampledata.iris import flowers as df
from bokeh.plotting import figure
from bokeh.io import show

source_data = ColumnDataSource(df)

color_mapper = CategoricalColorMapper(
    factors=['setosa', 'virginica', 'versicolor'],
    palette=Magma[3]
)

plot = figure()
plot.circle('petal_length', 'sepal_length', source=source_data, size=10,
            color={'field': 'species', 'transform': color_mapper})

show(plot)

