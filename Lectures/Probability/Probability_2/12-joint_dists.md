
# Joint Probability Distributions

To kick things off here let's start with some questions using the ten card problem 
setting we previously worked on. Namely, suppose you have the following ten cards 
(and that an ace card counts as a value of 1):

$$ H = [AH, 2H, 2C, 2S, 4D, 4S, 5C, 6H, 7D, 9S] $$


#### !challenge

* type: paragraph
* id: joint_question_1
* title: Joint distribution

#### !question

How would you go about calculating the 
probability that the sum of two cards selected randomly without replacement is 10?

#### !end-question
#### !explanation

While this could be done using a "10 choose 2" calculation for the denomenator,
you still need to carefully identify all the ways two cards can sum to 10, so
how about just using this table to list out the joint sample space

    | AH | 2H | 2C | 2S | 4D | 4S | 5C | 6H | 7D | 9S 
----|----|----|----|----|----|----|----|----|----|----
 AH | NA |    |    |    |    |    |    |    |    | 10 
 2H |    | NA |    |    |    |    |    |    |    |    
 2C |    |    | NA |    |    |    |    |    |    |    
 2S |    |    |    | NA |    |    |    |    |    |    
 4D |    |    |    |    | NA |    |    | 10 |    |    
 4S |    |    |    |    |    | NA |    | 10 |    |    
 5C |    |    |    |    |    |    | NA |    |    |    
 6H |    |    |    |    | 10 | 10 |    | NA |    |    
 7D |    |    |    |    |    |    |    |    | NA |    
 9S | 10 |    |    |    |    |    |    |    |    | NA 

where the columns are the first card picked and the rows
are the second card picked and then just simply calculating

$$ \frac{6}{10^2-10} $$

The interesting thing we are doing by using this table is that we are 
directly specifying and utilizing the joint distribution of this question/problem. 

#### !end-explanation
#### !end-challenge

#### !challenge

* type: paragraph
* id: joint_question_2
* title: Conditional distribution

#### !question

How would you go about calculating the 
probability that the sum of two cards selected randomly without replacement is 10
given that the first card is a 6?


#### !end-question
#### !explanation

Using the joint distribution (or joint sample space) table again
(where the columns are the first card picked and the rows are the second card picked)
we can focus in on the relevant column

|    | AH | 2H | 2C | 2S | 4D | 4S | 5C | 6H | 7D | 9S |
----|----|----|----|----|----|----|----|----|----|----
| AH | NA |    |    |    |    |    |    |    |    |    |   
| 2H |    | NA |    |    |    |    |    |    |    |    |
| 2C |    |    | NA |    |    |    |    |    |    |    |
| 2S |    |    |    | NA |    |    |    |    |    |    |
| 4D |    |    |    |    | NA |    |    | 10 |    |    |
| 4S |    |    |    |    |    | NA |    | 10 |    |    |
| 5C |    |    |    |    |    |    | NA |    |    |    |
| 6H |    |    |    |    |    |    |    | NA |    |    |
| 7D |    |    |    |    |    |    |    |    | NA |    |
| 9S |    |    |    |    |    |    |    |    |    | NA |
----|----|----|----|----|----|----|----|----|----|----
|    |    |    |    |    |    |    |    |  9 |    |    |

and then calculate the questions answer as 

$$ \frac{2}{9} $$

The interesting thing we are doing here is focussing on a "slice" of the 
joint distribution.  This is actually the conditional distribution,
and we are deriving it based off of the joint distribution.

#### !end-explanation
#### !end-challenge



#### !challenge

* type: paragraph
* id: joint_question_3
* title: Marginal distribution

#### !question

How would you go about calculating the
probability that the first randomly drawn card is a 6?

#### !end-question
#### !explanation

While this seems quite a straight forward and direct calculation _per se_, 
we can also use our familiar table listing first and second card drawn

|    | AH | 2H | 2C | 2S | 4D | 4S | 5C | 6H | 7D | 9S |  --- |  
----|----|----|----|----|----|----|----|----|----|----|----
| AH | NA |    |    |    |    |    |    |  6 |    |    |    
| 2H |    | NA |    |    |    |    |    |  6 |    |    |    
| 2C |    |    | NA |    |    |    |    |  6 |    |    |    
| 2S |    |    |    | NA |    |    |    |  6 |    |    |    
| 4D |    |    |    |    | NA |    |    |  6 |    |    |    
| 4S |    |    |    |    |    | NA |    |  6 |    |    |    
| 5C |    |    |    |    |    |    | NA |  6 |    |    |    
| 6H |    |    |    |    |    |    |    | NA |    |    |    
| 7D |    |    |    |    |    |    |    |  6 | NA |    |    
| 9S |    |    |    |    |    |    |    |  6 |    | NA |    
----|----|----|----|----|----|----|----|----|----|----|----
|    |    |    |    |    |    |    |    |  9 |    |    | 90 

and compute this answer as 

$$ \frac{9}{9*10} $$

The interesting thing that we are doing here is deriving the marginal
distribution from the joint distribution.

#### !end-explanation
#### !end-challenge


#### !challenge

* type: paragraph
* id: joint_question_4
* title: Marginal distribution

#### !question

How would your answers change (if at all) 
if the cards were sequentially randomly selected WITH REPLACEMENT?

#### !end-question
#### !explanation

The probability of two cards summing to 10 increases a little bit
because there's now another card that can make a contribution:
$$ \frac{7}{100} $$

The probability of two cards summing to 10 given that the first
one drawn was a 6 decreases a little bit
because there's now another potential card to be drawn 
that can't make a contribution:
$$ \frac{2}{10} $$

The marginal probability of the first card remains unchanged
since it is unaffected by the manner in which the second card 
is drawn; and regardless, this is confirmed through the joint
distribution using the new denominator:
$$ \frac{10}{10*10} $$

This of course can all be done on the basis of the (new) joint
distribution introduced in this problem:

|    | AH | 2H | 2C | 2S | 4D | 4S | 5C | 6H | 7D | 9S |     |
----|----|----|----|----|----|----|----|----|----|----|----
| AH |    |    |    |    |    |    |    |    |    | 10 |     |
| 2H |    |    |    |    |    |    |    |    |    |    |     |
| 2C |    |    |    |    |    |    |    |    |    |    |     |
| 2S |    |    |    |    |    |    |    |    |    |    |     |
| 4D |    |    |    |    |    |    |    | 10 |    |    |     |
| 4S |    |    |    |    |    |    |    | 10 |    |    |     |
| 5C |    |    |    |    |    |    | 10 |    |    |    |     |
| 6H |    |    |    |    | 10 | 10 |    |    |    |    |     |
| 7D |    |    |    |    |    |    |    |    |    |    |     |
| 9S | 10 |    |    |    |    |    |    |    |    |    |     |
----|----|----|----|----|----|----|----|----|----|----|----
| 9S |    |    |    |    |    |    |    | 10 |    |    | 100 |

(And of course, as has been our habit, 
columns are the first card picked and the rows are the second card picked.)

The interesting thing that happened in this problem is that 
the marginal distributions of the first and second card went from being 
dependent to being independent (and identically distributed).  
So in this problem the random variables of our joint distribution are i.i.d..

#### !end-explanation
#### !end-challenge


Actually, with these four questions we have already introduced 
(in the same order) the key 
components of multivariate probability distribution theory; namely

- Joint Distributions
- Conditional Distributions
- Marginal Distributions
- Independently and Identically Distributed (i.i.d.) Random Variables

The distributions here are comprised of the sets of cards available to select at each draw 
(each with equal probability of being drawn) and the random variable is the function
mapping each drawn card to a number (Aces are 1, two's are 2, etc.). 
And notice that these four concepts were introduced in manner 
based exactly on a perfect correspondence to the previously introduced
joint probability theory of multiple events; namely 

- Joint Probability
- Conditional Probability
- Marginal Probability
- Independently and Identically Distributed (i.i.d.) Experiments

Given that this is how these topics have been reintroduced, 
you will likely be quite unsurprised to hear that distributions for
multiple random variables follow the same types rules as the probabilities of multiple events.
Indeed, all the statements that were made for joint probabilities of multiple events 
have straight forward analogous applications for distributions of multiple random variables.
But of course probability distributions and their associated random variables 
should follow the same rules: they represent and model probabilities!  
We will net go ahead and formalize these rules for random variables and probability distributions
with some formal mathematical definitions. 

