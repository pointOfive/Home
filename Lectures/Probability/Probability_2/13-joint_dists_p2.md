
# Joint Probability Distributions 

A _joint probability distribution_ describes the probability of two or more distinct random variables 
either (a) actualizing a specific co-occurrence of values (for discrete random variables), 
or (b) actualizing a set of outcomes within preset ranges 
(for continuous random variables). A joint probability distribution of \\(n\\) random variables is indicated as

$$ P\left(X_1, X_2, \cdots X_n\right) $$

where \\(P(\cdots)\\) denotes either a probability mass function or a probability 
density function (or even a mix of the two if the random variables themselves are mixed). 
In the previous challenges about the joint distribution of "10 cards" there were two discrete random variables:
\\(X_1\\), the card drawn the first time, and \\(X_2\\), the card drawn the second time). 
So the joint distribution of these two random variables would be indicated as 

$$ P(X_1, X_2) $$

Now, please take special care to note that \\(P(\cdots)\\) IS NOT necessarily specifying \\(Pr(\cdots)\\).
Yes, for discrete random variables this is what it expresses; but for continuous random
variables it represents a probability density function, \\(f_{\cdots}(\cdots)\\),
not a probability mass function.  So the notation 

$$ P\left(X_1, X_2, \cdots X_n\right) $$

is meant to generically represent either

$$ f_{X_1, X_2, \cdots X_n}\left(X_1, X_2, \cdots X_n\right) \quad\text{ or }\quad Pr\left(X_1, X_2, \cdots X_n\right) $$

i.e., it represents either a joint probability density function or a joint probability mass function, 
depending upon the continuous or discrete nature of the random variables involved.
We will return to this notion and clarify it further below. 


## Conditional and Marginal Probability Distributions 

The joint distribution of \\(n\\) (arbitrarily ordered) random variables can ALWAYS
be re-expressed as the multiplicative sequence of _conditional probability distributions_ 
and a _marginal probability distribution_ as follows according to the _chain rule_
for probability distributions:

$$ P\left(X_1, X_2, \cdots X_n\right) = 
\left(\prod_{i=n}^{2} P\left(X_i | X_{i-1}, \cdots X_1 \right)\right) \times P\left(X_1\right) $$

where the mathematical _multiplication notation_, e.g., \\(\displaystyle \prod_{i=1}^{n} c_i\\)
for numbers \\(c_i, i = 1, \cdots, n\\) is just like the mathematical summation notation 
\\(\displaystyle \sum_{i=1}^{n} c_i\\) except that it indicates that the \\(c_i\\)
are multiplied rather than added together. And again, don't forget that the \\(P(\cdots)\\)
notation can specify either probability mass or probability density functions.


_Conditional distributions_ are what's left of a joint distribution after some of the 
random variables of the joint distribution have been determined and taken into account,
and marginal distributions are what you get from a joint distribution
if you just simply ignore the other random variables of the joint distribution.
So, for example, the distributional chain rule for the joint distribution
of two random variables is

$$ P(X_1, X_2) = P(X_2 | X_1) P(X_1) $$

which states that the joint distribution of \\(X_1\\) and \\(X_2\\) 
can be defined as the product of the conditional of \\(X_2\\) given \\(X_1\\) times the 
marginal distribution of \\(X_1\\).

#### !challenge

* type: multiple-choice
* id: joint_question_5
* title: Distributional chain rule

#### !question

Which of the following define the distributional chain rule for

$$ P\left(X_1, X_2, X_3, X_4, X_5\right) $$ 

#### !end-question
### !options
* (a) \\(P\left(X_1 | X_2, X_3, X_4, X_5\right)  P\left(X_2 | X_3, X_4, X_5\right) P\left(X_3 | X_4, X_5\right) P\left(X_4 | X_5\right) P\left(X_5\right) \\)
* (b) \\(P\left(X_5 | X_4, X_3, X_2, X_1\right)  P\left(X_4 | X_3, X_2, X_1\right) P\left(X_3 | X_2, X_1\right) P\left(X_2 | X_1\right) P\left(X_1\right) \\)
* (c) both of the two above are appropriate chain rule factorizations
* (d) \\(P\left(X_5 | X_4\right) P\left(X_4 | X_3\right) P\left(X_3 | X_2\right) P\left(X_2 | X_1\right) P\left(X_1 | X_5\right)\\)
* (e) \\(P\left(X_1\right) P\left(X_2\right) P\left(X_3\right) P\left(X_4\right) P\left(X_5\right)\\)
### !end-options
### !answer
(c) both of the two above are appropriate chain rule factorizations
### !end-answer
#### !explanation

The order of the variables in a chain rule factorization is not material, 
only the relative structuring and form of the conditional distributions.
Admittedly, this was a bit of a trick question because the only
suggestion of this in the text was the relatively innocuous looking 
and perhaps somewhat obscure note "(arbitrarily ordered)" towards the beginning of the 
section. 

If that qualification was missed, then the only other indication
you might have realistically had to discern the correct answer to this
question was the fact that for events the ordering in the probability
chain rule calculation was irrelevant so you might have had an inkling
that this temporal ambiguity characteristic of probability calculations
would find its way into random variables and their joint distributions as well.
If you caught this you were right and deserve some very rare kudos on some very
exceptional problem considerations.

Answers (d) and (e) of course do not conform to the chain rule of conditional 
probability; although there could certainly be some joint distribution contexts
where they are indeed correct factorizations of the joint distribution. I.e.,
when the conditional independence they specify is indeed reflective 
of the actual conditional independence structure of the joint distribution.

#### !end-explanation
#### !end-challenge


#### !challenge

* type: paragraph
* id: joint_question_6
* title: Distributional chain rule verbalization

#### !question

Give a written definition/explanation of the distributional chain rule
applied to \\( P\left(X_1, X_2, X_3, X_4, X_5\right) \\) in the previous problem.

#### !end-question
#### !explanation

The joint distribution is the product of 

- the conditional distribution of the first random variable (conditional on all the others), times
- the conditional distribution of the second random variable (conditional on all the others except the first), times
- the conditional distribution of the third random variable (conditional on all the others except the first and the second), times
- the conditional distribution of the fourth random variable (conditional on the fifth), times
- the marginal distribution of the fifth (and last) random variable

#### !end-explanation
#### !end-challenge

## Another Example of Joint, Conditional and Marginal Probability Distributions 

To bring this all together a little more concretely and  make the notions of the conditional 
and marginal distributions a little more explicit, let's consider a new example of a joint distribution
and the conditional and marginal distributions that comprise it.
Consider a joint probability distribution for the number of statistics books a random person owns
and the number of video game consoles someone owns.
To keep this simple we'll consider only the case where everyone has only 0, 1, or 2 of each.


|  | 0 Stats Books | 1 Stats Book | 2 Stats Books
---:|:---|:---|:---
0 Consoles| 0.02 | 0.20 | 0.15
1 Console| 0.10 | 0.15 | 0.20
2 Consoles| 0.03 | 0.15 | 0.05

Notice that the sum of all cells is equal to \\(1.0\\) because this is a (joint) probability mass function.
Joint probability distributions define both conditional distributions and marginal distributions
(for both discrete and continuous random variables).
Again, marginal distributions are where the distribution of one or more variables is considered
without consideration of some of the other variables defined by the joint distribution. 
And conditional distributions are distributions where some of the variables of the joint distribution
have been realized and knowledge of their values are taken into consideration.

To extract the marginal distribution of stats books from this joint distribution
we need to "ignore" the video game random variable.  I.e., we sum down each of the columns:

$$ Pr(\text{Stats Books} = 0) = 0.02 + 0.10 + 0.03 = 0.15 $$
$$ Pr(\text{Stats Books} = 1) = 0.20 + 0.15 + 0.15 = 0.45 $$
$$ Pr(\text{Stats Books} = 2) = 0.15 + 0.20 + 0.05 = 0.40 $$

Just as with the joint distribution, the marginal probabilities
of discrete random variables should will always add to one.
If they don't then something went wrong.

Alternatively, to extract a specific conditional distribution from the joint distribution,
e.g., the probability distribution for consoles amongst people who own 2 stats books,
we simply have to renormalize the slice of the joint distribution we care about:

$$ P(\text{Consoles} = 0 | \text{Stats Books} = 2) = \frac{0.15}{0.40} = 0.375 $$
$$ P(\text{Consoles} = 1 | \text{Stats Books} = 2) = \frac{0.20}{0.40} = 0.50 $$
$$ P(\text{Consoles} = 2 | \text{Stats Books} = 2) = \frac{0.05}{0.40} = 0.125 $$

This is the probability distribution for Consoles Owned, conditional upon owning two stats books. 
Note that once again, the probabilities add to 1.0.

While deriving the conditional distribution in this manner may (and hopefully does) feel intuitive,
it is actually just the result of a rearrangement of the chain rule.  Namely,

$$ P(X_1, X_2) = P(X_2 | X_1)P(X_1) \quad \Longrightarrow \quad P(X_2 | X_1) = \frac{P(X_1, X_2)}{P(X_1)}$$

so that for our case we have 

$$ P(\text{Consoles} = x | \text{Stats Books} = 2) = 
\frac{P(\text{Consoles} = x, \text{Stats Books} = 2)}{P(\text{Stats Books} = 2)} $$


#### !challenge

* type: number
* id: joint_distribution_7
* title: Marginal distributions expectation
* decimal: 2

#### !question

Given the following joint distribution table, what is the expected value of \\(X\\)?

|  | \\(X = 5\\) | \\(X = 10\\) |
|:----|----:|----:|
\\(Y = 1\\) | .40 | .05 |
\\(Y = 2\\) | .25 | .30 |

#### !end-question

### !placeholder
enter your answer as an exact decimal
### !end-placeholder

### !answer
6.75
### !end-answer

#### !explanation

We must first compute the marginal distribution of \\(X\\).
$$ P(X = 5) = .40 + .25 = .65 $$
$$ P(X = 10) = .05 + .30 = .35 $$
and then based on this marginal distribution calculate 
\\(\operatorname{E}\_X[X]\\):

$$ \operatorname{E}\_X[X] = \sum\_{x = \{5, 10\}} x P(x) $$

$$                       = 5 \times .65 + 10 \times .35 = 6.75 $$

#### !end-explanation

#### !end-challenge



#### !challenge

* type: number
* id: joint_distribution_8
* title: Conditional distributions expectation
* decimal: 2

#### !question

Given the following joint distribution table, what is the expected value of \\(X\\) 
given \\(Y=1\\)?

|  | X = 5 | X = 10 |
|:----|----:|----:|
Y = 1 | .40 | .05 |
Y = 2 | .25 | .30 |

#### !end-question

### !placeholder
round your answer to two decimal places
### !end-placeholder

### !answer
5.56
### !end-answer

#### !explanation

We must first compute the conditional distribution of \\(X\\) given that \\(Y=1\\).
$$ P(X = 5 | Y = 1) = \frac{.40}{.45} $$
$$ P(X = 10 | Y = 1) = \frac{.05}{.45} $$
and then based on this conditional distribution calcualte 
\\(\operatorname{E}\_{X|Y}[X]\\):

$$ \operatorname{E}\_{X|Y}[X] = \sum_{x = \{5, 10\}} x P(x) $$

$$                       = 5 \times \frac{.40}{.45} + 10 \times \frac{.05}{.45} = 5.55555555... $$


#### !end-explanation

#### !end-challenge

