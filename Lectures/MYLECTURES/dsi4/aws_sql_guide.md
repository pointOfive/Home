### How to install SQL server on AWS EC2 instance.

#### To launch an EC2 instance -

1. Go to -
* Amazon AWS EC2 console - https://console.aws.amazon.com/ec2/
* Select 'launch instance'
* Choose an Amazon Machine Image (Ubuntu, linux, Red Hat, etc.)
* Choose Instance type (micro, small, medium, large, etc.) for your project
* Important: Under 'Step 4' of configuration, add storage to your instance. The default of 8 GiB is not enough and it's a headache to expand in the future. Choose appropriate size for your project; e.g. 100 GB
* Click 'Review and Launch'
* Get the ip address from AWS console.
* ssh -i filename.pem ubuntu@ip_address_EC2

#### To install PostgreSQL, go to command line. These instructions are for Ubuntu -

* sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" >> /etc/apt/sources.list.d/pgdg.list'
* wget -q https://www.postgresql.org/media/keys/ACCC4CF8.asc -O - | sudo apt-key add -

(Output - OK)
* sudo apt-get update
* sudo apt-get install postgresql postgresql-contrib

3. To test PostgreSQL -
* sudo su - postgres
* psql (this takes inside psql command line)
* \conninfo

(Output - You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".)
* \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)

* \q

(to quit)

* exit
(from postgres user)

#### To install MS-SQL server on Amazon EC2 ubuntu -

* sudo apt-get update
* sudo apt-get install -y mysql-server
(the command line prompts for setting password, twice)
* sudo mysql_secure_installation
* sudo apt-get update

5. Testing MSSQL -
* systemctl status mysql.service

● mysql.service - MySQL Community Server
   Loaded: loaded (/lib/systemd/system/mysql.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2017-05-29 20:13:00 UTC; 2min 50s ago
 Main PID: 7034 (mysqld)
   CGroup: /system.slice/mysql.service
           └─7034 /usr/sbin/mysqld

May 29 20:12:59 ip-172-31-8-143 systemd[1]: Starting MySQL Community Server...
May 29 20:13:00 ip-172-31-8-143 systemd[1]: Started MySQL Community Server.

#### To install MongoDB on Amazon Linux

1. ssh into your EC2 instance (ssh -i path_to_pem_key ec2-user@IP_address)

2. Create a /etc/yum.repos.d/mongodb-org-3.0.repo file so that you can install MongoDB directly, using yum:
  * $ sudo nano /etc/yum.repos.d/mongodb-org-3.0.repo
  * copy this into the file:

    [mongodb-org-3.0]

    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/amazon/2013.03/mongodb-org/3.0/x86_64/

    gpgcheck=0

    enabled=1
3. Install the MongoDB packages and associated tools:
  * $ sudo yum install -y mongodb-org
4. Start MongoDB:
  * $ sudo service mongod start
5. To access your MongoDB in the future:
  * $ mongo
