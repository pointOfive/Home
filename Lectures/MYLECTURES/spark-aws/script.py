import pandas as pd
tmp = pd.read_csv("https://s3.amazonaws.com/myownfirsttrybucketss/cancer.csv", chunksize=301)
# returns of "TextFileReader" type
tmp = tmp.read()

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.hist(tmp.cancer/tmp.population.apply(float))
plt.savefig("test.png")
plt.show()

import boto
access_key, access_secret_key = 'AKIAJGXK5YK45QPNDCZA', '9jg3AfuR1MqnmJ220usKp8wsY3otklYFv+YsRsd7'
conn = boto.connect_s3(access_key, access_secret_key)

b = conn.create_bucket('myownsecondtrybucketss', policy='public-read')
file_object = b.new_key('test.png')
with open('test.png') as f:
         file_object.set_contents_from_file(f, policy='public-read')

