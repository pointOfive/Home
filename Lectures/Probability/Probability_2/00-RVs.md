
# Define and work with random variables

We previously introduced (discrete and continuous) distributions, such as the Poisson and normal distribution.
But to begin with we first introduced the notion of an experiment which we referred to as \\(X\\)
which would realized an observed value which we referred to as \\(x\\) 
which could take on any value in the sample space which we referred to as \\(S_X\\) of the experiment \\(X\\).
Then later, when we got back around to talking about distributions, 
we suggested that the probabilities of the outcomes \\(x\\) could be specified using probability distributions.
Of course, the exact specification in question would be dependent on what the actual experiment \\(X\\) was. 
For example, a specific Poisson or normal distribution might be appropriate as a 
probability model for the number of cars that pass a specific corner in a 30 minute interval
or the time it takes someone to run the Boston marathon, respectively.  
We could then say that we were modeling the experiment \\(X\\) (e.g., number of car arrivals in 30 minutes
or Boston marathon time) as a Poisson or normal distribution, and that an actual observation \\(x\\) 
from this experiment would be realized as random samples from the relevant distribution.  I.e., we would say something like
"the probability of \\(x\\) cars passing here in 30 minutes is given by a Poisson distribution with parameter \\(\lambda\\)", 
or "the time it takes to finish the Boston marathon \\(x\\) will be normally distributed with parameters \\(\mu\\) and 
\\(\sigma^2\\)".

Actually, it turns out that we have not yet really introduced the primary terminology associated the
statements above.  That is, we have not yet defined a formal notion called a _random variable_.  
The reason for our delay thus far is that the notion of a random variable seems like somewhat of a technicality. 
But once we understand it, it will greatly ease our ability to express ourselves in a consistent, clear language. 
And of course, the random variable nomenclature is so ubiquitous and common that we'll have to adopt it at some point, anyway;
and now seems like the right time if there ever was one, so we might as well get this mathematical construct nailed down and on the books. 


A random variable \\(X\\) is a mapping from an outcome \\(x\\) in a sample space \\(S_X\\) onto a real valued number
(which of course could be an integer).  
This allows us to represent represent experiments numerically.  I.e., experiments \\(X\\) become random variables \\(X\\)
whose outcomes \\(x\\) and sample space \\(S_X\\) comprise numeric values.  
This may seem completely redundant and obvious and you may feel even unnecessary. But actually, e.g., when we roll
a six-sided die and see the number "5" showing on the face that landed "up", we haven't actually gotten a true numerical
value.  What we really have is a die with 'a "5" showing on the face that landed "up"'.  That is, we have some actual
random physical process with some physical state or description associated with its outcome.  The definition 
of experiments was intentionally general so that it provided a mathematical framework to describe 
such physical phenomenon with actual physical attributes and characteristics.  
That's why events were based on the notions of sets: so we could have a sufficiently general mathematical
construct with which to talk about and describe any sort of physical experiment that we might wish to consider. 
But of course to actually do numerical
calculations we need to move all these considerations into the space of calculable numbers. And this is 
where random variables come in to play.  So all of our distributions, both discrete AND continuous, were 
based on numbers.  And of course the reason for that is so that we can use these probability distributions to do numerical
calculations and actually make some meaningful statements about probabilities and physical experiments and such. 
You probably didn't take much note of it initially, but now it's obvious.
So that's all a random variable is.  It maps our theoretical mathematical framework for describing experiments 
\\(X\\) onto a numeric space where we can actually do things.  And for our purposes we can just retain the 
same notation we have already started using.  Random variables giving numerical representations of 
experiments will be denoted as (capital) \\(X\\) and actualized outcomes of these experiments will be denoted as
(lowercase) \\(x\\) and the set of all possible outcomes of the experiment -- the sample space of the experiment --
will still be denoted as \\(S_X\\).  But these will now all live in the space of real-valued numbers. 


So, formally, a _random variable_ is a mapping from a set of possible outcomes to a set of numerical values.  I.e.,

$$ X: S_X \rightarrow \mathbb{R} $$

with \\(x\\) being the realizations of this mapping upon observing the outcomes of the physical phenomenon
in question.  

Now, there are two types of random variables, discrete and continuous:

* Discrete random variables can only take on integer values, 
such as the value of a playing card or number of children in a family. I.e.,
for discrete random variables we have that

$$ X: S_X \rightarrow x \in \mathbb{N} $$

* Continuous random variables can take on *any* real value within a specified range -- 
meaning there are an uncountably infinitely many values such random variables can take on.
A common example is height -- in reality, people don't jump from being 5'6" to 5'7", or even from 5'6" to 5'6 1/4", 
but can instead have heights anywhere within a range (even if it's not precisely measurable by human instruments). I.e.,
for continuous random variables we have that

$$ X: S_X \rightarrow x \in \mathbb{R} $$

For further discussion regarding random variables, 
have a look at this [Khan academy discussion here](https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/discrete-and-continuous-random-variables/v/random-variables).  


 ### !challenge
* type: multiple-choice
* id: scott_rv_1
* title: Variables?
### !question

Does a random variable have a "value" like a variable in python or an algebraic expression?

### !end-question
### !options

* an experiment \\(X\\) can realize an outcome \\(x\\) from the sample space (i.e., the set of possible outcomes) \\(S_X\\)
* a random variable \\(X\\) represents an experiment which will produce a measured (observed) outcome that is represented numerically by \\(x\\)
* random variables \\(X\\) have probabilities associated with all their possible outcomes \\(x \in S_X\\)
* random variables are a mapping, or a function from the outcomes in an experimental sample space \\(S_X\\) to a numeric representation \\(S_X\\)
* all of the above are true statements

### !end-options
### !answer
all of the above are true statements
### !end-answer
### !explanation
### !end-explanation
### !end-challenge



#### !challenge
* type: paragraph
* id: scott_rv_2
* title: Non uniform random variables
#### !question

When we think about selecting something at random, we might instinctively feel that all outcomes are equally likely. When rolling a die, each face value is equally likely to come up. When selecting a card, each card is equally likely. What are some situations where the outcome of selecting a random variable is not distributed in this way -- where instead one outcome is more likely than another?  

Do you have any ideas about what distributions might you choose for the probabilistic modeling of these random variables?

#### !end-question
#### !explanation

#### !end-explanation
#### !end-challenge


#### !challenge
* type: paragraph
* id: scott_rv_3
* title: Exploring prediction
#### !question

Give some examples two kinds of random phenomenon -- those that seem like they could be predicted
with some accuracy and those like seem they would be difficult to predict with any accuracy -- 
and define random variables \\(X\\) and their sample space \\(S_X\\) that can be used to quantitatively represent these random phenomenon.

Do you have any ideas about what distributions might you choose for the probabilistic modeling of these random variables?

#### !end-question
#### !explanation

#### !end-explanation
#### !end-challenge
