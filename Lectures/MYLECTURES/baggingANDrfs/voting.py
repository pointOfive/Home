# run this with: bokeh serve --show voting.py

from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.plotting import ColumnDataSource, Figure
from bokeh.models.widgets import Slider
from scipy import stats

my_plot = Figure(title="Binomial Distribution of Correct Votes", plot_height=400, plot_width=400, x_axis_label='Number of Experts Voting Correctly', y_axis_label='Binomial Probability')
my_plot_b = Figure(title="Power Calculation", plot_height=400, plot_width=400, x_axis_label='Number of Experts', y_axis_label='Probability Majority of Experts Are Correct')

p=.7
n=11
slider_p = Slider(start=.01, end=.99, step=.01, value=p, title="Chance Each Expert is Correct")
slider_n = Slider(start=1, end=99, step=2, value=n, title="Number of Experts")

# The datapoints
sup = range(n+1)
pmf = stats.binom.pmf(sup, n, p)
source_points = ColumnDataSource(data=dict(sup=sup, pmf=pmf))
my_plot.scatter(x='sup', y='pmf', source=source_points, color="#2222aa", line_width=3)

x=2*[n/2.]
y=[0,max(pmf)]
source_points_d = ColumnDataSource(data=dict(x=x,y=y))
my_plot.line(x='x', y='y', source=source_points_d, color="#ff0000", line_width=3)

sup = range(1,100,2)
cut = [i/2 for i in sup]
cdf = 1-stats.binom.cdf(cut, sup, p)
source_points_b = ColumnDataSource(data=dict(sup=sup, cdf=cdf))
my_plot_b.line(x='sup', y='cdf', source=source_points_b, color="#2222aa", line_width=3)

sup = [n]
cdf = [1-stats.binom.cdf(sup[0]/2, n, p)]
source_points_c = ColumnDataSource(data=dict(sup=sup, cdf=cdf))
my_plot_b.scatter(x='sup', y='cdf', source=source_points_c, color="#00ff00", line_width=3)

def update(attrname, old, new):
    n=slider_n.value
    p=slider_p.value

    sup = range(n+1)
    pmf = stats.binom.pmf(sup, n, p)
    source_points.data = dict(sup=sup, pmf=pmf)

    x=2*[n/2.]
    y=[0,max(pmf)]
    source_points_d.data = dict(x=x,y=y)

    sup = range(1,100,2)
    cut = [i/2 for i in sup]
    cdf = 1-stats.binom.cdf(cut, sup, p)
    source_points_b.data = dict(sup=sup, cdf=cdf)

    sup = [n]
    print(sup[0])
    cdf = [1-stats.binom.cdf(sup[0]/2, n, p)]
    source_points_c.data = dict(sup=sup, cdf=cdf)

    
for w in [slider_n, slider_p]:
    w.on_change('value', update)

layout = column(row(my_plot, my_plot_b), slider_p, slider_n)
curdoc().add_root(layout)
