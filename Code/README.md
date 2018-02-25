# Coding

I work fluently in data analysis using either [R](#r) or [Python](#python),
work comfortably in [SQL](#sql) and [bash](https://github.com/pointOfive/Home/tree/master/Compute#open-source-tools) environments,
and am capable with core [C++](#c) functionality.

## R

I have used R for approximately ten years, beginning in college, 
continuing in graduate school (except for a year long period of matlab use)
and during my postdoctoral program, and in my two subsequent work positions. 
Approximately two years ago I switched over to Python (primarily for access to the scikit-learn library); however,
I use R when the necessary functionality is not available in a Python context.
For example, [this analysis of job salaries](R/mbrp.pdf) uses
[model based tree partitioning](http://party.r-forge.r-project.org) (MBTR)
that is currently only available in R.
MBTP is a very interesting
methodology for subgroup analysis that has recently received attention in the context of
[causal inference](http://www.pnas.org/content/113/27/7353.full).

[![a](R/partition_all.png)](https://github.com/pointOfive/Home/tree/master/Code/R#mbrp)
[![a](R/salary.jpg)](https://github.com/pointOfive/Home/tree/master/Code/R#mbrp)


## Python

Examples of data analysis using Python and supporting tools are available on the [data analysis page](https://github.com/pointOfive/Home/tree/master/Analysis#data-analysis-with-python).

The following are examples of algorithm prototyping and implementation with Python,
and are meant to augment the [C++ coding practice below](#c).  These problems were drawn from the resources 
[here](https://careercup.com/page?pid=amazon-interview-questions&sort=votes), 
[here](https://www.geeksforgeeks.org/amazons-asked-interview-questions/), and
[here](https://technicalyorker.files.wordpress.com/2016/02/cracking-the-coding-interview1.pdf). 

#### Programming Interview Questions
<details>
<summary>
Click here for problems/solutions (9)
</summary>

<br>

- [Fix swapped BST nodes](Python/swapped_bst_nodes.py)
- [In place unsorted counter](Python/tally.py)
- [Pyramid water buckets](Python/pyramid.py) 
- [Maximum increasing product](Python/product.py)
- [Maximum unique substring](Python/substring.py)
- [Matrix rotation](Python/rotate.py)
- [Connected matrix neighbors](Python/graph.py)
- [Matrix parsing](Python/zeroout.py)
- [Find odd appearance items](Python/odd.py)
</details>

#### Stacks and Queues
<details>
<summary>
Click here for problems/solutions (7)
</summary>

<br>

- [Set of stacks](Python/stacksset.py)
- [3 stack array](Python/threestack.py)
- [O(1) min pop stack](Python/threestack.py)
- [Towers of Hanoi](Python/tower.py)
- [Two stack queue class](Python/stackqueue.py)
- [Sort stack with stack](Python/twostacksort.py)
- [Animal shelter](Python/shelter.py)
</details>

## Spark

Instructions for setting up
spark on an AWS cluster or local machine
are given on the [computing page](https://github.com/pointOfive/Home/tree/master/Compute#emr-distributed-computing-paradigm).
A spark NLP and unsupervised learning pipeline is given on the [data analysis page](www.google.com).


## SQL

I have experience using SQL in `postgreSQL`, `psycopg2`, and `sparkSQL` contexts.
Some example queries are given below.


#### Find items sold, not sold, and a subset of items sold within a specific month

```SQL
SELECT c.Name FROM Catelog c JOIN Sales s ON (c.Product_ID = s.Product_ID) 
    GROUP BY c.Name ;

SELECT c.Name FROM Catelog c LEFT JOIN Sales s ON (c.Product_ID = s.Product_ID)
    WHERE s.Date IS NULL
    GROUP c.Name ;

SELECT c.Name, s.Date FROM Catelog c JOIN Sales s ON (c.Product_ID = s.Product_ID)
    WHERE s.Date (BETWEEN to_date("01 11 2015", DD Mon YYYY) AND 
                          to_date("01 11 2015", DD Mon YYYY))
          AND c.Name LIKE "S%" ;
```

#### Selecting largest, second largest, and kth largest `Salary` field value from the `Employee` table

```SQL
SELECT MAX(Salary) FROM Employee ;

SELECT MAX(Salary) FROM Employee WHERE Salary <> (SELECT MAX(Salary) FROM Employee) ;

CREATE TABLE Salary_Most2Least AS 
    (SELECT Salary FROM Employee GROUP BY Salary ORDER BY Salary DESC) ;

SELECT MAX(Salary) from Employee 
    WHERE Salary < (SELECT Salary FROM Salary_Most2Least LIMIT 1 OFFSET n-1) ;
```

#### Select employees, employees of specific managers and managers managing more than `n` employees

```SQL
SELECT Employee_ID FROM EMPLOYEES
    WHERE Employee_ID NOT IN (SELECT DISTINCT Manager_ID FROM Employee) ;

SELECT e1.ID, e2.ID FROM Employee e1 JOIN Employee e2 ON (e1.ID = e2.Manager_ID)
    WHERE e1.ID = xyz ;

CREATE TABLE Number_managed_GTn AS
    (SELECT Manager_ID, COUNT(*) FROM Employee 
    GROUP BY Manager_ID 
    HAVING COUNT(*) > n) ;

CREATE TABLE Managers_Charges AS
    (SELECT e1.ID AS Manager_ID, e2.ID AS Employee_ID 
     FROM Employee e1 JOIN Employee e2 ON (e1.ID = e2.Manager_ID) ) ;    

SELECT Managers_Charges.Employee_ID FROM Managers_Charges JOIN Number_managed_GTn 
    ON (Managers_Charges.Manager_ID = Number_managed_GTn.Manager_ID) ;
 ```


#### Find duplicate records, and get the 5 employees from each department with the highest salaries

```SQL
SELECT name, COUNT(name) AS times FROM contacts GROUP by name, phone HAVING COUNT(name)>1 ;

CREATE DATABASE windowing_practice;
CREATE TABLE Employees (
    Dept_ID VARCHAR(255),
    Employee_ID INTEGER PRIMARY KEY,
    Salary INTEGER
);

INSERT INTO employees (dept_id, employee_id, salary) VALUES ('develop',11,5200); 
INSERT INTO Employees (dept_id, employee_id, salary) VALUES ('develop',7,4200);
...

SELECT e.dept_ID, e.Employee_ID, e.Salary, second.salary FROM Employees e JOIN
    (SELECT dept_id, AVG(salary) AS salary 
        FROM (SELECT dept_ID, employee_ID, salary, rank() 
                  OVER (PARTITION BY Dept_ID ORDER BY Salary DESC) FROM Employees) 
             AS ranks
             WHERE rank = 2
             GROUP BY dept_id) 
     AS second ON (e.dept_ID = second.dept_ID)
     WHERE e.salary >= second.salary;
```
									       



## C++


For practice, and a general algorithm prototyping and implementation refresher, 
I have worked through problems from 
[Cracking the Coding Interview](https://technicalyorker.files.wordpress.com/2016/02/cracking-the-coding-interview1.pdf).

#### Arrays and Strings
<details>
<summary>
Click here for problems/solutions (7)
</summary>

<br>

0. String Buffer class ([stringBuffer.h](Cpp/stringBuffer.h), [stringBuffer.cpp](Cpp/stringBuffer.cpp)), with
1. [dynamically expandable appending](Cpp/stringBuffer.cpp)
2. [character uniqueness checking](uniqueChars.cpp), and
3. [in place string reversal](reverseString.cpp) functionality

Using this data structure I implemented the following capabilities

4. [Permutation Checking](Cpp/perm.cpp)
5. [Character Find/Replace](Cpp/replace.cpp)
6. [Simple Compression](Cpp/compress.cpp)
</details>

#### Linked Lists
<details>
<summary>
Click here for problems/solutions (11)
</summary>

<br>

0. Linked List Node class ([linkedListNode.h](Cpp/ll.h), [linkedListNode.cpp](Cpp/ll.cpp)), with auxiliary
1. [printing](Cpp/ll.cpp)
2. [duplicating](Cpp/ll.cpp)
3. [reversing](Cpp/ll.cpp), and
4. [checking equality](Cpp/ll.cpp) functionality

Using this data structure I implemented the following capabilities

5. [Dedup unsorted linked list](Cpp/dedup.cpp)
6. [Find kth node from end](Cpp/pali.cpp)
7. [Partition around node](Cpp/part.cpp)
8. [Add numbers stored as a linked list](Cpp/add.cpp)
9. [Check if linked list is looped](Cpp/circ.cpp)
10. [Check if linked list is a palindrome](Cpp/pali.cpp)

</details>

#### Trees and Graphs
<details>
<summary>
Click here for problems/solutions (12)
</summary>

<br>

0. Binary Tree class ([tree.h](Cpp/tree.h), [tree.cpp](Cpp/tree.cpp)), with
1. [adding](Cpp/tree.cpp)
2. [display](Cpp/tree.cpp), and
3. [depth calculation](Cpp/balanced.cpp) functionality

Using this data structure I implemented the following capabilities

4. [Check if tree is balanced](Cpp/balanced.cpp)
5. [Check path between two nodes](Cpp/path.cpp)
6. [Create balanced tree from sorted list](Cpp/tree.cpp)
7. [Make linked lists of tree levels](Cpp/tree2ll.cpp)
8. [Check if tree is a BST](Cpp/isbst.cpp)
9. [Find next node in BST](Cpp/next.cpp)
10. [Find first common ancestors](Cpp/ancestors.cpp)
11. [Find paths summing to x](Cpp/sum_path.cpp)

</details>



## git

<details>
<summary>
All materials here managed via git
</summary>

```
git pull https://github.com/pointOfive/Home.git
git checkout -b clone_to_edit
rm README.md
# <oops!>
git checkout -- README.md
# <edit README.md>
git status
git add README.md
git commit -m 'updating a file'
git push origin clone_to_edit
git branch -d clone_to_edit
git fetch origin clone_to_edit
git commit -m 'pull'
git branch
git checkout master
git merge clone_to_edit
git branch -D clone_to_edit
git push origin master
git push origin --delete clone_to_edit
git log
```
</details>
