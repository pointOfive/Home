# Independent and Identically Distributed Random Variables

In the very first three challenges in the joint distributions section --
the problems were we have 10 cards and we randomly draw two of them -- we have that 

$$ P(X_1, X_2) = P(X_2|X_1)P(X_2) $$

so the joint distribution is just the product of a conditional distribution
and a marginal distribution which is of course just the simplest form of the chain rule.
However, for the variation on that challenge -- where the first card was replaced after it was drawn --
it turns out that we have  

$$ P(X_1, X_2) = P(X_1)P(X_2) $$

This is because the card draws are independently of each other (since the first
card is replaced after being drawn). 
We additionally had that the card distributions were identical 
(again because the first card was replaced after it was drawn), 
so we would further precisely characterize \\(X_1\\) and \\(X_2\\) as being i.i.d..
We will return to this second i.i.d. notion shortly, but to start with let's begin
by discussing these two distributional factorizations a little more explicitly.

First, in all the 10 card problems above (and the Game Consoles and Statistics Textbook 
problems as well), it's easy to view our calculations as being done
directly with probabilities.  But that's not how we've actually conceptualized
what we've done in those problems.  What we've done is to explicitly extract the probability 
distributions of interest by deriving them from the joint probability distribution. 
Second, we are now here specifying the factorizations of the 
joint distribution of \\(X_1\\) and \\(X_2\\) in the 10 card problems.  
But this was not what we did (nor a necessary step) to our solutions for those 
problems. Rather we are now doing this factorization purely as an alternative exercise 
designed to explore the composition of the joint distribution in terms of the conditional 
and marginal distributions which comprise it (or which the joint distributions entails,
if you prefer). 

So, we are making distributional statements with respect to the above factorizations 
of the joint distribution of \\(X_1\\) and \\(X_2\\)
(where again, \\(X_1\\) and \\(X_2\\) represent the first and second drawn cards, respectively)
And specifically, we are saying there is a joint probability distribution called \\(ten\_cards(X_1, X_2)\\)
which can be factored into conditional and marginal distributions two ways: 
one factorization which is accurate in the context
of problems 1 through 3 and another factorization that is accurate within the context of 
problem 4.  These are, respectively:

$$ ten\\_cards(X_1, X_2) = ten\\_cards(X_2 | X_1) ten\\_cards(X_1) $$
$$ \quad\text{ and }\quad $$
$$ ten\\_cards(X_1, X_2) = ten\\_cards(X_1) ten\\_cards(X\_2) $$

or, more explicitly

$$ ten\\_cards(X_1, X_2) = ten\\_cards\\_draw1given1drawn(X_2 | X_1) ten\\_cards\\_draw1(X_1) $$
$$ \quad\text{ and }\quad $$
$$ ten\\_cards(X_1, X_2) = ten\\_cards\\_draw1(X_1) ten_cards\\_draw1(X\_2) $$

The reason for not being immediately (and only) explicit with the names of our 
probability distributions is that their function is already somewhat implied 
just by the notational specification of the random variables they entail. 
I.e., the conditional and marginal specifications of the notation 

-  "\\(X_2 | X_1\\)" and "\\(X_1\\)"

versus 

- "\\(X_1, X_2\\)"

tells us what we are evaluating with respect to the original joint distribution
\\(ten\\_cards(X_1, X_2)\\).

But nonetheless, this should very clearly clarify that we are factoring distributions
not just multiplying probabilities.  Now, in this context, these distributions are the 
following probability mass functions

- \\(ten\\_cards\\_draw1given1drawn(X_2 | X_1) = \frac{1}{9} \text{ for each card left after drawing } X_1\\) 
- \\(ten\\_cards\\_draw1(X_1) = \frac{1}{10} \text{ for each card in the set }\\)

so that the joint probability function is either

- \\(ten\\_cards(X_1, X_2) = \frac{1}{10} \frac{1}{9} \text{ for two cards } X_1, X_2 \text{ drawn under the first context, or}\\)
- \\(ten\\_cards(X_1, X_2) = \frac{1}{10} \frac{1}{10} \text{ for two cards } X_1, X_2 \text{ drawn under the second context}\\)

which does indeed appear to suggest we are multiplying together probabilities; but no, 
we are multiplying together probability mass functions.  

We can perhaps further emphasize this point by now returning to the notion of i.i.d..

First, in general, if \\(n\\) variables are _independent_ of each other then we have 
a complete simplification of the chain rule where every conditional distribution
just becomes a marginal distribution, i.e.,

$$ P\left(X_1, X_2, \cdots X_n\right) = \prod_{i=1}^n P\left(X_i\right) $$ 

where the meaning of the marginal distribution \\(P\left(X_i\right)\\) is implied
by the meaning of \\(X_i\\) under the joint distribution. 
Further, if the random variables are (in addition to being independent) 
also identically distributed 
according to some distribution \\(distribution\\_name\\) with parameters \\(\theta\\), then we write 

$$ X_i \overset{\small i.i.d.}{\sim} distribution\\_name(\theta) $$

So to give an explicit example of what is meant here, 
suppose each \\(X_i\\) was i.i.d. according to a normal 
distribution with parameters \\(\mu\\) and \\(\sigma^2\\). 
We would then write

$$ X_i \overset{\small i.i.d.}{\sim} Normal\left(\mu, \sigma^2\right) $$

and the joint distribution of all the \\(X_i\\)'s would be 

$$ f(X_1=x_1, X_2=x_2, \cdots, X_n=x_n) = \prod_{i=1}^n 
\frac{1}{\sqrt{2\pi\sigma^2}}exp\left(-\frac{(x_i - \mu)^2}{2\sigma^2}\right) \text{ for } x_i \in (-\infty, \infty)$$


So in this case the joint distribution is the product of (identical) marginal distributions 
(which are probability density functions) of the random variables entailing
the joint distribution. 

#### !challenge

* type: paragraph
* id: joint_question_9
* title: Joint distribution for i.i.d. Poisson random variables

#### !question

Provide the explicit mathematical definition of the joint
distribution of the random variables

$$ X_i \overset{\small i.i.d.}{\sim} Poisson\left(\lambda\right), \text{ for } i=1, \cdots, n $$

#### !end-question
#### !explanation

$$ Pr(X_1=x_1, X_2=x_2, \cdots, X_n=x_n) = \prod_{i=1}^n 
\frac{\lambda^{x_i} e^{-\lambda}}{x_i!},\text{ for each } x_i \in \{0,1,2,...\} $$

#### !end-explanation
#### !end-challenge


# Marginalization

As noted before, marginal distributions are simply the distributions 
of a specific random variable (or set random variables) of a joint
distribution where the remaining random variables of that joint distribution
are simply ignored.  While the notion of ignoring some of the random variables
of a joint distribution is very simple, the actual specification of this 
process, known as _marginalization_, is fairly involved (or at least notationally
involved).  The good news is that you have already seen 
the probabilistic analog to distributional marginalization: namely, the law of total probability.

So, specifying marginal distributions of random variables from a joint distribution 
looks quite similar to the law of total probability. For discrete random 
variables it is

$$ 
\begin{align}
Pr(X_0=x_0) = & \sum_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} Pr(X_0=x_0, X_1=x_1, \cdots X_n=x_n)\\\\ 
= &  \sum_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} 
Pr(X_0=x_0| X_1=x_1, \cdots X_n=x_n) Pr(X_1=x_1, \cdots X_n=x_n) 
\end{align}
$$

And for continuous random variables, it is

$$ 
\begin{align}
f(X_0=x_0) = & \int_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} 
f(X_0=x_0, X_1=x_1, \cdots X_n=x_n) dx_1 \cdots dx_n = 
f(X_0=x_0)\\\\
 =  & \int_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} 
f(X_0=x_0 | X_1=x_1, \cdots X_n=x_n) f(X_1=x_1, \cdots X_n=x_n) dx_1 \cdots dx_n 
\end{align}
$$

Of course, if \\(X_0\\) is independent of \\(X_i\\) for \\(i = 1, \cdots, n\\) then we have

$$ Pr(X_0=x_0) = 
\sum_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} 
Pr(X_0=x_0) Pr(X_1=x_1, \cdots X_n=x_n) $$

and

$$ f(X_0=x_0) = 
f(X_0=x_0) = \int_{(x_1, \cdots, x_n) \in S_{(X_1, \cdots, X_n)}} 
f(X_0=x_0) f(X_1=x_1, \cdots X_n=x_n) dx_1 \cdots dx_n $$

and the equalities are trivial. 


#### !challenge

* type: paragraph
* id: joint_question_10
* title: Marginal distribution for i.i.d. Poisson random variables

#### !question

Suppose 

$$ X_i \overset{\small i.i.d.}{\sim} Poisson\left(\lambda\right), \text{ for } i=1, \cdots, n $$

so that 

$$ Pr(X_1=x_1, X_2=x_2, \cdots, X_n=x_n) = \prod_{i=1}^n
\frac{\lambda^{x_i} e^{-\lambda}}{x_i!},\text{ for } x_i \in \{0,1,2,...\} $$

What is the marginal distribution of \\(X_i\\)?

#### !end-question
#### !explanation

$$ Pr(X_i=x_i) = \frac{\lambda^{x_i} e^{-\lambda}}{x_i!},\text{ for } x_i \in \{0,1,2,...\} $$

#### !end-explanation
#### !end-challenge


# Wrap Up

Next we will next quickly look at a the bivariate distributional characteristics
of covariance and correlation.  But after that we will return to distributional
theory again, particularly focussing closer on conditional distributions.
And the way we will do this is from from within the context of our long awaited discussion contrasting 
Bayesian analysis with classical frequentist statistics!


