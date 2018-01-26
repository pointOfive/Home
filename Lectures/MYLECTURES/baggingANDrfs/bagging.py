from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.plotting import ColumnDataSource, Figure
from bokeh.models.widgets import Select, TextInput, Slider
import numpy as np
from numpy import random
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from functools import reduce


def get_y(X, power, coeff):
    return reduce(lambda x, y: x+y, [coeff[i]*X**i for i in range(power)])

def func(x):
    return x+5*np.sin(x)


x_points = 200
x = np.linspace(0,20,x_points)
err = np.random.normal(size=x_points)

p = Figure(title="bagging demo", plot_height=400, plot_width=800, y_range=(-5,30))

slider_degrees = Slider(start=1, end=10, step=1, value=5, title="Degrees")
slider_lines = Slider(start=1, end=50, step=1, value=10, title="Lines")
slider_points = Slider(start=1, end=100, step=1, value=20, title="Points")

# The datapoints
source_points = ColumnDataSource(data=dict(x=x, y=func(x)+err))
p.scatter(x='x', y='y', source=source_points, color="#2222aa", line_width=3)

# The function where the datapoints come from
source_function = ColumnDataSource(data=dict(x=x, y=func(x)))
p.line(x='x', y='y', source=source_function, color="#2222aa", line_width=1)

# The bootstrap lines
source_lines = ColumnDataSource(data=dict(xs=[ [], [] ], ys=[ [], [] ]))
p.multi_line(xs='xs', ys='ys', source=source_lines, color="#ff9696", line_width=0)

# The average
source_avg = ColumnDataSource(data=dict(x=[], y=[]))
p.line(x='x', y='y', source=source_avg, color="#f44242", line_width=2)


def update(attrname, old, new):
    D=slider_degrees.value
    L=slider_lines.value
    N=slider_points.value

    list_xy=[]
    for i in range(L):
        filt = np.random.randint(0, len(x), N)
        list_xy.append((x[filt], (func(x)+err)[filt]))

    model = Pipeline([('poly', PolynomialFeatures(degree=D)), ('linear', LinearRegression(fit_intercept=False))])

    coeff_list=[]
    for xy in list_xy:
        model = model.fit(xy[0][:, np.newaxis], xy[1])
        coeff_list.append(model.named_steps['linear'].coef_)

    source_points.data = dict(x=x[filt], y=(func(x) + err)[filt])

    vtot=np.zeros(len(x))
    xs=[]
    ys=[]
    for i in range(L):
        v=np.array(get_y(x, len(coeff_list[i]),coeff_list[i]))
        vtot+=v
        xs.append(x)
        ys.append(v)

    source_lines.data = dict(xs=xs, ys=ys)
    source_avg.data = dict(x=x, y=vtot/float(len(coeff_list)))


for w in [slider_degrees, slider_lines, slider_points]:
    w.on_change('value', update)

layout = column(p, slider_degrees, slider_lines, slider_points)
curdoc().add_root(layout)
