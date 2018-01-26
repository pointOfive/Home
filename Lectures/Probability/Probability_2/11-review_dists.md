
## 3. Probability distributions for discrete and continuous random variables

Let's now turn to discrete and continuous probability distributions:

- uniform, Bernoulli, binomial, geometric, Poisson...

- uniform, normal (Gaussian), exponential...

First, we'll do a quick run through to make sure you remember the distributions we've learned so far,
and then we'll create our own novel probability distribution.


### !challenge
* type: multiple-choice
* id: scott_pc2_rev21
* title: Review Problem #21
### !question
What distributional class is a subset of the class of binomial distributions?
### !end-question
### !options
* (a) the class of normal distributions
* (b) the class of Bernoulli distributions
* (c) the class of Poisson distributions
* (d) the class of exponential distributions
* (e) the class of geometric distributions
### !end-options
### !answer
(b) the class of Bernoulli distributions
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev22
* title: Review Problem #22
### !question
What distributional class is typically considered when modeling 
the number of events occurring within a specified time interval?
### !end-question
### !options
* (a) the class of normal distributions
* (b) the class of Bernoulli distributions
* (c) the class of Poisson distributions
* (d) the class of exponential distributions
* (e) the class of geometric distributions
### !end-options
### !answer
(c) the class of Poisson distributions
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev23
* title: Review Problem #23
### !question
What might be called the class of "if at first you don't succeed, try, try, try again" 
distributions?
### !end-question
### !options
* (a) the class of normal distributions
* (b) the class of Bernoulli distributions
* (c) the class of Poisson distributions
* (d) the class of exponential distributions
* (e) the class of geometric distributions
### !end-options
### !answer
(e) the class of geometric distributions
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev24
* title: Review Problem #24
### !question
Which of the following classes of distributions would you say provides the largest, 
and most flexible collection of distributions? 
### !end-question
### !options
* (a) the class of normal distributions
* (b) the class of Bernoulli distributions
* (c) the class of Poisson distributions
* (d) the class of exponential distributions
* (e) the class of geometric distributions
### !end-options
### !answer
(a) the class of normal distributions
### !end-answer
### !explanation
### !end-explanation
### !end-challenge


### !challenge
* type: multiple-choice
* id: scott_pc2_rev25
* title: Review Problem #25
### !question
What class of distributions would be a good choice to use for modeling "time to event" phenomenon?
### !end-question
### !options
* (a) the class of normal distributions
* (b) the class of Bernoulli distributions
* (c) the class of Poisson distributions
* (d) the class of exponential distributions
* (e) the class of geometric distributions
### !end-options
### !answer
(d) the class of exponential distributions
### !end-answer
### !explanation
### !end-explanation
### !end-challenge





#### !challenge
* type: paragraph
* id: scott_pc2_rev_26
* title: Review problem #26
#### !question
What is the difference between continuous and discrete distributions?

#### !end-question
#### !explanation

Continuous distributions produce random values that are real valued; whereas discrete distributions 
produce random values that are integer valued (or can be mapped to the integers). 

Additionally, the mathematical formulas of discrete distributions provide actual probabilities associated
with the chances of observing specific outcomes; where as the mathematical formulas for continuous 
distributions provide relative measures of outcome frequencies.  Thus, for 
continuous distributions, if you want to know the probabilities that an outcome lies in some set
you can only evaluate this based on an "area under the curve" mechanism of 
continuous distribution probability calculations. 

#### !end-explanation
#### !end-challenge


#### !challenge
* type: paragraph
* id: scott_pc2_rev_27
* title: Review problem #27
#### !question

Visit this [coin flip simulation applet](http://www.math.uah.edu/stat/apps/BinomialCoinExperiment.html)

Keep the default settings, but set 'stop' to 'never'.

Click the play button a few times to get a feel for what's happening. Then click the fast forward button and let it run for ~30 seconds. Answer the following questions in the box below:

- about how long does it take the data to approximate the distribution?
- after a couple thousand trials, how different is the observed mean from the distribution (expected) mean? Does this surprise you? Why (not)?
- what is the significance of the 0.246 on the y-axis?

#### !end-question
#### !explanation
Find a friend to explain your answers too! 
A big part of being a data scientist is communication -- 
you are required to convey complex ideas to folks that may have never 
seen the kinds of ideas you're discussing.  
As with many exercises in this section, this exercise will give you an excellent 
simulation of what it's like to be a data scientist!

#### !end-explanation
#### !end-challenge




#### !challenge
* type: paragraph
* id: scott_pc2_rev_28
* title: Review problem #28
#### !question
In your own words, describe the following classes of distributions.
I.e., how do they work and what are some examples of what they can they be used for?

* discrete uniform distributions
* Bernoulli distributions
* geometric distributions
* binomial distributions
* Poisson distributions
* continuous uniform distributions
* exponential distributions
* normal distributions

Once you've made your notes provide them here, but of course also keep them for your own records.
It is crucial to develop your own "internal documentation and organization"
that allows you to systematically categorize and grow your knowledge so that you
can continually build from what you know as opposed to reinventing the wheel
each time you re-encounter a problem. 
And make sure that your organization is particularly well designed and laid out
with an eye to the future 
(via dates and appropriate titling and folder hierarchy structuring) -- the hardest
task a data scientist ever has is trying to look back over previous work that's
poorly organized and poorly documented.

#### !end-question
#### !explanation
Time to begin practicing being a real data scientist!  
Go find these distributions on wikipedia and _score yourself_ relative to
the explanations provided on wikipedia.  

Your ability to successfully execute these sorts of tasks -- effective learning and 
accurate self-assessment are absolutely crucial to the daily operations of a 
data scientist.  This type of activity is the bread and butter of being a data scientist,
so this is in no way some sort of "optional" activity.  This is a real-world experience
and simulation of what being a data scientist feels like!  So have fun and enjoy it!

#### !end-explanation
#### !end-challenge


#### !challenge
* type: paragraph
* id: scott_pc2_rev_29
* title: Review problem #29
#### !question
Go to the [scipy stats tutorial](https://docs.scipy.org/doc/scipy/reference/tutorial/stats.html) and 
work through the documentation there. 
We have already seen most of the concepts presented in this tutorial, but there are some new ones, e.g.,
sampling from distributions.  We will of course eventually address these topics, 
but see if you can make any progress tacking 
new material like this through the use of documentation manuals and tutorial offerings.  

Once you've gone through the library tutorial documentation, summarize what you've 
learned in a way that will help you easily remind yourself how to use these tools
with just a quick glance.  Go ahead an provide that here, but of course also keep 
that for your own records. As with the previous "wikipedia" exercise, 
it is crucial to develop your own "internal documentation and organization"
that allows you to systematically categorize and grow your knowledge so that you
can continually build from what you know as opposed to reinventing the wheel
each time you re-encounter a problem. 

#### !end-question
#### !explanation

As with the "wikipedia" portion of the exercise above, this is real-world practice and experience 
doing what a data scientist does. This exercise thus gives you a definitively authentic
simulation of a very major component of the life of a data scientist. So have fun and enjoy it!
Your ability to successfully execute these sorts of tasks -- effective self-learning 
on the basis of (sometimes poor) documentation is in no way a novelty -- it is the norm.
You will execute the "learn from documentation" task an untold number of times as 
you progress through your data science career. Indeed, you will never stop doing this
as a data scientist. So again, this is in no way some sort of "optional" activity.

Again, make sure that your organization is particularly well designed and laid out
with an eye towards the future 
(via dates and appropriate titling and folder hierarchy structuring) because again: the hardest
task a data scientist ever has is trying to look back over previous work that's
poorly organized and poorly documented.

#### !end-explanation
#### !end-challenge

### Create your own distribution! 

A salesperson has scheduled two appointments to sell encyclopedias. His first appointment will lead to a sale with probability 0.3, and his second will independently lead to a sale with probability 0.6. Any sale made is equally likely to be either for the deluxe model, which costs $1000, or the standard model, which costs $500.

### !challenge

* type: multiple-choice
* id: more_1
* title: Salesperson Question 1

##### !question

What are all the possible total sales outcomes at the end of the two appointments?

##### !end-question

##### !options


* $0, $500, $1000
* $500, $1000
* $0, $500, $1000, $1500, $2000


##### !end-options

##### !answer

$0, $500, $1000, $1500, $2000

##### !end-answer

##### !explanation

##### !end-explanation

### !end-challenge

### !challenge

* type: paragraph
* id: more_2
* title: Ways to earn $1000


##### !question

What are the three different ways he make $1000 in sales?

##### !end-question

##### !placeholder

Enter your response here

##### !end-placeholder


##### !explanation

##### !end-explanation

### !end-challenge

### !challenge

* type: number
* id: more_3
* title: Probability of selling $1500
* decimal: 3

##### !question

What is the probability that he will make MORE THAN $1000 in sales?

##### !end-question

##### !placeholder

Enter your answer as a decimal rounded to three decimal places

##### !end-placeholder

##### !answer
0.135
##### !end-answer

##### !explanation

For the first appointment we have 

Pr(no sale) = 0.7 and Pr(sale) = 0.3 (.5 of which is 1000 and .5 of which is 500), so:

Pr(sales1=0) = 0.7
Pr(sales1=500) = 0.15
Pr(sale1=1000) = 0.15

For the first appointment we have 

Pr(no sale) = 0.4 and Pr(sale) = 0.6 (.5 of which is 1000 and .5 of which is 500), so:

Pr(sales2=0) = 0.4
Pr(sales2=500) = 0.3
Pr(sales2=1000) = 0.3

Then, because of the independence of the sales, we have that:

Pr(sales1=1000 and sales2=1000) = Pr(sales1=1000) Pr(sales2=1000) = .15*.3
Pr(sales1=500 and sales2=1000) = Pr(sales1=500) Pr(sales2=1000) = .15*.3
Pr(sales1=1000 and sales2=500) = Pr(sales1=1000) Pr(sales2=500) = .15*.3

and we add these up to get our answer!

##### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python2.7
* id: more_4
* title: Function to return a PMF

### !question

Write a function that will return the probabilities for the salesperson's total sales given 
different input probabilities.  This is a discrete distribution for a salesperson's total sales!

### !end-question

### !placeholder

```python
def sales_probabilities(appt1, appt2, deluxe_sale, std_cost, deluxe_cost):
  '''INPUT:
    appt1: probability of making a sale at appointment one
    appt2: probability of making a sale at appointment two
    deluxe_sale: given a sale, probability of selling a deluxe model
    std_cost: cost of a standard model
    deluxe_cost: cost of a deluxe model

    OUTPUT:
    sales_probabilities: dictionary showing probabilities of all possible sales totals
    '''
```

### !end-placeholder

### !tests


```python
import main
import unittest

class TestPython1(unittest.TestCase):

    def test_sales_pmf(self):
      result = main.sales_pmf(0.3, 0.6, 0.5, 500, 1000)
      result = {k:round(v,3) for k, v in result.iteritems()}
      correct = {0: 0.28, 500: 0.27, 1000: 0.315, 1500: 0.09, 2000: 0.045}
      self.assertEqual(result, correct)
```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### Last question!


### !challenge

* type: number
* id: binomial_expectation
* title: Expected rainy days
* decimal: 2

##### !question

Recall the problem where the forecast for the next five days is that the chance of rain for each day is 25% 
and where we suppose that the weather on each day does not depend on the weather on the other days.

For how many days on average will it rain in the next five days?

##### !end-question

##### !placeholder

Enter your answer as a decimal rounded to two decimal places

##### !end-placeholder

##### !answer
1.25
##### !end-answer

##### !explanation

$$
\begin{align}
\text{E}\_X[X] &= 0\times Pr(x=0) + 1\times Pr(x=1) + 2\times Pr(x=2) + 3\times Pr(x=3) + 4\times Pr(x=4) + 5\times Pr(x=5) \\\\
&= 0\times {{5}\choose{0}} (.25)^0(.75)^5 + 1\times {{5}\choose{1}} (.25)^1(.75)^4 + 2\times {{5}\choose{2}} (.25)^2(.75)^3 + 3\times {{5}\choose{3}} (.25)^3(.75)^2 + 4\times {{5}\choose{4}} (.25)^4(.75)^1 + 5\times {{5}\choose{5}} (.25)^5(.75)^0
\end{align}
$$

##### !end-explanation
### !end-challenge


