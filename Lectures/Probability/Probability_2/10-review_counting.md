
## 2. Counting

Let's now turn to a review of counting with permutations and combinations, etc.. 
To begin with we'll do a few definitional "warm-up" questions, and then we'll 
move onto some actually counting calculations. 


### !challenge
* type: multiple-choice
* id: scott_pc2_rev16
* title: Review Problem #16
### !question
Which of the following is used to count _permutations_ of size \\(k\\) from a set of size \\(n\\)?
### !end-question
### !options
* (a) \\(\frac{n!}{(n-k)!}\\)
* (b) \\(k!\\)
* (c) \\(\frac{n!}{(n-k)! k!}\\)
* (d) \\(n^k\\)
* (e) none of the above
### !end-options
### !answer
(a) \\(\frac{n!}{(n-k)!}\\)
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev17
* title: Review Problem #17
### !question
Which of the following is the _multiplication rule_? I.e., the number of possible outcomes
for \\(k\\) independently and identically distributed draws from a unique set of size \\(n\\)?
### !end-question
### !options
* (a) \\(\frac{n!}{(n-k)!}\\)
* (b) \\(k!\\)
* (c) \\(\frac{n!}{(n-k)! k!}\\)
* (d) \\(n^k\\)
* (e) none of the above
### !end-options
### !answer
(d) \\(n^k\\)
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev18
* title: Review Problem #18
### !question
Which of the following counts the number of orderings of \\(k\\) distinct objects? 
### !end-question
### !options
* (a) \\(\frac{n!}{(n-k)!}\\)
* (b) \\(k!\\)
* (c) \\(\frac{n!}{(n-k)! k!}\\)
* (d) \\(n^k\\)
* (e) none of the above
### !end-options
### !answer
(b) \\(k!\\)
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev19
* title: Review Problem #19
### !question
Which of the following represents the "choose" notation?
### !end-question
### !options
* (a) \\(\frac{n!}{(n-k)!}\\)
* (b) \\(k!\\)
* (c) \\(\frac{n!}{(n-k)! k!}\\)
* (d) \\(n^k\\)
* (e) none of the above
### !end-options
### !answer
(c) \\(\frac{n!}{(n-k)! k!}\\)
### !end-answer
### !explanation
### !end-explanation
### !end-challenge

### !challenge
* type: multiple-choice
* id: scott_pc2_rev20
* title: Review Problem #20
### !question
Which of the following counts the number of unordered groupings of size \\(k\\)
that can be made from \\(n\\) unique objects? 
### !end-question
### !options
* (a) \\(\frac{n!}{(n-k)!}\\)
* (b) \\(k!\\)
* (c) \\(\frac{n!}{(n-k)! k!}\\)
* (d) \\(n^k\\)
* (e) none of the above
### !end-options
### !answer
(c) \\(\frac{n!}{(n-k)! k!}\\)
### !end-answer
### !explanation
### !end-explanation
### !end-challenge



#### !challenge

* type: number
* id: extra_1
* title: Distinct strings with 'name'

#### !question

How many distinct ways can we arrange the letters in the word 'name'?
#### !end-question

### !placeholder

enter your answer here
### !end-placeholder

### !answer
24
### !end-answer

#### !explanation

#### !end-explanation

#### !end-challenge

#### !challenge

* type: number
* id: extra_2
* title: Distinct strings with 'data'

#### !question

How many distinct strings can you make from the characters in the word 'data'?

#### !end-question

### !placeholder
enter your answer here
### !end-placeholder

### !answer
12
### !end-answer

#### !explanation

#### !end-explanation

#### !end-challenge


#### !challenge

* type: number
* id: extra_3
* title: Distinct strings with 'better'

#### !question

How many distinct strings can you make from the characters in the word 'better'?

#### !end-question

### !placeholder
enter your answer here
### !end-placeholder

### !answer
180
### !end-answer

#### !explanation

#### !end-explanation

#### !end-challenge


### !challenge

* type: paragraph
* id: extra_4
* title: Explain how you got those numbers

##### !question

What is the rule for counting permutations where one or more elements are identical? In other words: how would you generalize the computations you performed above?

##### !end-question

##### !placeholder

Enter your answer here

##### !end-placeholder

##### !explanation



##### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python2.7
* id: extra_5
* title: Make a function to count distinct permutations

### !question

Write a function, `count_strings()`, that takes a string and counts the number of distinct permutations of that string.

### !end-question

### !placeholder

```python
import itertools

def count_strings(string):
    '''
    INPUT: a string
    OUTPUT: an integer

    returns the number of distinct strings that can be made from the characters inside the argument string

    use itertools.permutations

    You should be able to use the function like this:
    >>> my_string = 'ab'
    >>> count_strings(my_string)
    2

    '''
    pass
```

### !end-placeholder

### !tests

```python
import main
import unittest
import itertools

class TestPython1(unittest.TestCase):

    def test_count_strings_name(self):
      result = main.count_strings('name')
      self.assertEqual(result, 24)

    def test_count_strings_data(self):
      result = main.count_strings('data')
      self.assertEqual(result, 12)

    def test_count_strings_better(self):
      result = main.count_strings('better')
      self.assertEqual(result, 180)
```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: multiple-choice
* id: extra_6
* title: Choose the right formula

##### !question

### Question

Given a fruit bowl with 6 fruits (say, for instance, a pear, a banana, an apple, a pineapple, a kiwi and a mango), you would like to know many different fruit salads you could make, such that each salad contains exactly 3 different fruits.

Which of the following expressions would give the correct answer?

##### !end-question

##### !options

* $$ 3! $$
* $$ 6!\,3! $$
* $$ \frac{6!}{3!} $$
* $$ \frac{6!}{3!\,3!} $$

##### !end-options

##### !answer

$$ \frac{6!}{3!\,3!} $$

##### !end-answer

##### !explanation



##### !end-explanation

### !end-challenge

### !challenge

* type: code-snippet
* language: python2.7
* id: extra_7
* title: Make fruit salads

### !question

Write a function that prints all possible combinations of k fruits, selected from a list of (k or more) fruits.

### !end-question

### !placeholder

```python
import itertools

def make_fruit_salad(lst, k):
    '''
    return the list of possible combinations by taking k elements from lst

    use itertools.combinations

    You should be able to use the function like this:
    >>> my_fruits = ['pear', 'banana', 'apple']
    >>> make_fruit_salad(my_fruits, 2)
    [('pear', 'banana'), ('pear', 'apple'), ('banana', 'apple')]
    '''
    pass
```

### !end-placeholder

### !tests

```python
import main
import unittest
import itertools

# concern here that a student could technically be right without matching
# the lists we test for if their lists or tuples print in a different order.
class TestPython1(unittest.TestCase):

    def test_fruit_salad_1(self):
      result = main.make_fruit_salad(['pear', 'banana', 'apple'], 2)
      correct = [('pear', 'banana'), ('pear', 'apple'), ('banana', 'apple')]
      self.assertEqual(result, correct)

    def test_make_fruit_salad_2(self):
      result = main.make_fruit_salad(['pear', 'apple', 'banana', 'mango',
                'strawberry'], 5)
      correct = [('pear', 'apple', 'banana', 'mango', 'strawberry')]
      self.assertEqual(result, correct)

```


### !end-tests


### !explanation

### !end-explanation

### !end-challenge


#### !challenge

* type: number
* id: extra_8
* title: Compute a probability using combinatorics

#### !question

You call 2 Ubers and 3 Lyfts. If the time that each takes to reach you are independent and identical distributions, what is the probability that all the Lyfts arrive first?


#### !end-question

### !placeholder

enter your answer as a decimal
### !end-placeholder

### !answer
0.1
### !end-answer

#### !explanation

#### !end-explanation

#### !end-challenge

### !challenge

* type: multiple-choice
* id: extra_9
* title: Compare another probability

##### !question

### Question

The probability that both Ubers will arrive first is _______ the probability that all 3 Lyfts will arrive first.

##### !end-question

##### !options

* less than
* equal to
* greater than


##### !end-options

##### !answer

equal to

##### !end-answer

##### !explanation


##### !end-explanation

### !end-challenge

### !challenge

* type: paragraph
* id: extra_10
* title: Explain the comparison above

##### !question

Explain why the above is true.
##### !end-question

##### !placeholder

Enter your response here.

##### !end-placeholder

##### !explanation


##### !end-explanation

### !end-challenge

#### !challenge

* type: number
* id: extra_11
* title: How many handshakes?

#### !question

Consider a group of 20 people. If everyone shakes hands with everyone else, how many handshakes take place?

#### !end-question

### !placeholder

enter your answer here
### !end-placeholder

### !answer
190
### !end-answer

#### !explanation

#### !end-explanation

#### !end-challenge
