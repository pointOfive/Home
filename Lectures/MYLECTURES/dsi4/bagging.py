
# IT IS NOT INITIALIZED PROPERLY (HAVE TO MOVE A SLIDER FIRST)
# STRANGE BEHAVIOR WHEN POLYNOMIAL DEGREES>12 AT x EXTREMES

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.plotting import ColumnDataSource, Figure
from bokeh.models.widgets import Select, TextInput, Slider
from bokeh.models import InputWidget
from bokeh.models.callbacks import Callback
import numpy as np
from numpy import random

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


def get_y(X, power, coeff):
    return reduce(lambda x, y: x+y, [coeff[i]*X**i for i in range(power)])


x_points = 200
x = np.linspace(0,20,x_points)
y = x+5*np.sin(x)
err = np.random.normal(size=x_points)

p = Figure(title="bagging demo", plot_height=400, plot_width=800, y_range=(-5,30))



slider_degrees = Slider(start=1, end=20, step=1, value=5, title="Degrees")
slider_lines = Slider(start=1, end=50, step=1, value=10, title="Lines")
slider_points = Slider(start=1, end=100, step=1, value=20, title="Points")
D=5
L=10
N=20

# The datapoints
source_1 = ColumnDataSource(data=dict(x=x, y=x+err+5*np.sin(x)))
p.scatter(x='x', y='y', source=source_1, color="#2222aa", line_width=3)

# The function where the datapoints come from
source_2 = ColumnDataSource(data=dict(x=x, y=x+5*np.sin(x)))
p.line(x='x', y='y', source=source_2, color="#2222aa", line_width=1)
source_2.data = dict(x=x, y=x+5*np.sin(x))

# The bootstrap lines
source_3 = ColumnDataSource(data=dict(xs=[ [], [] ], ys=[ [], [] ]))
p.multi_line(xs='xs', ys='ys', source=source_3, color="#ff9696", line_width=0)

# The average
source_4 = ColumnDataSource(data=dict(x=x, y=x+1))
p.line(x='x', y='y', source=source_4, color="#f44242", line_width=2)


def update(attrname, old, new):

    D=slider_degrees.value
    L=slider_lines.value
    N=slider_points.value

    list_xy=[]
    for i in range(L):
        filt = np.random.randint(0, len(x), N)
        list_xy.append((x[filt], (y+err)[filt]))


    model = Pipeline([('poly', PolynomialFeatures(degree=D)), ('linear', LinearRegression(fit_intercept=False))])

    coeff_list=[]
    for xy in list_xy:
        model = model.fit(xy[0][:, np.newaxis], xy[1])
        coeff_list.append(model.named_steps['linear'].coef_)


    source_1.data = dict(x=x[filt], y=(x + err +  5*np.sin(x))[filt])

    vtot=np.zeros(len(x))
    xs=[]
    ys=[]
    for i in range(L):
        v=np.array(get_y(x, len(coeff_list[i]),coeff_list[i]))
        vtot+=v

        xs.append(x)
        ys.append(v)

    source_3.data = dict(xs=xs, ys=ys)
    source_4.data = dict(x=x, y=vtot/float(len(coeff_list)))


for w in [slider_degrees, slider_lines, slider_points]:
    w.on_change('value', update)

layout = column(row(p), row(slider_degrees, slider_lines, slider_points, width=400))

curdoc().add_root(layout)
