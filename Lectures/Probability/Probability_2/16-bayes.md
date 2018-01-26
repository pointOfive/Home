# Bayesian Inference (or Bayesian Analysis)

is what is comprised in the field of so-called Bayesian statistics.
The phrase Bayesian statistics is actually quite a bit of an oxymoron, though,
because Bayesians do not concern themselves with _statistics_ _per se_. 
Rather, Bayesian statisticians concern themselves with probability distribution
calculations.  The term statistics, on the other hand, is actually a technical
term that refers to a numerical calculation carried out on a sample of actualized
random variable	values (or, "data", as it might be loosely referred to 
in the course of a casual conversation). Because the statistic of the 
random variables is some mathematical calculation involving random variables,
it (the statistic) itself is also a random variable.  Therefore the 
uncertainty characteristics of the statistic can be evaluated based on the 
uncertainty characteristics of the random variables which comprise it.
This analysis is the central exercise defining exercise of the frequentist,
or classical paradigm of statistics. 
But characterizing the long term frequency behavior of sample statistics 
is not the only game in town.  Indeed, the Bayesian paradigm prescribes 
another that is not based on statistics, but distributional calculations 
only (as indicated above).  And that, and other various considerations
relative to the frequentist paradigm are what we shall consider here!
Before we begin these exploits, however, let us apologetically admit that the 
_statistics_ is also used to refer to the _field of statistics_, and in this sense
the term Bayesian statistics is a reasonable one. 

_Bayesian inference_ is based on the idea that distributional parameters
\\(\theta\\) can themselves be viewed as random variables with their
own distributions.   We've generically used \\(\theta\\) to refer to 
distributional parameters since distributional parameters
are often indicated as greek letters and \\(\theta\\) is actually
a very common greek letter used to indicate a distributions parameter(s).  
Anyway, this view of a parameter as being a random variable is 
is distinct from the frequentist perspective in which the 
parameter is viewed as being a fixed constants to be estimated. E.g.,
"If we measured everyone's height instantaneously, at that moment there would
be one true average height in the population."  Regardless of one's philosophical
perspective, both approaches have value in practice.

The key computational step in the Bayesian framework is deriving the posterior
distribution, which is done using the a formula we have already seen; namely 
Bayes' formula, or rule:  

$$ P(\theta|X) = \frac{P(X|\theta)P(\theta)}{P(X)} $$

Here, however, we shall refer to this computation as _Bayes' theorem_, 
because it sounds fancier. But also because we certainly ought to provide
a sufficient level of decorum and grandiosity to what we're doing here 
given how advanced and sophisticated it will turn out to be, oughtn't we?

Regardless, Bayes' theorem is comprised of the

* _posterior distribution_ \\(P(\theta|X)\\)
* _likelihood function_ \\(P(X|\theta)\\)
* _prior distribution_ \\(P(\theta)\\)
* _marginal likelihood_ \\(P(X)\\)

Just as the posterior distribution is the central estimand in Bayesian statistics,
the likelihood function is the central piece of machinery in a frequentist context.
But as you can see from the formula, the posterior is simply a kind of
"re-weighting" of the likelihood function.  This immediately shows that 
Bayesian and frequentist inference must not be completely at odds -- 
they agree on at least something. The re-weighting is accomplished
by striking a balance between the likelihood function and the
prior distribution. The prior distribution represents our belief about the
parameter prior to seeing the data, while the likelihood function tells us
what the data implies about the parameter -- and then these two perspectives
are reconciled to form the posterior distribution.  
The marginal likelihood (which is in the denominator) turns out to just be a constant which
ensures that the posterior is a probability mass function or a probability
density function (i.e., sums to one or has area one) so that the posterior 
is a proper distribution.  As such, in many
contexts the marginal likelihood simply represents a formality that is not
crucial to the posterior calculation; however, sometimes it can be incredibly useful 
(although it can also be incredibly difficult to obtain...).  
For example, the marginal likelihood can be used for Bayesian model selection.
So for some tasks it's easy to see that the marginal likelihood might be 
precisely the thing of primary importance that we are interested in!

# Statistical Paradigms

Bayesian inference works by updating the belief about the parameters 
\\(\theta\\) encoded in the prior distribution with the information
about the parameters contained in the observed data \\(x\\) 
as quantified in the likelihood function.
This updated belief -- called the posterior distribution -- 
can serve as the next prior distribution for the subsequent collection
of additional data and can thus itself be updated, and so on.
The updated belief is always encoded as a probability distribution,
so statements of belief about parameters are made using probability
statements. This is quite in contrast frequentist, or classical statistical
paradigms, which instead focus on characterizing uncertainty in parameter 
estimation procedures that results from random sampling variation. 
I.e., frequentist statistics as a discipline 
never makes statements about parameters, but instead makes
statements about probabilities (long-run frequency rates) of
estimation procedures.  Which does seem a little bit backwards...

## Arguments for Bayesian Analysis

### Ease of interpretability

Probability statements about parameters are more easily interpreted than confidence intervals, 
hypothesis testing and p-values  

### Utilizes prior information

The Bayesian framework is a natural mechanism to incorporate, build upon and grow information, 
i.e., learn in an sequential and iterative manner

### No "large n" asymptotic distribution requirements

Bayesian analysis is a fully coherent probabilistic framework regardless of sample size, 
whereas many frequentist methodologies (vaguely) rely upon "large n" results
    
### Complex hierarchical data models

Many complicated modeling specifications are _only_ available within the Bayesian computational framework
    
    
### Uncertainty propagation 

Bayesian analysis provides a hierarchical modeling framework that definitionally 
incorporates all modeled uncertainty into parameter estimation

### Performs regularization

The prior specification can stabilize model fitting procedures so they are less prone to overfitting data


## Arguments Against Bayesian Analysis

...and these are to be taken seriously as they represent substantial objections
largely amounting to practical, topically relevant restatements of Occam's Razor and Murphy's Law.


### Requires specification of the prior 

Allows objectivity to be sacrificed for subjectivity -- arbitrary information can be  incorporated into Bayesian analysis
    
    
### Bayesian computation has more overhead/is more expensive than Frequentist computation on a number of levels

  * Bayesian analysis requires practitioners with more advanced skill sets

  * Bayesian analysis is more difficult to implement correctly
    
  * simple Frequentist solutions often outperform complex Bayesian solutions at a fraction of total development and computational costs
    

## Next Steps

Many of the topics alluded to in this discussion have not yet been formally
introduced, so it's quite expected that some things in this conversation aren't 
going to be completely clear and fully meaningful to you yet.  Hopefully though,
at this stage, your interest was peaked and you're looking forward to learning
about all the topics addressed here.  And in that regard, you're in luck:
all of these topics will be introduced and covered slowly but surely until we 
get through everything.  For now, take a little time to give some answers to the 
following questions as a way to mark your lay out your current starting point
from which we will continue to progress though these materials. 


### !challenge

* type: paragraph
* id: bae1
* title: Philosophies

##### !question

What do you appreciate most about the *Bayesian philosophy*?

What do you appreciate about the *Frequentist philosophy*?

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation
##### !end-explanation
### !end-challenge



### !challenge

* type: paragraph
* id: bae2
* title: Are YOU a Bayesian?

##### !question

Consider the following scenarios:

  * You're playing poker to win (like your life depends on it!), and the
    person you're bidding against just tipped his hand a little too low and
    you've seen his cards...

  * You're a skilled programmer, but bugs still slip into your code. After a 
    particularly difficult implementation of an algorithm, you decide to test 
    your code on a trivial example. It passes. You test the code on a harder 
    problem. It passes once again. And it passes the next, *even more difficult*, 
    test too! You are starting to believe that there may be no bugs in this code...

  * You're a doctor who has some previous experience with the symptoms that are 
    presenting for the current patient and you've diagnosed this sort of condition
    many times before...  

Do you see yourself as a Bayesian? If so, why?

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation
##### !end-explanation
### !end-challenge
   


### !challenge

* type: paragraph
* id: bae3
* title: Are YOU SURE you're a Bayesian?

##### !question

Without looking...

Write Bayes' theorem and describe the function of the different components 
that comprise the theorem, particularly with respect to parameters and evidence.

##### !end-question
##### !placeholder
##### !end-placeholder
##### !explanation
##### !end-explanation
### !end-challenge


## Further study

If you do actually want to be a Bayesian -- fear not -- you can!
Programming in the Bayesian landscape has become incredibly easy
via the advent of _probabilistic programming_.
Here are several outstanding resources available 
that you can use to start learning more about Bayesian analysis: 

* [Entry level intro posted through kdnuggets](http://www.kdnuggets.com/2016/12/datascience-introduction-bayesian-inference.html)

* [Probabilistic Programming and Bayesian Methods for Hackers](https://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers>`_ by `Cameron Davidson-Pilon <https://github.com/CamDavidsonPilon)

* [A repository introducing probabilistic programming in Python](https://github.com/GalvanizeOpenSource/probabilistic-programming-intro)



