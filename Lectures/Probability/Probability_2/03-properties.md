# Properties of PMFs and PDFs (and all "probability things")

There are three axioms of probability known as the _Kolmogorov axioms_. 
They are very simple and will come as no surprise.
What may be surprising, however, is that they are all that's needed on which 
to base the entire enterprise of "probability". But let's see what you think; without further ado, 
for the set of all outcomes \\(S_X\\) that may actualized by a random variable 
\\(X\\), a probability distribution must satisfy the following three properties:


1. The probability of any event \\(E \subset S_X\\) must be non-zero and less than or equal to 1:

   $$ 0 \leq Pr(x \in A \subset S_X) \leq 1 $$

2. The probability of a _sure_ event (that will absolutely happen) is 1:

   $$ Pr(x \in S_X) = 1 $$

3. And if events \\(E_1\\) and \\(E_2\\) are mutually exclusive, then:

   $$ Pr\left(x \in (E_1 \cup E_2)\right) = Pr(x \in E_1) + Pr(x \in E_2) $$

   where (remember that) two events are mutually exclusive if they cannot both be
   true at the same time -- i.e., the two event sets are disjoint so that \\(Pr(E_1 \cap E_2) = 0\\).

It's seems amazing (at least to me) 
that this is all it takes to define the notion of probability. But it's true.
For example, from these three axioms we can derive that, e.g., 

a. The sum of the probabilities of an event \\(E \subset S_X\\) and its complement is 1:

   $$ Pr(x \in E) + Pr\left(x \in E^C\right) = Pr(x \in S_X) = 1 $$

b. The probability of an impossible event is zero:

   $$ Pr\left(x \in S^C\right) = 0 $$

## Wrap Up

Both discrete and continuous distributions satisfy the axioms of probability, i.e.,

1. \\(0 \leq Pr(X=x \in E \subseteq S_X) \leq 1\\) and \\(0 \leq \underset{E \subseteq \mathbb{R}}{\int} f(X=x)\; dx \leq 1\\)

2. \\(\sum_{x_j \in S_X} Pr(X=x_j) = 1\\) and \\(\int_{-\infty}^{\infty} f(X=x) \; dx = 1 \\)

3. \\( \displaystyle \sum_{x_j \in (E_1 \cup E_2) \subseteq S_X} Pr(X=x_j) = 
\sum_{x_j \in E_1 \subseteq S_X} Pr(X=x_j) + \sum_{x_j \in E_2 \subseteq S_X} Pr(X=x_j) \\) 
and \\( \displaystyle \int_{(E_1 \cup E_2) \subseteq \mathbb{R}} f(X=x) \; dx = 
\int_{E_1 \subseteq \mathbb{R}} f(X=x) \; dx + \int_{E_2 \subset \mathbb{R}} f(X=x) \; dx \\)
for two disjoint events \\(E_1\\) and \\(E_2\\).





