import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib
import pylab
#[u'seaborn-darkgrid', u'fivethirtyeight', u'seaborn-colorblind', u'seaborn-deep', u'seaborn-whitegrid', u'seaborn-bright', u'seaborn-poster', u'seaborn-muted', u'seaborn-paper', u'seaborn-white', u'seaborn-pastel', u'seaborn-dark', u'seaborn-dark-palette']
matplotlib.style.use('seaborn-whitegrid')
%matplotlib inline
pylab.rcParams['figure.figsize']=(5,3.4)

games_played = np.arange(1,1000,10)
fig = plt.figure(1)
p = .506; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Baccarat")
p = .507; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Craps")
p = .51; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Blackjack")
p = .515; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Video Poker")
p = .5265; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Roulette")
p = .55; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Slots")
p = .635; plt.plot(games_played, stats.norm.cdf(.5,p,np.sqrt(p * (1-p)/games_played)),label="Keno")
plt.xlabel("Number of games played")
plt.ylabel("Probability of Expected Wins > $0")
plt.legend(frameon = 1)
