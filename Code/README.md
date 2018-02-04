# Coding

I work fluently in data analysis using either [R](#r) or [Python](#python),
work comfortably in [SQL](#sql) and [bash](https://github.com/pointOfive/Home/tree/master/Compute#open-source-tools) environments,
and am capable with core [C++](#sql) functionality.

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

## Spark

## SQL

I have experience using SQL in `postgreSQL`, `psycopg2`, and `sparkSQL` contexts.
Some example queries are available in the [SQL subdirectory](https://github.com/pointOfive/Examples/Code/SQL).

## C++

To practice my coding ability I have begun working through the problems from 
[Cracking the Coding Interview](https://technicalyorker.files.wordpress.com/2016/02/cracking-the-coding-interview1.pdf).

### Strings and Lists
0. String buffer class [stringBuffer.h](Cpp/stringBuffer.h) and [stringBuffer.h](Cpp/stringBuffer.cpp)
1. In place [string reversal](Cpp/reverseString.cpp) functionality





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
