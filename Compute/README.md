# Computing

I've worked in scientific computing contexts for over 15 years 
using primarily [Python, R, SQL, C++](https://github.com/pointOfive/Examples/), and Matlab. 
Additionally, I have experience with

- **Cloud Computing** ([AWS EC2/EMR/S3](#aws-ec2emrs3))
- **High Performance Computing** ([Batch Submission](#hpc))
- **Open Source Software Pipelines** ([Bioinformatics](#open-source-tools))
- **Bash Environments** ([Mac/Linux](#bash))


## AWS EC2/EMR/S3

I'm familiar with creating, managing, and using AWS cloud computation infrastructurs. 

- [EC2 Instances](https://aws.amazon.com/ec2/instance-types/)
- [EC2 Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)

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


### Server/Worker(s) Paradigm

The example below demonstrates deploying [web scraper workers and a managing database server](https://www.google.com).


#### Postgres Server
```
~/.local/bin/aws ec2 run-instances --image-id ami-aa2ea6d0 --key-name=given_pem_name
     --instance-type t2.xlarge --count 1 --user-data file://bootstrap_ec2_master.sh
ssh -i ~/.ssh/given_pem_name.pem ubuntu@address.compute-1.amazonaws.com
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

Click [here](https://www.google.com) to see the functionality of the postgres server `psql_server.py`
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

Click [here](https://www.google.com) to see the functionality of the webscraper worker `psql_worker.py`
</details>


### EMR Distributed Computing Paradigm

The example below demonstrates a [sparkML+NLP data analysis pipeline](https://www.google.com).

#### Spark


```
number_cores = 3
bash launch_cluster.sh given_bucket_name given_pem_name $number_cores
scp -i ~/.ssh/given_bucket_name.pem file.py hadoop@address.compute-1.amazonaws.com:/home/hadoop
```

<details>
<summary>
launch_cluster.sh
</summary>

```
~/.local/bin/aws emr create-cluster --name PySparkCluster --release-label emr-5.11.0 \
    --applications Name=Spark --ec2-attributes KeyName=$2 --use-default-roles --instance-groups \
      InstanceGroupType=MASTER, InstanceCount=1, InstanceType=m3.xlarge \
      InstanceGroupType=CORE, InstanceCount=$3, InstanceType=m3.xlarge \
    --bootstrap-actions Path=s3://$1/scripts/bootstrap.sh
```

<details>
<summary>
bootstrap.sh
</summary>

```
# INSTALL ANACONDA
sudo yum -y update
sudo yum -y install tmux
wget -S -T 10 -t 5 https://repo.continuum.io/archive/Anaconda2-5.0.1-Linux-x86_64.sh -O $HOME/anaconda.sh
sudo bash $HOME/anaconda.sh -b -p /mnt/anaconda
sudo chown -R hadoop:hadoop /mnt
export PATH=/mnt/anaconda/bin:$PATH
echo -e "\n\n# Anaconda2" >> $HOME/.bashrc
echo "export PATH=/mnt/anaconda/bin:$PATH" >> $HOME/.bashrc
rm $HOME/anaconda.sh

# INSTALL RUN TOOLS
wget https://given_bucket_name.s3.amazonaws.com/scripts/nlp_pipeline.py -O $HOME/nlp_pipeline.py
ipython -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); 
	   	   nltk.download('averaged_perceptron_tagger'); nltk.download('maxent_treebank_pos_tagger')"

```

Click [here](https://www.google.com) to see the sparkML NLP pipeline `nlp_pipeline.py`
</details>
</details>


#### Spark Practice 

<details>
<summary>
To practice on a local spark installation (in a mac environment)
</summary>

```
brew cask install java8
brew install hadoop
brew install apache-spark
pip install py4j
#import pyspark
```
with the following system variable
```
export SPARK_HOME=`brew info apache-spark | grep /usr | tail -n 1 | cut -f 1 -d " "`/libexec
export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
export HADOOP_HOME=`brew info hadoop | grep /usr | head -n 1 | cut -f 1 -d " "`/libexec
export LD_LIBRARY_PATH=$HADOOP_HOME/lib/native/:$LD_LIBRARY_PATH
source ~/.bash_profile
```
</details>


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
| Multi-Barcode Demultiplexing        | [Illumina](https://support.illumina.com/content/dam/illumina-support/documents/documentation/software_documentation/bcl2fastq/bcl2fastq_letterbooklet_15038058brpmi.pdf)/[fastX](http://hannonlab.cshl.edu/fastx_toolkit/) | .csv      |
| Read Adapter/Quality Trimming       | [fastX](http://hannonlab.cshl.edu/fastx_toolkit/)/[cutadapt](https://cutadapt.readthedocs.io/en/stable/)         | .fastq    |
| Quality Assessment and Delivery     | [fastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/)/[ftp](http://cs.baylor.edu/~donahoo/classes/tutorials/ftp/ftp.html)             | .tar      |
| Genome Alignments                   | [bwa](http://bio-bwa.sourceforge.net/)/[bowtie](http://bowtie-bio.sourceforge.net/index.shtml)      | .sam      |
| Genome Visualizations               | [IGV](http://software.broadinstitute.org/software/igv/)                    | .genome   |
| SNP Calling (GWAS, MapPop, BulkSeg) | [SAMtools](http://www.htslib.org/)/[GATK](https://software.broadinstitute.org/gatk/)          | .vcf      |
| Counting (RAD, TAG, RNA, TSS, ASE)  | [HTseq](https://htseq.readthedocs.io/en/release_0.9.1/)/[TopHat](https://ccb.jhu.edu/software/tophat/index.shtml)           | .gff      |


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
