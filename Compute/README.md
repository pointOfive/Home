# Computing

I've worked in scientific computing contexts for over 15 years 
using primarily [Python, R, SQL, C++](https://github.com/pointOfive/Examples/), and Matlab. 
Additionally, I have experience with

- **Cloud Computing** ([AWS EC2/EMR/S3](#aws-ec2emrs3))
- **High Performance Computing** ([Batch Submission](#hpc))
- **Open Source Software Pipelines** ([Bioinformatics](#open-source-tools))
- **Bash Environments** ([Mac/Linux](#bash))


## AWS EC2/EMR/S3

I'm familiar with [creating](https://aws.amazon.com/ec2/instance-types/), [managing](https://aws.amazon.com/ec2/pricing/on-demand/), and [using](https://aws.amazon.com/) AWS cloud computation infrastructurs. 


### Permissions and S3

<details>
<summary>
AWS resources can be accessed via a command line interface.
</summary>

```
pip install --upgrade --user awscli
.local/bin/aws configure
# https://aws.amazon.com
# "My Account" -> "Security Credentials" -> "Access Keys"
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-east-1
Default output format [None]: json
```
</details>

<details>
<summary>
AWS instances require authentication keys.
</summary>

```
# https://aws.amazon.com
"EC2" -> "key Pairs" or "NETWORK & SECURITY" -> "Key Pairs"
mv ~/Downloads/given_pem_name.pem ~/.ssh/
chmod 400 ~/.ssh/given_pem_name.pem
```    
</details>

<details>
<summary>
AWS S3 buckets provide cloud storage for data.
</summary>

- https://aws.amazon.com
- "Console (orange box)" -> "S3" -> "Create"
- "Type of Policy" -> "S3 Bucket Policy"
  - Principal: *
  - Actions: GetObject
  - Amazon Resource Name (ARN): arn:aws:s3:::given_bucket_name/*
</details>


### Managed Server/Worker(s) 

The example below demonstrates deploying  
[web scraper workers and a managing database server](https://www.google.com).


#### Postgres Server
```
~/.local/bin/aws ec2 run-instances --image-id ami-aa2ea6d0 --key-name=given_pem_name
     --instance-type t2.xlarge --count 1 --user-data file://bootstrap_ec2_master.sh
```

<details>
<summary>
bootstrap_ec2_master.sh
</summary>

```
# INSTALL POSTGRESS SERVER
sudo apt-get update
sudo apt-get -y install postgresql-9.5 postgresql-contrib-9.5
sudo sed -e 's/127.0.0.1\/32/0.0.0.0\/0/' /etc/postgresql/9.5/main/pg_hba.conf > tmpy.txt
sudo mv tmpy.txt /etc/postgresql/9.5/main/pg_hba.conf
sudo chown postgres:postgres /etc/postgresql/9.5/main/pg_hba.conf
sudo sed "s/\#listen_addresses = 'localhost'/listen_addresses = '\*'/" /etc/postgresql/9.5/main/postgresql.conf > tmpy.txt
sudo mv tmpy.txt /etc/postgresql/9.5/main/postgresql.conf
sudo chown postgres:postgres /etc/postgresql/9.5/main/postgresql.conf
sudo service postgresql restart
echo "ALTER USER postgres WITH PASSWORD 'postgres';" | sudo -u postgres psql
echo "CREATE DATABASE database_name;" | sudo -u postgres psql

# LOAD STORED DATABASE
wget -S -T 500 -t 50 https://given_bucket_name.s3.amazonaws.com/dbexport.pgsql.gz -O /home/ubuntu/dbexport.pgsql.gz
gunzip -c /home/ubuntu/dbexport.pgsql.gz | sudo -u postgres psql database_name 

# INSTALL ANACONDA
wget -S -T 500 -t 50 https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -O /home/ubuntu/anaconda.sh
sudo bash /home/ubuntu/anaconda.sh -b -p /mnt/anaconda
sudo chown -R ubuntu:ubuntu /mnt
export PATH=/mnt/anaconda/bin:$PATH
echo -e "\n\n# Anaconda2" >> /home/ubuntu/.bashrc
echo "export PATH=/mnt/anaconda/bin:$PATH" >> /home/ubuntu/.bashrc
rm /home/ubuntu/anaconda.sh

# INSTALL RUN TOOLS
pip install psycopg2
ipython -c "import nltk; nltk.download('stopwords', download_dir='/home/ubuntu/nltk_data'); 
	   	   	 nltk.download('punkt', download_dir='/home/ubuntu/nltk_data'); 
			 nltk.download('averaged_perceptron_tagger', download_dir='/home/ubuntu/nltk_data'); 
			 nltk.download('maxent_treebank_pos_tagger', download_dir='/home/ubuntu/nltk_data')"
wget -S -T 500 -t 50 https://given_bucket_name.s3.amazonaws.com/psql_server.py -O /home/ubuntu/psql_server.py
```

The [functionality of the postgres server](https://www.google.com) is given in `psql_server.py`
</details>


#### Webscraper Worker

```
~/.local/bin/aws ec2 run-instances --image-id ami-aa2ea6d0 --key-name=given_pem_name
     --instance-type t2.small --count 1 --user-data file://bootstrap_ec2_worker.sh
```

<details>
<summary>
bootstrap_ec2_worker.sh
</summary>

```
# INSTALL HEADLESS BROWSER
sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev libfreetype6-dev libfreetype6 libfontconfig1-dev libfontconfig1 -y
sudo wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 -C /usr/local/share/
sudo ln -s /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/local/bin/

# INSTALL ANACONDA
wget -S -T 500 -t 50 https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -O /home/ubuntu/anaconda.sh
sudo bash /home/ubuntu/anaconda.sh -b -p /mnt/anaconda
#$HOME/anaconda
sudo chown -R ubuntu:ubuntu /mnt
export PATH=/mnt/anaconda/bin:$PATH
echo -e "\n\n# Anaconda2" >> /home/ubuntu/.bashrc
echo "export PATH=/mnt/anaconda/bin:$PATH" >> /home/ubuntu/.bashrc
rm /home/ubuntu/anaconda.sh

# INSTALL RUN TOOLS
pip install psycopg2
pip install selenium
wget -S -T 500 -t 50 https://given_bucket_name.s3.amazonaws.com/psql_worker.py -O /home/ubuntu/psql_worker.py
```

The [functionality of the webscraper worker](https://www.google.com) is given in `psql_worker.py`
</details>



#### SparkML on EMR




To practice on a local spark installation (in a mac environment)
```
brew install hadoop
brew cask install java8
brew install apache-spark
pip install py4j
import pyspark
```
with the following system variable
```
export SPARK_HOME=`brew info apache-spark | grep /usr | tail -n 1 | cut -f 1 -d " "`/libexec
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export HADOOP_HOME=`brew info hadoop | grep /usr | head -n 1 | cut -f 1 -d " "`/libexec
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native/:$LD_LIBRARY_PATH
source ~/.bash_profile

```



- 
- 
- 




```
~/.local/bin/aws ec2 run-instances \
                 --image-id ami-aa2ea6d0 \
                 --count 1 \
    --instance-type t2.xlarge \
    --key-name=try3 \
    --user-data file://bootstrap_ec2_master.sh
    
```






## HPC

I've developed, managed, and run bioinformatics pipelines for NGS data both on 

- dedicated local 32GB/80TB linux servers
- HPC batch submission environments

| [TACC](https://www.tacc.utexas.edu) (slurm) | [TAMU HPCR](https://hprc.tamu.edu) (LSF) |
:---------------------------------------------|:-----------------------------------------|
| Queue/Node Type                             | Core Memory				 |
| Node Count   	 			      | Node Count				 |
| Job Count   	 			      | Core Count				 |
| Time Limit   	 			      | Wall Time				 |


## Open Source Tools

Bioinformatics data pipelining tasks included

| Task                                | Tool                   | Key Data  |
|:------------------------------------|-----------------------:|:----------|
| Multi-Barcode Demultiplexing        | Illumina/fastX         | .csv      |
| Read Adapter/Quality Trimming       | fastX/cutadapt         | .fastq    |
| Quality Assessment and Delivery     | fastQC/ftp             | .tar      |
| Genome Alignments                   | bwa/bowtie/IGV         | .sam      |
| Genome Visualizations               | IGV                    | .genome   |
| SNP Calling (GWAS, MapPop, BulkSeg) | SAMtools/GATK          | .vcf      |
| Counting (RAD, TAG, RNA, TSS, ASE)  | HTseq/TopHat           | .gff      |


## Bash

Specific Bash environment tools I'm familiar with include

| Task        | Tool                    |
|:------------|------------------------:|
| edit        | emacs, vi               |
| transfer    | scp, wget, curl, ssh    |
| access      | chown, chmod            |
| script      | $var, if, for, ', `, "  |
| manipulate  | awk, sed, tr            |
| pipe        | \|, >>, >               |
| search      | grep, find              |
| display     | wc, cat, head           |
| compress    | tar, gz, bzip           |
| navigate    | ls, pwd, cd, mkdir, rm  |
| monitor     | top, kill, md5, du, df  |
