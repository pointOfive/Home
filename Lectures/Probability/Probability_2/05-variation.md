# Variation and Standard Deviation

The expected value of a random variable \\(\operatorname{E}_X[X]\\) is a very important characteristic of the random variable
\\(X\\) as it provides a measure of the centrality of the outcomes \\(x\\) of the random variable.  That is, \\(\operatorname{E}_X[X]\\) 
describes a sort of "long term average" behavior of the random variable. 


### !challenge

* type: paragraph
* id: dist_pars_1
* title: Expectation

##### !question

Define the expectation of a discrete and a continuous random variable. 

Hint: you won't be able to type the notation \\( \displaystyle  \underset{x_j \in S_X}{\sum}\\) or \\( \displaystyle  \int_{-\infty}^\infty\\) into
the answer box, but you should be able to use some sort of text-based notation to indicate summation and its 
continuous analog, integration. 

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation

The expectation of a discrete random variable \\(X\\) is the weighted average of all possible outcomes 
\\(x_i\\) of that random variable:

$$ \operatorname{E}_X[X] = \underset{x_j \in S_X}{\sum}  x_j Pr(X=x_j) $$

The expectation of a continuous random variable \\(X\\) is the integral

$$ \operatorname{E}_X[X] = \overset{\infty}{\underset{-\infty}{\int}} x f(X=x) \mathrm{d}x $$

##### !end-explanation
### !end-challenge


### !challenge
* type: multiple-choice
* id: dist_pars_2
* title: expectation versus random variables
### !question
Is an expectation \\(\operatorname{E}_X[X]\\) a random variable?
### !end-question
### !options
* Yes, because it's based on a random variable
* No, it's just a numerical calculation based on outcomes and their associated probabilities defined by a probability distribution and is just a constant value and has no randomness associated with it
### !end-options
### !answer
No, it's just a numerical calculation based on outcomes and their associated probabilities defined by a probability distribution and is just a constant value and has no randomness associated with it
### !end-answer
### !explanation
Expectation is "of a random variable" -- not "based on a random variable". 
For the discrete random variable case, 
expectation is calculated as the weighted average of all possible outcomes (weighted by the probabilities of each outcome).
For the continuous random variable case, expectation is defined as the integral over the 
outcome times the probability density function evaluated at the outcome 
(since there is no probability mass function assigning actual probabilities to individual outcomes for continuous random variables).
### !end-explanation
### !end-challenge


Now actually, the _expected value operator_ of a random variable 
\\(\operatorname{E}\_X[\cdot]\\) _  is just a notation for a function with respect to the
 distribution of the random variable \\(X\\) 
that depends on the argument inside the brackets.
This is the reason for the subscript \\(X\\) on  \\(\operatorname{E}\_X[\cdot]\\)  
referred to in the previous section. 
So for example, instead of \\(\operatorname{E}\_X[X]\\), we could have the expectation 
with respect to any function \\(g(X)\\), e.g., 
\\(\operatorname{E}\_X\left[(X-\operatorname{E}\_X[X])^2\right]\\)  where \\(g(X) = (X-\operatorname{E}\_X[X])^2\\). 
And actually, this specific expectation calculation (perhaps surprisingly at first glance because initially it looks pretty weird)
is another very, very important characteristic of a random variables distribution (just as \\(\operatorname{E}\_X[X]\\) is).
Specifically, this expectation calculation provides a measure of volatility, or the extent 
of variety that we might see in outcomes \\(x\\) observed from a random variable \\(X\\).
Distributions are after all meant to characterize and represent uncertainty and randomness, 
so beyond the general location of outcomes generated from a distribution, it's quite obvious that 
a measure of volatility in randomness is a very important distributional characteristic. 
This expectation calculation is so useful in providing this characterization 
that it has received the special name _variance_ and has its own special notation: 

$$ \operatorname{Var}[X] = \operatorname{E}_X\left[(X-\operatorname{E}[X])^2\right] $$

### !challenge

* type: paragraph
* id: dist_pars_3
* title: Standard deviation

##### !question

A common alternative to the variance for representing the level of 
volatility associated with a random variable is called the _standard deviation_
and is defined to be \\(SD[X] = \sqrt{\operatorname{Var}[X]}\\).  
For a discrete random variable with an associated probability mass function defining \\(Pr(X=x)\\),
how would you actually physically calculate the standard deviation (i.e., without using any 
\\(\operatorname{E}_X[X]\\) notation)?

Note: once the standard deviation calculation has been specified for a discrete random variable it's just a matter of 
switching out summation notation for the integration notation to convert the calculation for a continuous random variable. 

Note: the reason the standard deviation is sometimes preferred over the variance is that 
it is measured on the original scale of the data, as opposed to variance which is given on the squared scale of the data.

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation

The standard deviation of a discrete random variable \\(X\\) is calculated as 

$$ SD[X] =  \sqrt{\operatorname{Var}[X]} = \sqrt{\sum_{x_k \in S_X} \left( x_k - \sum_{x_k \in S_X} x_k Pr(X=x_k) \right)^2 Pr(X=x_k)} $$

The standard deviation of a continuous random variable \\(X\\) is calculated as 

$$ SD[X] = \sqrt{\operatorname{Var}[X]} = \sqrt{\int_{-\infty}^\infty \left(x - \int_{-\infty}^\infty x f(X=x) \mathrm{d}x \right)^2 f(X=x) \mathrm{d}x} $$



##### !end-explanation
### !end-challenge


### !challenge

* type: paragraph
* id: dist_pars_4
* title: Alternative definition for variation

##### !question

Show that \\(\operatorname{Var}[X] = \operatorname{E}[X^2] - \operatorname{E}[X]^2 \\).
I.e., the variance is a function of the first two _moments of a distribution_ (as defined below).

Hint: for a discrete random variable the proof just amounts to the simple mathematics of summation... 
show this for a discrete random variable and you can easily transition over to the 
continuous random variable analog by simply replacing the summation computation with
the integration computation.

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation

$$
\begin{align}
\operatorname{Var}[X] &= \operatorname{E}[(X - \operatorname{E}[X])^2] \\\\
&= E[X^2 -2X\operatorname{E}[X] + \operatorname{E}[X]^2] \\\\
&= \sum_{x_i \in S_X} (X^2 -2X\operatorname{E}[X] + \operatorname{E}[X]^2)Pr(X=x_i) \\\\
&= \sum_{x_i \in S_X} (X^2Pr(X=x_i)  -2X\operatorname{E}[X]Pr(X=x_i)  + \operatorname{E}[X]^2 Pr(X=x_i) \\\\
&= \sum_{x_i \in S_X} X^2Pr(X=x_i)  -2 \sum_{x_i \in S_X} X\operatorname{E}[X]Pr(X=x_i)  + \sum_{x_i \in S_X} \operatorname{E}[X]^2 Pr(X=x_i) \\\\
&= \sum_{x_i \in S_X} X^2Pr(X=x_i)  -2 \operatorname{E}[X] \sum_{x_i \in S_X} X Pr(X=x_i)  + \operatorname{E}[X]^2 \sum_{x_i \in S_X} Pr(X=x_i) \\\\
&= E[X^2] -2 \operatorname{E}[X] \operatorname{E}[X] + \sum_{x_i \in S_X} \operatorname{E}[X]^2 Pr(X=x_i) \\\\
&= E[X^2] - \operatorname{E}[X]^2
\end{align}
$$

##### !end-explanation
### !end-challenge



## Wrap Up

The expected value of a random variable \\(\operatorname{E}\_X[X]\\) is called the _first moment_ of a distribution.
The \\(k^{th}\\) distributional moment is defined to be \\(\operatorname{E}\_X[X^k]\\).
Variation is called the _second central moment_ of a distribution.
The \\(k^{th}\\) distributional central moment is defined to be \\(\operatorname{E}\_X[(X - \operatorname{E}\_X[X^k])^k]\\).
Expectation and variance characterize the location and spread of a distribution. 
The higher order moments of a distribution characterize finer property details of that distribution. 
For example, the _skewness_ characterizes the asymmetry of a distribution and the 
_kurtosis_ characterizes the "heavy-tailedness" of a distribution 
(which captures a notion of how often extreme outliers occur under the distribution). 

The _moment generating function_ (MGF) is defined as \\(\operatorname{E}\_X\left[e^{tX}\right]\\) and the \\(k^{th}\\)
derivative of this function will be equal to \\(\operatorname{E}\_X\left[X^k\right]\\).
The moments of a distribution characterize that distribution, and the set of all moments 
of a distribution thus serve to define a distribution in the same way that a CDF 
(or PMF or a PDF) serve to define distribution.  

Another alternative form that is very useful for defining distributions 
for the purposes of advanced theoretical work is the _characteristic function_ of a distribution. 
of a distribution which is defined to be \\(\operatorname{E}\_X\left[e^{itX}\right]\\), 
where \\(i\\) is the _imaginary number_ \\(\sqrt{-1}\\). Unlike the MGF, the characteristic function
always exists, which makes the characteristic function a more useful tool theoretical tool than the MGF
for a number of purposes (although of course the MGF by definition provides a 
mechanism to calculate the moments of distribution).  If you're intrigued by
the MGF and characteristic function you should go and do a little bit of reading about 
these topics!





