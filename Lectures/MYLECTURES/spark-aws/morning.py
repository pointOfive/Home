

import pyspark as ps
ps_sql = ps.sql.SparkSession.builder.appName("df lecture").getOrCreate()

#ps_sql.read.json('http://jmcauley.ucsd.edu/data/amazon/... it's in a local repo: data/reviews_Musical_Instruments_5.json.gz')
jmcauley_url = 'http://snap.stanford.edu/data/amazon/productGraph/categoryFiles/reviews_Musical_Instruments_5.json.gz'
df_reviews = ps_sql.read.json(jmcauley_url)
# can't do http... only s3 or local 
################s3a://galvanize-ds-bak/yelp_academic_dataset_business.json.gz
# https://s3.amazonaws.com/scottschwartzs3bucket/Musical_Instruments_5.json

jmcauley_url = 's3a://scottschwartzs3bucket/Musical_Instruments_5.json'
df_reviews = ps_sql.read.json(jmcauley_url)
df_reviews.printSchema()

print(df_reviews.count())

df_corpus = df_reviews.select('reviewText', 'overall')

df_corpus.printSchema()

from pyspark.sql.functions import count

from pyspark.sql.functions import count
res_test = df_corpus.groupBy("overall").agg(count("overall"))

classes_count = dict(res_test.collect())
print("class representation: {}".format(classes_count))

balanced_classsize=217
from pyspark.sql.functions import rand
dataset_neg = df_corpus.filter(df_corpus["overall"] <= 1.0).orderBy(rand()).limit(balanced_classsize)
dataset_pos = df_corpus.filter(df_corpus["overall"] >= 5.0).orderBy(rand()).limit(balanced_classsize)
df_posnegdataset = dataset_pos.union(dataset_neg)

df_posnegdataset = df_posnegdataset.withColumn("label", (df_posnegdataset['overall']-1.0)/4.0)

# notice that you need the "hadoop" user
# scp -i ~/.ssh/mysecondkey.pem nlp_pipeline.py hadoop@ec2-52-71-30-92.compute-1.amazonaws.com:~/
# and yes it worked: 
# ssh -i ~/.ssh/mysecondkey.pem hadoop@ec2-52-71-30-92.compute-1.amazonaws.com


from nlp_pipeline import indexing_pipeline
df_output, vocab = indexing_pipeline(df_posnegdataset, inputCol="reviewText")





def import_my_special_package(x):
  from nlp_pipeline import indexing_pipeline
  return x

int_rdd = sc.parallelize([1, 2, 3, 4])
int_rdd.map(lambda x: import_my_special_package(x))
int_rdd.collect()


