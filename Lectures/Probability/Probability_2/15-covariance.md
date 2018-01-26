
# Covariance (and Variance, again)

Covariance is a measure of how much two variables change together. 
For example, the covariance is positive when high values of \\(X\\) co-occur frequently 
with high values of \\(Y\\); and the covariance is negative when high values of \\(X\\) co-occur 
frequently with low values of \\(Y\\); and the covariance is zero when the values of \\(X\\) 
co-occur randomly with values of \\(Y\\).

For example, shoe size and height positively co-vary -- 
an increase in one is likely to be accompanied by an increase in the other. 
A person with a size 10 foot will probably be taller than a person with a size 7 foot. 
However, this isn't a perfect relationship. 
Not every person with a size 10 foot is taller than every person with a size 7 foot, 
and knowing someone's height doesn't give us enough information to know their exact shoe size.

Covariance is a distributional characteristic of a joint distribution and 
for discrete random variables it is defined and calculated as 

$$ \operatorname{Cov}(X, Y)= \sum\_{(x,y) \in S_{X, Y}} 
(x-\operatorname{E}\_X(X))(y-\operatorname{E\}_Y(Y)) Pr(X=x, Y=y)$$

and for continuous random variables it is defined and calculated as 

$$ \operatorname{Cov}(X, Y) = \underset{(x,y) \in S\_{X, Y}}{\int \int} 
(x-\operatorname{E}\_X(X))(y-\operatorname{E}\_Y(Y)) f\_{X,Y}(X=x, Y=y) \; dx dy$$


I.e., for each outcome under the joint distribution we find the marginal distances 
to the marginal means for each of the two random variables \\(X\\) and \\(Y\\).  
We then take the weighted average (weighted by the relative outcome frequencies)
of the product of these distances, which gives us the covariance measure over
the (bivariate) joint distribution of the random variables. 
This  tells us how much, and in what direction, outcomes in \\(Y\\) and \\(X\\)
tend to change at the same time relative to each other as defined by the 
(bivariate) joint distribution.

What would it it mean to take the covariance of \\(X\\) and \\(X\\)? 
I.e., the covariance of \\(X\\) with itself?
We can plug it in to the formula easily enough, e.g.,

$$
\begin{align}
\operatorname{Cov}(X, Y) =& \sum\_{x \in S\_{X, Y}} 
(x-\operatorname{E}\_X(X))(x-\operatorname{E}\_X(X)) Pr(X=x, Y=y)\\\\
=& \sum\_{x \in S\_{X}} (x-\operatorname{E}\_X(X))(x-\operatorname{E}\_X(X)) Pr(X=x)\\\\
=& \sum\_{x \in S\_{X}} (x-\operatorname{E}\_X(X))^2 Pr(X=x)
\end{align}
$$

which asks whether a "large change away from the mean" in \\(X\\) 
is accompanied by a "large change away from the mean" in \\(X\\). 
Well of course it would be. So what we're measuring here is how large of a change away 
from the mean do we tend to get? 
If most of our outcomes \\(x\\) cluster around the mean, we tend to have a small amount of 
change from the mean.  If the outcomes \\(x\\) tend to be more spread out then we tend to have 
a bigger amount of change from the mean.  But of course you will probably by now have noticed 
that the covariance of \\(X\\) with itself is just the variance of \\(X\\), 
\\(\operatorname{Var}[X]\\), which of course measures the amount of variance, or 
volatility, that might be observed in the outcome of the random variable \\(X\\).


## Correlation

Here is a hypothetical covariance matrix for height (in inches), 
weight (in pounds), and shoe size (in US units):

       | height | weight| shoe
       ---|---|---|---
height  |  15.7  | 107.5  | 6.2
weight  | 107.5 | 1250.0 | 45.0
shoe     |  6.2  |  45.0  | 3.2

So, e.g., \\(\operatorname{Var}[\text{height}] = 15.7\\) and 
\\(\operatorname{Cov}(\text{height, weight}) = 107.5\\).

Considering the formulas for variance and covariance, what units are these a measure of? 
Awkwardly, the variance of height would be measured in inches squared; 
and the covariance of height and weight would be measured in units of inch-pounds. 
Neither of these are particularly intuitive units of measure...

Standard deviation is the square root of variance, which brings the units back down the first degree.
That's much easier to interpret. Here, the standard deviation for height would be 3.96 inches, 
meaning, roughly, that it's quite common for a random person to have a height within about 4 inches 
higher or lower than the mean height of the entire group.  So that's useful for interpretation.
We like the standard deviation because it is nicely interpretable like that. 

Unfortunately, just taking the square root of the other covariances will not be so helpful
because the square root of the inch-pounds unit is probably even less meaningful
than the inch-pounds unit without the square root...

Let's change our tactic.  What if we wanted to know whether height or weight was a better 
predictor of shoe size. We can see here that the covariance of height and shoe size is 6.2, 
while the covariance of weight and shoe size is 45. 
Can we conclude the relationship between weight and shoe size is seven times stronger than 
between height and shoe size? Well, no, because the units are not the same, 
so the values can't be compared meaningfully. What we need to do is get 
strength of relationship measures that are on the same scale.  It turns out that this can actually
be done!  What we do is somehow normalize the covariance matrix into a common scale matrix.
This common scale matrix is called the correlation matrix (as opposed to the covariance matrix).
Then using the correlation matrix we can compare the strengths of relationships between
the random variables (since they are now on a common scale). 

The correlation matrix for our random variables is:

       |  height |   weight   |   shoe
      ---|---|---|---        
height  | 1.000000 | 0.767368 |  0.874716
weight | 0.767368 |  1.000000 | 0.711512
shoe  |  0.874716 | 0.711512  | 1.000000

From this we can see that the correlation between height and shoe size (0.874716) 
is somewhat greater than the correlation between weight and shoe size (0.711512). 
It appears that height is a better predictor of shoe size than weight is.

The way we transform the covariance into the common scale correlation is by 
dividing the covariance by the standard deviations of the two random variables.
That is we take a measure in units "unit A - unit B" and divide it my measures 
in "unit A" and "unit B", which cancels all the units!  So the correlation
measure is unitless!

Here is (super easy) the formal definition of the correlation between random variables \\(X\\) and \\(Y\\),
(which of course applies to both discrete and continuous pairs of random variables):

$$ \operatorname{Cor}(X, Y) = \frac{\operatorname{Cov}(X, Y)}{\sqrt{\operatorname{Var}[X]\operatorname{Var}[Y]}} $$


### !challenge

* type: multiple-choice
* id: cov_1
* title: comparison of correlation and covariance

### !question

When is the correlation the same as the covariance for two random variables?

### !end-question
### !options

* It is never the same -- covariance and correlation are different things
* When both of the random variables are "standardized", i.e., they have standard deviation 1

### !end-options
### !answer
When both of the random variables are "standardized", i.e., they have standard deviation 1
### !end-answer

### !explanation

Correlation is just the measure of linear association when the scales of the data 
are ignored.  I.e., scaled to 1.  So, yes, correlation is the covariance of two 
random variables who both have a standard deviation of 1.
In this way correlation gives us a measure of linear association in an "absolute" sense. 

### !end-explanation
### !end-challenge


A few further notes about covariance and correlation are in order:

- covariance can range from \\(-\infty\\) to \\(\infty\\), while correlation is bounded between \\(-1\\) and \\(1\\)
- covariance will change if the scale of its random variables changes -- not so for correlation since the scale is divided out
- both covariance and correlation measure the strength of a linear relationship between two random variables, but correlation is readily interpretable since it is on an absolute scale while the covariance is not 
since its value is dependent upon the scales of the random variables. 
I.e., covariance does not provide an absolute interpretation of the the strength of linear association -- 
it is arbitrarily dependent upon data scales.  


Changes in unit scale will change measures of covariance. The number of minutes you study 
compared to your test score will have a different covariance than the number of hours you 
study compared to your test score. Thus, correlation allows us to compare the strength 
of relationships in a way that covariance does not. What if you wanted to find out which 
had a stronger relationship to your test score: number of hours studied or number of YouTube 
videos watched? In order for the comparison to be meaningful, you would first put your 
strength of relationship measure on an absolute scale. Because of this, 
correlation is generally a more useful descriptor than covariance.

## Covariance (or correlation) as a parameter of the multivariate normal distribution

Recall that if we have two random variables that are 
i.i.d. according to a normal distribution with parameters \\(\mu\\) and \\(\sigma^2\\)
then we write that

$$ X_i \overset{\small i.i.d.}{\sim} Normal\left(\mu, \sigma^2\right), \text{ for i = 1, 2} $$

and the joint distribution of \\(X_1\\) and \\(X_2\\) is 

$$ f(X_1=x_1, X_2=x_2) = \prod_{i=1}^2
\frac{1}{\sqrt{2\pi\sigma^2}}exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right) $$

for \\(x_i \in (-\infty, \infty), \text{ and for} i = 1, 2\\)

But what if \\(X_1\\) and \\(X_2\\) have some linear association? 
I.e., what if \\(X_1\\) and \\(X_2\\) have a non-zero covariance?
In this case \\(X_1\\) and \\(X_2\\) are not independent!
So \\( f(X_1=x_1, X_2=x_2) \\) is not equal to the above (i.i.d. based) 
specification. 

Well, it turns out that if \\(X_1\\) and \\(X_2\\) are both marginally normally
distributed, but are associated according to some non-zero covariance, then the 
joint distribution \\( f(X_1=x_1, X_2=x_2) \\) is what is known as a
_multivariate normal distribution_, i.e.,

$$ f(X_1=x_1, X_2=x_2) = 
(2\pi)^{-\frac{n}{2}} |\Sigma|^{-\frac{1}{2}} 
e^{-\frac{1}{2} ({\boldsymbol X} - {\boldsymbol \mu})^T \Sigma^{-1}({\boldsymbol X} - {\boldsymbol \mu})} 
$$

where here 
- \\(n=2\\) 
- \\( {\boldsymbol X} = (X_1, X_2)^T \\)
- \\( {\boldsymbol \mu} = (\mu_1, \mu_2)^T \\)
- and \\( \Sigma = \left[\begin{array}{cc}\sigma^2_1 & \sigma_{12}\\\\ \sigma_{12} & \sigma^2_2\end{array} \right] \\) 
  - is the _covariance matrix_ parameter of the multivariate normal distribution
  - \\( \sigma_{12} = \operatorname{Cov}(X_1,X_2)\\)
  - \\(|\Sigma|\\) is the determinant of the covariance matrix, and 
  - \\(\Sigma^{-1}\\) is the inverse of the covariance matrix

And notice that we need not have the mean parameters \\( \mu_1 = \mu_2 \\) nor 
the variance parameters \\( \sigma^2_1 = \sigma^2_2 \\).

The multivariate normal distribution looks as follows:

![Bivariate (multivariate) normal distribution](images/MultivariateNormal.png)

where the middle green ellipse reflects the "mound" nature of the distribution, 
and the distribution is specified by the five parameters indicated above:
- two mean (location) parameters \\( {\boldsymbol \mu} = (\mu_1, \mu_2)^T \\)
- two variance (spread) parameters \\(\sigma^2_1\\) and \\(\sigma_2\\)
- and one covariance parameter \\(\sigma_{12}\\)

the latter three of which comprise the covariance matrix \\(\Sigma\\).

The interesting parameter for the bivariate normal distribution of course is the 
covariance parameter \\(\sigma_{12}\\) because this determines the strength
of linear associate that exists between \\(X_1\\) and \\(X_2\\) in the joint
distribution \\( f(X_1=x_1, X_2=x_2) \\) 

### !challenge

* type: paragraph
* id: cov_2
* title: comparison of correlation and covariance

### !question

Label the following on the above plot:

(1) Joint Distribution

(2) Marginal Distribution 

(3) Covariance/Correlation

(4) Variances

(5) Means

(6) Conditional Distribution

### !end-question

### !explanation

(1) green curve is a mound/orientation representation

(2) red/blue curve are marginal distributions

(3) tightness of green distribution is the Covariance/Correlation

(4) spread of red/blue distribution (and hence green distribution representation) are the variances

(5) locations of red/blue distribution (and hence green distribution representation) are the means

(6) slice of the green distribution parallel to the X (if conditioning on Y) or Y (if conditioning on X) axis 

### !end-explanation
### !end-challenge


### !challenge
* type: code-snippet
* language: python2.7
* id: params_117
* title: Gamma distribution
### !question

Write a function which returns the value of the probability density function
of a bivariate normal distribution with 
- \\( {\boldsymbol \mu} = (1, 2)^T \\)
- \\( \Sigma = \left[\begin{array}{cc} 1 & 1\\ 1 & 2\end{array} \right] \\)

at the point \\((2,1)\\). 

Hint: [check out the SciPy documentation](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.multivariate_normal.html) to see how their implementation of the multivariate normal distribution works.


```python
>>> from scipy import stats
>>> my_function()
```

### !end-question

### !placeholder

```python
import numpy as np
from scipy import stats

def my_function():
    return stats.multivariate_normal...
```

### !end-placeholder
### !tests
```python

import main
import unittest
from scipy import stats
import numpy as np

class TestPython1(unittest.TestCase):
      def test_my_function(self):
        result = round(main.my_function(), 3)
        correct = 0.0131
        self.assertEqual(result[0], correct[0])
```
### !end-tests

### !explanation
### !end-explanation
### !end-challenge

