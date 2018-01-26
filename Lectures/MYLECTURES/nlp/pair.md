
# Part 1: Implementing Naive Bayes

In this exercise you will implement Naive Bayes classification in Python. You should rely primarily on counters and dictionaries instead of numpy arrays for this implementation.

Recall the formulas we use for Naive Bayes:

![likelihood](images/likelihood2.png)

Let's unpack this a bit.  The numerator is the number of times a word from the document in question appears in each class from the training set plus a Laplace smoother.  The denominator is the total number of words in each class from the training set with additional smoothing.

Notice that these probabilities are simply the probability that the word you are investigating would be drawn at random from all of the documents in a given class (with smoothing).

And here's how we calculate the probability that the document in question belongs to a class:

![posterior](images/posterior.png)

Here we determine the probability of a class given a document.  This probability is given by the frequency of each class in the training set `P(y)` plus the sum of the probabilities that each word in the document would be drawn at random from the class you are investigating `sum(P(x_i|y))`.  You will need one of these probabilities for each class in your training set.  Choose the class with the largest probability.

The summation here explains that we need to sum the probabilities for each word in the document we are investigating. <a href='http://scikit-learn.org/stable/modules/naive_bayes.html'>Sklearn's formulation is pretty good too.<a>

1. Open src\naive_bayes.py and look at the 'fit' method in the NaiveBayes class definition. This method calculates the prior probabilities.  In this case the prior is just the frequency of each class in the training set.

2. Implement the `_compute_likelihoods` method. This is the majority of work we will need to do to train the model.

    * The `class_counts` attribute should contain the total number of samples in all the features for each class. This is denominator (minus the smoothing) from above. The keys should be the classes.

    * The `class_feature_counts` attribute should contain the number of occurrences of each word (feature) for each class. This is a dictionary of dictionaries (technically a defaultdict of Counters). This is numerator from above. You should be able to access this dictionary like this: `class_feature_counts[class y][feature j]`.

    This is in fact all that we need to precompute. We will be doing the Laplace smoothing when we do predictions. As you go, you can run `nosetests tests/test_nb.py` to verify you've correctly implemented each method.

3. Implement the `posteriors` method. For each row in the feature matrix `X` and for each potential label, you will need to calculate the log likelihood. You should follow the formula from above.

    The `predict` method then returns the class with the largest probability for each data point.

4. Run `nosetests tests/test_nb.py` to verify you've correctly implemented.

5. Use the function `run_naive_bayes.load_data` to load the NY Times dataset from this morning. This will load two sections and tokenize them. To reduce running time we're only loading the 'Sports' and 'Fashion & Style' articles, but feel free to modify and play around with that.

# Part 2: Applications of tf-idf and cosine similarity

Tfidf can be used for purposes other than just classification. In this exercise we will explore using tfidf to highlight important topics and to compare the topics of different documents.

For this exercise we will use the [20 News groups corpus](http://qwone.com/~jason/20Newsgroups/) (a canonical NLP text). [scikit-learn](http://scikit-learn.org/stable/datasets/twenty_newsgroups.html) and [nltk](http://www.nltk.org/nltk_data/) both have utilities for loading in the dataset, but you can use any library you so choose ([textblob](http://textblob.readthedocs.org/en/dev/), [pattern](http://www.clips.ua.ac.be/pattern) are two others). The latter half will deal with the NYT articles we have gotten.

## Feature importances

For a given corpus you can rank words (features) by their average (or total) tf-idf score across documents or simply consider words with the highest term frequency across your corpus.

1. For the 4 of the 20newsgroups corpus (your choice), find the 10 most important words by:
    * total tf-idf score
    * average tf-idf score (average only over non-zero values)
    * highest tf (only) score across corpus (try using `use_idf = False` in `TfidfVectorizer` )

2. Do the top 10 words change based on each of the different ranking methods?

3. Also do this for each category of article (each of the 20 newsgroups) and compare the top words of each. You should treat each category of newsgroup as a separate "corpus" for this question.

## Ranking

You can use cosine similarity to rank the relevance of a document to a given search query using the following process:
* Convert a search query into a feature vector, treat the query as a document in your corpus and apply tf-idf vectorizing to it.
* Normalize your query vector and all of your document vectors (since documents are often much longer than a query)
* Compute the cosine similarity between the search query and each of your documents
* Rank the documents by their similarity score

Sample queries are available in `data/queries.txt`.

1. For each query, find the 3 most relevant articles from the 20 Newsgroups corpus.


# Extra Credit: SQL Practice with NLP and NYT data set

In this exercise, you will implement TFIDF using SQL.

Here's an overview of what we'll be doing:

1. Create SQL tables
2. Parse articles: single string of text => tokenized words
3. Index words + documents into SQL tables
4. Using SQL, calculate bag-of-words vectors for each document
5. Apply tf-idf weighting to feature vectors

## Setup

We are going to be building the following SQL tables to contain the article data. You're going to write a python script using `psycopg2`.

__urls__

| id | url | label |
| :--:| :--| :--: |
| 1 | `"http://nyt.com/hotdogs_in_the_park..."`| Dining & Wine |
| 2 | ...| ... |
| ... | ...| ... |

__wordlist__

| id | word |
| :--:| :--|
| 1 | "dog"|
| 2 | "car" |
| ... | ...|

__wordlocation__

| id | url_id | word_id | location|
| :--:| :--| :--| :--|
| 1 | 54 | 2 | 523 |
| 2 | 1 | 1 | 12 |
| ... | ...| ... | ...|

__urls table:__ mapping of url, label => url_id

__wordlist table:__ mapping word => word_id

__wordlocation table:__ connect words => urls. (location is position of word in article, i.e. "dog" is the 12th word in "http://nyt.com/hotdogs_in_the_park...")

You'll be using your work from this morning that extracted the words from the `articles_mongoimport.json`.

1. First create an 'articles' database and the tables you need. Recall how to use `psycopg2`:

    ```python
    import psycopg2

    conn = psycopg2.connect(dbname='articles', user='postgres', host='/tmp')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE urls (
                       id integer PRIMARY KEY,
                       url text,
                       label text);''')
    ```

    Primary keys are useful for ensuring that there's only one entry with a given id. They also serve the purpose of making lookups by id fast.

2. Write a for loop to go over all the documents in the dataset and do an SQL insert. Your insert will look something like this:

    ```python
    cur.execute('''INSERT INTO urls VALUES (%d, '%s', '%s'); % (url_id, url, label)''')
    ```

3. Use some method of tokenization from the morning to split your documents into tokens. Also remove stop words and use stemming.

4. Write a loop to go over all of the words in all the documents.

    * If the word is new, add it to the `wordlist` table and assign it an id. It might be helpful to remember these ids in a python dictionary.
    * Add the word to the `wordlocation` table. Note that the columns you need to include are `id`, `url_id`, `word_id` and `location`. The location is what word number it is in the given document. The actual word won't be in this table.

6. You can also uses an [index](http://www.postgresql.org/docs/9.1/static/indexes-intro.html) to make lookups fast. Create indices for the following columns:

    * `word` in the `wordlist` table
    * `word_id` and `url_id` in the `wordlocation` table

7. This is essential what people call an "inverted index". Inverted indices are often used in information retrieval and search to find relevant documents. Write a python function that takes a search query to return all the articles containing those words.

    * You should first tokenize the query in the same manner you tokenized your documents
    * Strip out stop words
    * Use `psycopg2` to run the appropriate SQL query to get the result

## Bag of words

Yay! We now have a text index of (part of) the NYT. Now lets put those words into bags! In a [bag-of-words](http://en.wikipedia.org/wiki/Bag-of-words_model) model, each word has a unique index in the feature vector. This vector will be as wide as our corpus (i.e. the English language). In order to implement this in SQL, we will not need to actually create a separate (and VERY wide) table. This would be somewhat bad. Instead we will use our `wordlist` table. Its second column appropriate maps each word to a position in our feature vectors.

1. For our bag-of-words (and tf-idf) we will be calculating them using our tables.  Bag-of-words should be quite simple now that we have indexed our words.

    Write a query to create a `bag` table, so that we have all the necessary data in one table:
    * Join (INNNER should be fine) `wordlocation` and `wordlist` to link a `url_id` with the words the article contains.  We can `GROUP BY` `url_id` and `word`.
    * Do a COUNT on this group to create a new table of our bag of words. Add an additional column of the count of each word. This table should have columns for: `word_id`, `url_id`, and `count`.

    This table is our bag (of words).

2. [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) is a short hop away from a bag.  We basically need to update our counts based on the total occurrence of words across all articles.  I will leave it up to you to use SQL aggregates and the method we have used above to create a [view](http://www.postgresql.org/docs/9.2/static/sql-createview.html) for tf-idf weighting as well.

   ![tf](https://upload.wikimedia.org/math/5/c/c/5cc18acd4dbd9be636047fc2a7a10105.png)

   ![idf](https://upload.wikimedia.org/math/6/9/1/691e665ba9ae9448219cedb8365bf961.png)

# Extra Credit: Tuning and Model Comparison

Try to run each of these other classifiers over the dataset and compare the results. We're going to start with the pickle file `data.pkl`. This dataset has 1405 articles.

1. Load in the data from the pickle file:

    ```python
    import cPickle as pickle

    with open('data/data.pkl') as f:
        df = pickle.load(f)
    ```

2. To create the label vector `y`, use sklearn's [LabelEncoder](http://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.LabelEncoder.html) to convert the strings to integers.

3. For all of your models, you should use [TfidfVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html) to create a feature matrix of the text.

    Tf-idf will create a feature matrix where each word is a feature.

    **Note:** You should fit the tfidf vectorizer on the *training set only*! Don't use the test set to build your training feature matrix, or you are using the test set to help build your model! You should do something like this, if `data` is a list of strings of the text of the documents.

    ```python
    data_train, data_test = data[train_index], data[test_index]
    tfidf = TfidfVectorizer()
    X_train = tfidf.fit_transform(data_train)
    X_test = tfidf.transform(data_test)
    ```

4. Use sklearn's implementation of Naive Bayes: [MultinomialNB](http://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html). Use cross validation to find the optimal value for the laplace smoothing constant.

5. Try running the classifiers we've learned about so far:

    * Logistic Regression
    * kNN
    * Decision Tree
    * Random Forest
    * AdaBoost
    * Gradient Boosting
    * SVM
    * Naive Bayes

    Note that to use some of these models, you will need to use tactics to deal with multiple classes. SVMs and Logistic Regression only work on binary predictions. kNN, Decision Trees, Random Forests and Naive Bayes are naturally multiclass. There are two techniques for dealing with making multiclass classification problems into binary problems:

    * One-Vs-All: For each of the labels, build a model which predicts True or False for that label. (faster!)
    * One-Vs-One: For each pair of labels, build a model which predicts which of those two labels is more likely.

    Sklearn has these implemented already, and you can read about them [here](http://scikit-learn.org/stable/modules/multiclass.html).

    In the interest of time, use any cross validation technique you see fit.

    Which models get the best accuracy?

    If you have time, do a grid search to get the best parameters for each model so you can do a fair comparison.

6. Use the `time` module to get the runtime of each of the models like this:

    ```python
    import time

    start = time.time()
    # do some stuff
    end = time.time()
    print "total time:", end - start
    ```

    Which models are the fastest to train? To predict?

7. Instead of using KFold, use [LeaveOneOut](http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.LeaveOneOut.html). This is more time consuming but maybe gets a better measure of the score. This will take a few hours to run, so don't just sit there waiting! It's sometimes worth doing if you have the time and want the accuracy, but it's worth understanding the tradeoffs.


# Extra Credit: NYT Ranking

Now that we have our bag of words and tf-idf scores we can start ranking.  Revisiting your query method, we can order our returned results intelligently.

1. Using what we did at the start of this exercise (but this time in SQL), for a given query return the top three documents ranked by (aggregate) tf-idf score.  In other words, sum the tf-idf scores for the documents that contain the words in the query and return the top 3 that have the highest sums.

2. The second technique to rank results is to consider where in the document the query occurs.  For a given query:
    * Sum up the word locations (from the wordlocation table) for each word in a query for each document. (if a word appears in multiple locations use the lowest).
    * Rank by lowest word location sum.  To compare these scores with the tf-idf tanking you must normalize them to be between 0 and 1 and invert them where the article with the lowest word location sum gets a 1 on this scale.

3. Combine the tf-idf ranking and the word location ranking into one aggregate metric.  You may want to weight each differently.  Change the weights and see if it affects the return documents.
