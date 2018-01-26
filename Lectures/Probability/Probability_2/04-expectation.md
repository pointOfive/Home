# Expectation

To begin this section, let's warm up with a few exercises that we can use to
slowly work our way into the topic we're studying.

For the next three questions, suppose you have the following 10 cards in your hand:

$$ H = [AH, 2H, 2C, 2S, 4D, 4S, 5C, 6H, 7D, 9S] $$


#### !challenge
* type: number
* id: expect_1
* title: Compute a probability 1
* decimal: 1
#### !question

What is the probability of randomly selecting a card of value 4?

#### !end-question

### !placeholder
enter your answer as a decimal here
### !end-placeholder

### !answer
0.2
### !end-answer

#### !explanation
There are ten cards in our hand, of which 2 have face value 4. 
So if \\(X\\) is the random variable capturing a drawn cards fact value,
then \\(Pr(X=4) = 2/10 = 0.2\\)
#### !end-explanation

#### !end-challenge



#### !challenge

* type: number
* id: expect_2
* title: Compute a probability 2
* decimal: 1

#### !question

What is the probability of randomly selecting a card of value 3 or less?
Consider an Ace to have value 1.

#### !end-question

### !placeholder
enter your answer as a decimal here
### !end-placeholder

### !answer
0.4
### !end-answer

#### !explanation
\\(Pr(X<=3) = Pr(X=3) + Pr(X=2) + Pr(X=1) = 0/10 + 3/10 + 1/10\\)
#### !end-explanation

#### !end-challenge

#### !challenge

* type: number
* id: expect_3
* title: Compute an expectation 1
* decimal: 1

#### !question

Assuming an Ace to have value 1, if you hypothetically drew a single card from
this set of 10 over and over (with replacement, obviously), what value would you 
expect to get on average? 

Hint: the answer is of course \\(42 \times 10^{-1}\\), but we're not just looking for answers here...
we're looking for you to know how to compute the answer!
#### !end-question

### !placeholder
enter your answer as a decimal here
### !end-placeholder

### !answer
4.2
### !end-answer

#### !explanation
One tenth of the time you'd get a 1, three tenths of the time you'd get a 2,
two tenths of the time you'd get a 4, ..., etc., so 

$$
\begin{align}
\operatorname{E}_X[X] &= 1\times Pr(X=1) + 2\times Pr(X=2) + 4\times Pr(X=4) + 5\times Pr(X=5) + 6\times Pr(X=6) + 7\times Pr(X=7) + 9\times Pr(X=9)\\
&= 1\times \frac{1}{10} + 2\times \frac{3}{10} + 4\times \frac{2}{10} + 5\times \frac{1}{10} + 6\times \frac{1}{10} + 7\times \frac{1}{10} + 9\times \frac{1}{10} 
\end{align}
$$

where \\(\operatorname{E}_X[X]\\) is a notation that we will introduce next
(i.e., hold on and suspend disbelief for just a moment more!).

If this answer just seems weird and you're really not sure what's going on here, don't worry!
Move on to the reading of the exposition below and then come back around to this explanation after 
you've got a better sense of what's going on. Then the solution here will probably make more sense!

#### !end-explanation

#### !end-challenge



# Expectation

The _expectation_, or _expected value_, of a random variable -- notated as \\(\operatorname{E}_X[X]\\) --  
can be thought of as the average (specifically, the mean) 
of all possible outcomes weighted by their respective probabilities. 
If we think of a single fair coin flip and assign 0 to heads and 1 to tails, 
we can expect over the long run to have an average flip value of 0.5. 
Or, how about the expected value of a six-sided die roll?
Well, if we add up the values 1 through 6 and divide by 6 (since they're all equally likely), we get \\(21/6 = 3.5\\).

What about a four-sided die where one face is a 3 and the other three faces are 5s? 
Intuitively we can sense that the average roll won't be the average of these two numbers, 
but that it will instead be closer to 5 than to 3. How much closer? 
We could add up all the faces: 3 + 5 + 5 + 5 = 18 and divide by 4 to get 4.5. 
Or we could also say that \\(Pr(roll=3) = 1/4 = 0.25\\) and \\(Pr(roll=5) = 3/4 = 0.75\\)
and then  take the sum of the product of each value and its probability, i.e.,

$$ 3\times 0.25 + 5 \times 0.75 = 0.75 + 3.75 = 4.5 $$

Mathematically, these two approaches are equivalent.  But it's the second method that most efficiently describes 
the notion of an _expected value_ of a discrete random variable; namely


$$ 
\begin{align}
\operatorname{E}_X[X] = &  \underset{x_k \in S_X}{\sum}  x_k Pr(X=x_k) \\\\
= & \; x_1 Pr(X=x_1) + x_2 Pr(X=x_2) + \cdots 
\end{align}
$$


for every outcome \\(x_k \in S_X\\).  The _summation notation_ \\(\displaystyle \sum_{x_k \in S_X}\\)
is a very convenient way to express a summation without having to explicitly write out every single term involved.
It's a somewhat fancy notation -- and a very common notation that's used all the time --
that you'll want to keep at the ready in case you want to impress your friends
(or neatly and efficiently express a mathematical idea here or there). And in that regard, a further way 
that this summation notation is utilized is based on the fact that for discrete random variables the the outcomes 
\\(x_k \in S_X\\) can be enumerated, i.e., \\(k = 1, 2, \cdots \\) where the sequence 
may or may not terminate (i.e., go to infinity or not).  For example, \\(k = 1, 2, \cdots n\\) for a binomially
distributed random variable but \\(k = 1, 2, \cdots \\) with no end for a Poisson distributed random variable.  
Therefore it is very common to see the notational forms analogous to the following: 

$$ \sum_{k=1}^n x_k \quad\text{or}\quad \sum_{k=1}^{\infty} x_k $$

One final note on notation here is that we will return to the reason for the subscript \\(X\\) on \\(\operatorname{E}_X\\) in the next section.
For now, suffice it to say that this notation explicitly ties the expectation operator to the random variable \\(X\\).
Often this is implied and obvious and so this redundancy is not always utilized (or necessary), 
but it doesn't hurt to be explicit here for now. 

Okay, so moving on from notational considerations, always remember 
that a random variable is a mapping of the sample space of an experiment onto numerical values. 
So, for example, we could use a die to do our random sampling for a game where we win five points 1/3 of the time, 
and lose two points 2/3 of the time. We could map our outcomes to the die as (for example):

1 &rarr; +5<br>
2 &rarr; +5<br>
3 &rarr; -2<br>
4 &rarr; -2<br>
5 &rarr; -2<br>
6 &rarr; -2<br>

and in this case our expected number of points for one roll is
$$ 5 \times \frac{1}{3} + (-2) \times \frac{2}{3} = \frac{1}{3} $$


## Try it out!

For the final challenge questions of this section, consider the following context: 
 
A gambling book recommends the following "winning strategy" for the game of roulette: Bet $1 on red. 
If red appears (which has probability 18/38), then take the $1 profit and quit. 
If red does not appear and you lose this bet (which has probability 20/38 of occurring), 
make additional $1 bets of red on each of the next two spins of the roulette wheel and then quit. 
Let \\(X\\) be the random variable capturing your winnings (or losses) when you quit.

### !challenge

* type: number
* id: expect_4
* title: Probability of winning
* decimal: 2

##### !question

Find P(X > 0)

##### !end-question

##### !placeholder

Enter your answer as a decimal rounded to two decimal places

##### !end-placeholder

##### !answer
0.59
##### !end-answer

##### !explanation


The way to win is to win right away (18/38), 
or lose but then win both times the second time (20/38 * 18/38 * 18/38) (so you make your loss back and win $1 too).


\\(\frac{18}{38}\\): $1 (1 down get 2 back)

\\(\frac{20}{38} \times \frac{18}{38} \times \frac{18}{38}\\):  $1 (lost 1, 1 down 2 back, 1 down 2 back = 1)

\\(\frac{20}{38} \times \frac{18}{38} \times \frac{20}{38}\\): -1 (lost 1, 1 down 2 back, 1 down lost it = -1)

\\(\frac{20}{38} \times \frac{20}{38} \times \frac{18}{38}\\): -1 (lost 1, 1 down lost it, 1 down 2 back = -1)

\\(\frac{20}{38} \times \frac{20}{38} \times \frac{20}{38}\\): -3

\\(Pr(X=$1) = \frac{18}{38} + \frac{20}{38} \times \frac{18}{38} \times \frac{18}{38}\\)


##### !end-explanation

### !end-challenge

### !challenge

* type: number
* id: expect_5
* title: Find expectation
* decimal: 3

##### !question

Find \\(E[X]\\)

##### !end-question

##### !placeholder

Enter your answer as a decimal rounded to three decimal places

##### !end-placeholder

##### !answer
-0.108
##### !end-answer

##### !explanation

\\(\operatorname{E}_X[X] =  \frac{18}{38} \times 1 +  \frac{20}{38}\times  \frac{18}{38}\times  \frac{18}{38}*1 +  \frac{20}{38}\times  \frac{18}{38}\times  \frac{20}{38} \times (-1) +   \frac{20}{38}\times  \frac{20}{38}\times  \frac{18}{38} \times (-1) + \frac{20}{38}\times  \frac{20}{38}\times  \frac{20}{38}\times (-3)\\)

##### !end-explanation

### !end-challenge

### !challenge

* type: paragraph
* id: expect_6
* title: Winning strategy?

##### !question

Considering your findings, are you convinced that the strategy is indeed a “winning” strategy?

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation

So you have a greater than 50/50 chance of winning. 
But if you continually did this strategy over and over you would
expect to lose money, despite winning over half the time...

So do you like this strategy?

##### !end-explanation
### !end-challenge


## Wrap Up

The notion of expectation extends to continuous random variables, but we must (a) replace the summation notation with its  
integral analog and (b) use the probability density function of the random variable \\(f_X(x)\\) 
rather than the probability mass function \\(Pr(X=x)\\), i.e.,

$$ \operatorname{E}_X[X] =  \overset{\infty}{\underset{-\infty}{\int}}   x f_X(x) \mathrm{d}x $$







