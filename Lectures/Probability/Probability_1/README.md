
Now, don't forget all the tools you have at your disposal to help you calculate probabilities:

- Cardinality
  - factorials
  - permutations
  - combinations
  - multiplication rule

- Probability
  - the chain rule
  - conditional probability
  - Bayes' rule
  - indepdendence
  - mutual exclusivity

parameter


even if they are defined over an (uncountably) infinite number of real
values.	I.e., outcomes over such continuous distributions could	  be any one of an (uncountably) infinite number of real valued
possibilities.	       The reason they	    are specifically chosen  so that the total area under their curve is 1 is exactly so that we can
use areas	       under their curves as probabilities.  We certaintly won't be able to use their heights as probabilities since  there are an
(uncountably) infinite number of real valued outcomes that could be actualized under such functions, and we cannot make
an (uncountably) infinite number of non-zero numbers sum to 1... which leads to	     the very bizare contradiction that the probability
of any single outcome must be 0... but then of course we have to get something when the	 experiment actualizes a   value...



## More practice

For a little more exposition regarding conditional probability, here is very nice [abridged review](resources/conditional_probability_lecture.pdf)
of the most relevant topics



# Apply major probability rules, including the chain rule, the law of total probability

For any sample space *S*, a probability function **P** has the following properties:

property | meaning
---|---
$$ P(A) \ge 0 \; \forall A \in S $$ | The probability of A is greater than or equal to 0 for all A in S
$$ P(S) = 1 $$ | The sum of the probabilities of all possible outcomes in S equals 1
$$ P(\neg {A}) = 1 - P(A) $$ | The probability of Not A equals 1 minus the probability of A




## Glossary

### Section 1
- **experiment:**  The formal term for a process that procduces a random _outcome_ <br>
- **outcome:**  The formal term of an actualized random result of an _experiment_ <br>
- **sample space:**  The collection of all possible _outcomes_ that could be observed from an _experiment_ <br>
- **event:**  A collection of possible _outcomes_ from the sample space of an experiment; an event occurs if an _outcome_ from an _experiment_ is included in the set of _outcomes_ defining the event <br>
- **probability:**  A measure of how likely it is that an event will occur always expressed as a real number between 0 and 1, inclusive. <br>
- **percentage:**  A reformatted expression of a probability given as a real number between 0 and 100, inclusive, and followed by a "%" sign. <br>
- **Venn diagram:**  A nice tool for visually represent sets and set operations heavily relied upon in this section <br>
- **De Morgan's laws:**  The tautologies ------ and ------, which can also be usefully applied for event probability calculations<br>

mutually exclusive
partition


### Section 2

law of total probability 
dependence/independence 

## Notation

### Section 1
- \\(Pr(E)\\):  The _probability_ of event \\(E\\) occuring for a given experiment <br>
- \\(E^C\\):  The _complement_ of event \\(E\\), i.e., all outcomes not in \\(E\\) <br>
- \\(cup\\):  The _union operator_, i.e., \\(E_1 \cup E_2\\) gives the set of all outcomes in either \\(E_1\\) or \\(E_2\\) <br>
- \\(cap\\):  The _intersection_ operator, i.e., \\(E_2 \cap E_2\\) gives the set of all outcomes in both \\(E_1\\) and \\(E_2\\) <br>

emptyset
mutually exclusive
partition


### Section 2

conditional probability, given notation











# Reason through questions of probability, making proper use of associated terms and concepts


## Unit learning goal

[Reason through questions of probability, making proper use of associated terms and concepts](https://github.com/zipfian/probability)

## Unit Overview

Probability is a foundational concept in data science and machine learning. You will need a solid understanding of probability to understand hypothesis testing, Bayesian statistics, logistic regression, and much more.

<!--
### Learning objectives

By the end of this chapter, you will be able to:
  - Explain the difference between permutations and combinations
  - Understand and explain major probability rules, including the chain rule, the law of total probability, and Bayes' rule
  - Explain the concept of independence of random variables
  - Describe important discrete and continuous probability distributions
-->

## Glossary

- **proportion:**  The ratio (usually expressed as a fraction) of the number of positive outcomes of the number of all possible outcomes. <br>
- **sample space:**  The set of all possible outcomes. <br>
- **random variable:** The mapping that assigns a number to each outcome in the sample space.<br>
- **success:** A positive outcome or event. Success is defined by the experimenter. It's not a value judgement: 'success' can be a good thing (a sale), but it can also be neutral (a head on a coin flip), or negative (a case of fraud). 'Success' is the outcome you are interested in knowing more about.<br>


## Joint Probability Distributions and Marginal Distributions

A joint probability distribution describes the probability of two distinct random variables (or ranges of random variables, in the continuous case) co-occuring. Joint probability distributions can lead us to marginal distributions (the distribution of one variable without respect to the other) as well as conditional probabilities (the distribution of one variable when the other variable has a specified condition).

We could have a joint probability distribution for the number of statistics books a random person owns, and the number of video game consoles someone owns. We'll keep it simple and say everyone has either 0, 1, or 2 of each.


|  | 0 Stats Books | 1 Stats Book | 2 Stats Books
---:|:---|:---|:---
0 Consoles| 0.02 | 0.20 | 0.15
1 Console| 0.10 | 0.15 | 0.20
2 Consoles| 0.03 | 0.15 | 0.05

Notice that the sum of all cells is equal to 1.0. If we wanted to know the marginal distribution of stats books, we would need to add each of the columns:
$$ P(\text{Stats Books} = 0) = 0.02 + 0.10 + 0.03 = 0.15 $$
$$ P(\text{Stats Books} = 1) = 0.20 + 0.15 + 0.15 = 0.45 $$
$$ P(\text{Stats Books} = 2) = 0.15 + 0.20 + 0.05 = 0.40 $$

The marginal probabilities should always add to one. If they don't something went wrong.

We can also compute conditional distributions. For example, what is probability distribution for consoles amongst people who own 2 stats books? This requires a little rearrangement of the familiar
$$ P(A \cap B) = P(A | B)P(B) $$
We would like to know P(A | B), which we can isolate as
$$ P(A | B) = P(A \cap B) / P(B) $$

or

$$ P(\text{Consoles} = x | \text{Stats Books} = 2) = P(\text{Consoles} = x \cap \text{Stats Books} = 2)/P(\text{Stats Books} = 2) $$

so

$$ P(\text{Consoles} = 0 | \text{Stats Books} = 2) = 0.15/0.40 = 0.375 $$
$$ P(\text{Consoles} = 1 | \text{Stats Books} = 2) = 0.20/0.40 = 0.50 $$
$$ P(\text{Consoles} = 2 | \text{Stats Books} = 2) = 0.05/0.40 = 0.125 $$

This is the probability distribution for Consoles Owned, conditional upon owning two stats books. Note that once again, the probabilities add to 1.0.

#### !challenge

* type: number
* id: 1beecbad-8e57-4d5f-8f5c-4deb959a3a3a
* title: Marginal distributions and expectation
* decimal: 2

#### !question

Given the following marginal distribution table, what is the expected value of X?

|  | X = 5 | X = 10 |
|:----|----:|----:|
Y = 1 | .40 | .05 |
Y = 2 | .25 | .30 |

#### !end-question

### !placeholder
enter your answer as an exact decimal
### !end-placeholder

### !answer
6.75
### !end-answer

#### !explanation
We must first compute the marginal distribution of X.
$$ P(X = 5) = .40 + .25 = .65 $$
$$ P(X = 10) = .05 + .30 = .35 $$
We then determine the E(X) for this discrete random variable:

$$ E[X] = \sum_{s\in S} x_s P(x_s) $$

$$      = 5 * .65 + 10 * .35 = 6.75 $$

#### !end-explanation

#### !end-challenge


#### !challenge

* type: paragraph
* id: dist_10
* title: Exploring the binomial distribution

#### !question

Visit this [coin flip simulation applet](http://www.math.uah.edu/stat/apps/BinomialCoinExperiment.html)

Keep the default settings, but set 'stop' to 'never'.

Click the play button a few times to get a feel for what's happening. Then click the fast forward button and let it run for ~30 seconds. Answer the following questions in the box below:

- about how long does it take the data to approximate the distribution?
- after a couple thousand trials, how different is the observed mean from the distribution (expected) mean? Does this surprise you? Why (not)?
- what is the significance of the 0.246 on the y-axis?

#### !end-question
#### !explanation
Be ready to share your responses during breakout.
#### !end-explanation

#### !end-challenge






