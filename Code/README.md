# Coding

I work fluently in data analysis using either [R](#r) or [Python](#python),
work comfortably in [SQL](#sql) and [bash](https://github.com/pointOfive/Home/tree/master/Compute#open-source-tools) environments,
and am capable with core [C++](#cpp) functionality.

## R

I have used R for approximately ten years, beginning in college, 
continuing in graduate school (except for a year long period of matlab use)
and during my postdoctoral program, and in my two subsequent work positions. 
As of approximately two years ago I switched over to Python (primarily for access to the scikit-learn library); however,
I use R when the necessary functionality is not available in a Python context.
For example, please see the [R subdirectory](https://github.com/pointOfive/Home/tree/master/Code/R) for an analysis
of job salaries using [Model Based Tree Partitioning](http://party.r-forge.r-project.org), a very interesting
methodology for subgroup analysis that has recently received attention in the context of
[causal inference](http://www.pnas.org/content/113/27/7353.full).

## Python

- Matrix Parsing
- Matrix Rotation
- Connected matrix neighbors
- amazon question


## Spark

## SQL

I have experience using SQL in `postgreSQL`, `psycopg2`, and `sparkSQL` contexts.
Some example queries are available in the [SQL subdirectory](https://github.com/pointOfive/Examples/Code/SQL).

## Cpp

For a refresher and practice problems I have worked through the problems from 
[Cracking the Coding Interview](https://technicalyorker.files.wordpress.com/2016/02/cracking-the-coding-interview1.pdf).

<details>
<summary>
Arrays and Strings
</summary>

0. String Buffer class ([stringBuffer.h](Cpp/stringBuffer.h)/[stringBuffer.cpp](Cpp/stringBuffer.cpp)), with
1. [dynamically expandable appending](Cpp/stringBuffer.cpp)
2. [character uniqueness checking](Cpp/uniqueChars.cpp), and
3. [in place string reversal](Cpp/reverseString.cpp) functionality

Using this data structure I implemented the following capabilities

4. [Permutation Checking](Cpp/perm.cpp)
5. [Character Find/Replace](Cpp/replace.cpp)
6. [Simple Compression](Cpp/compress.cpp)
</details>


<details>
<summary>
Linked Lists
</summary>

0. Linked List Node class ([linkedListNode.h](Cpp/ll.h)/[linkedListNode.cpp](Cpp/ll.cpp)), with auxillary
1. [printing](Cpp/ll.cpp)
2. [duplicating](Cpp/ll.cpp), and
3. [reversing](Cpp/ll.cpp) functionality

Using this data structure I implemented the following capabilities

4. [Dedup unsorted linked list](Cpp/dedup.cpp)
5. [find kth node from end](Cpp/pali.cpp)
7. [Partion around node](Cpp/part.cpp)
8. [Store numbers as linked list](Cpp/add.cpp)
9. [Check if linked list is looped](Cpp/circ.cpp)
10. [Check if linked list is a palindrome](Cpp/pali.cpp)

</details>


<details>
<summary>
Stacks and Queues
</summary>

0. String buffer class [stringBuffer.h](Cpp/stringBuffer.h) and [stringBuffer.h](Cpp/stringBuffer.cpp)
1. In place [string reversal](Cpp/reverseString.cpp) functionality

</details>


<details>
<summary>
Trees and Graphs
</summary>

0. String buffer class [stringBuffer.h](Cpp/stringBuffer.h) and [stringBuffer.h](Cpp/stringBuffer.cpp)
1. In place [string reversal](Cpp/reverseString.cpp) functionality

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
