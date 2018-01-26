
# conda install graphviz
# pip install graphviz

from graphviz import Digraph

g = Digraph()

#g.node('here', label='YOU ARE\nHERE.', shape='box', style='dashed')


g.node('start', shape="box", style="rounded")
g.node('noob', label="Pretty new to statistics\nor don't remember much?", shape='diamond')
g.node('practice', label="Just need a refresher to pass \nstats interview questions?", shape='diamond')
g.node('regressionML', label="Need a refresher to pass \nregression/ML interview questions?", shape='diamond')
g.node('apply', label="!!! Schedule Stats Interview !!!", shape='diamond')



g.node('stat101', label='https://www.udacity.com/course/intro-to-statistics--st101\nhttps://www.khanacademy.org/math/statistics-probability/probability-library\nhttps://www.khanacademy.org/math/statistics-probability/random-variables-stats-library', shape='parallelogram')
g.node('stat201', label='http://www.intmath.com/counting-probability/counting-probability-intro.php', shape='parallelogram')
g.node('ML', label='https://www.r-bloggers.com/in-depth-introduction-to-machine-learning-in-15-hours-of-expert-videos/\nChapters 1-4 http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf', shape='parallelogram')




g.edge('start', 'noob')
g.edge('noob', 'practice', label='no')
g.edge('practice', 'regressionML', label='no')
g.edge('regressionML', 'apply', label='no')

g.edge('noob', 'stat101', label='yes')
g.edge('practice', 'stat201', label='yes')
g.edge('regressionML', 'ML', label='yes')


g
