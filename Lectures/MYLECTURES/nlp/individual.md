NLP and Information Retrieval
============================================================================

![pipes](images/supervised_scikit_learn.png)

Setup
===============================
In this exercise, we'll be using MongoDB. To start the mongodb service, run ```sudo mongod``` in the terminal.

Without closing the terminal tab, open a new terminal tab and run ```mongoimport --db nyt_dump --collection articles  articles_mongoimport.json --batchSize 1```


This data will be used for the rest, and throughout the exercise. We will be transforming the data set (documents) into a full bag of words that can be used for topic modeling and other advanced NLP techniques.

Loading your data from Mongo
===========================================

1. After doing the above import, load all of the article content from the collection into a list of strings where each individual string is a NY Times article. 

    **Note:** the `"content"` field is a list of strings. You should just join these together, separated by white space.

    Here's a rough start.

    ```python
    from pymongo import MongoClient
    client = MongoClient()
    db = client.nyt_dump
    coll = db.articles
    for document in coll.find():
        ### ....
    ```
 
The content from each item in the collection, the parsed out article contents, should have no html or anything left. This will be our initial document set that we'll tokenize later on.

Text Processing Pipeline
===================================

**Goal:** Build a basic text processing pipeline to compare the documents. Let's play with nltk here. 

* Remember, a text processing pipeline involves tokenization, stripping stopwords, and stemming.

Tokenization and Stop words
====================================

```python
from nltk.corpus import stopwords
```

1. Use nltk's [word_tokenize](http://www.nltk.org/api/nltk.tokenize.html#nltk.tokenize.punkt.PunktLanguageVars.word_tokenize) to tokenize the documents.

    You should end up with a list of lists, like this:

    ```python
    [['this', 'is', 'the', 'first', 'document'], ['here', 'is', 'another', 'document']]
    ```

    Note: Don't forget to lowercase the strings!

2. Remove all the stop words. You should use nltk's stopwords (check out section 4.1 in [nltk book ch 2](http://www.nltk.org/book/ch02.html)).

    For best performance, make the stop words a set instead of a list.

Stemming/Lemmatization
====================================================

Now that we have seen how to create a list of documents (lists of strings which are tokens), let's go through and stem / lemmatize each token. See [stemming](http://www.nltk.org/howto/stem.html) page and [lemmatization](http://www.nltk.org/_modules/nltk/stem/wordnet.html) page.

```python
from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

porter = PorterStemmer()
snowball = SnowballStemmer('english')
wordnet = WordNetLemmatizer()
```

1. Try running both stemmers and the lemmatizer on the documents. They only modify one word at a time, so you'll need to do a double for loop to apply the stemmer/lemmatizer to each word in all the documents.

    Save the results in 3 separate variables.

2. Compare the results. What do you notice are the differences between the two stemmers and the lemmatizer? Write your results as comments in your code!

3. Choose one of the 3 to use from here on out.

Bag Of Words and TFIDF
===================================================

1. Create your vocab, a set of words UNIQUE over the whole corpus (list of documents which are lists of strings). A `set` is a good datatype for this since it doesn't allow duplicates. At the end you'll want to convert it to a list so that we can deal with our words in a consistent order.

    We call this the *bag of words*.

2. Create a reverse lookup for the vocab list. This is a dictionary whose keys are the words and values are the indices of the words (the word id). This will make things much faster than using the list `index` function.

3. Now let's create our word count vectors manually. Create a numpy matrix where each row corresponds to a document and each column a word. The value should be the count of the number of times that word appeared in that document.

4. Create the document frequencies. For each word, get a count of the number of documents the word appears in (different from the number of times the word appears!).

5. Normalize the word count matrix to get the term frequencies. This means dividing each term frequency by the l2 (euclidean) norm. This makes each vector have a length of 1.

6. Multiply the term frequency matrix by the log of the inverse of the document frequencies to get the tf-idf matrix.

    Note: we add one to the denominator to avoid dividing by 0.

7. Normalize the tf-idf matrix as well by dividing by the l2 norm.


Using sklearn
=========================

Unsurprisingly, you don't actually have to do this by hand. You can use sklearn's [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) and [TFIDFVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)

Here's what your code should look like:

```python
vect = CountVectorizer(stop_words='english')
word_counts = vect.fit_transform(documents)
```

Note that `documents` here is a list of strings (pre-tokenized).

It will remove the stop words for you.

You can also use the same tokenization process that you did above by using the `tokenize` parameter, but you will need to write a `tokenize` function.

1. Write the `tokenize` function. It should use nltk's `word_tokenize` as well as the stemmer or lemmatizer that you chose to use.

    ```python
    def tokenize(doc):
        '''
        INPUT: string
        OUTPUT: list of strings

        Tokenize and stem/lemmatize the document.
        '''
    ```

2. Apply the `CountVectorizer` on the whole corpus. Use your `tokenize` function from above. Do you get the similar results as you did when you created this by hand?

    You can use `vect.get_feature_names()` to get the ids of the words.

3. Apply the `TfidfVectorizer`. Compare it to your tfidf results from above.

    Note: You may get slightly different values since there are some different varieties with where you add 1.


Extra Credit 1: Cosine Similarity using TFIDF
========================================================

Now that we're comfortable with tokenizing documents, let's use the cosine similarity to find similar documents.

1. Use sklearn's [linear_kernel](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.linear_kernel.html) to compute the cosine similarity between two documents.

    Use the vectors created above with the tfidf vectorizer.

    Here's a page on cosine similarity from [sklearn documentation](http://scikit-learn.org/stable/modules/metrics.html#cosine-similarity) and a relevant [stack overflow post](http://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity).

2. Now iterate over all possible pairs (as in 2 for loops iterating over the same list of documents) print the cosine similarities of their tfidf scores for each documents bag of words.

Extra Credit 2: Part of speech tagging
========================================

As a side note, let's take a quick look at Part of speech tagging. These part of speech tags can be used as features.

You can see the documentation on the part of speech tagger in the [nltk book ch 5](http://www.nltk.org/book/ch05.html)

1. Since part of speech tagging takes a long time, pick off a single document.

2. Create a part of speech tagged version of the document. Which version of your documents should you use? The original tokenized one, the one with stop words removed, or the stemmed version? Try all of them and take a look at the results to see which one performs the best.

3. What happens if I part of speech tag my bag of words? Does it perform well? Why or why not?
