Zombit Pandemic
=============================================

I've included the constraints and problem description.

Note that solution.py is the final solution submitted.

solution2.py is a hardcoded, constant time solution (Hardcoded solutions are sometimes GOOD solutions!).  Originally I was failing time constraints because I neglected to memoize the binomial coefficient computation.  I tried hardcoding the solutions, which is possible because we know n is in the range [2, 50].  When I tested solution2.py on foobar it failed two of the test cases despite that it matches output from solution.py.  It's possible I tested it before I fixed the output for n = 2 and n = 3 (should be "2/1" and "3/1" respectively - but was possibly coded instead as "2" and "3" which is the wrong output format per the problem description).  But I don't remember which version I tested with.


Solving the Problem
-------------------
Expected outcome is expressed as the sum of the product of outcome and probability of outcome, for all possible outcomes.
```
p_e = sum(v_i * p_i), for all outcomes
v_i = value of a possible outcome
p_i = probability of v_i
```

So we can break the problem into three subproblems:
- Problem 1: Given a value n [2 - 50], return the unique set of possible partitions.

  (For example, following the rules of the problem the minimum warren size is 2.  So for n = 4, partitions = [[4], [2, 2]])
- Problem 2: Count the number of ways of creating each possible partition.
- Problem 3: Count the total number of ways of creating ALL possible partitions.

**NOTE:**

Problem 3 is simply the sum of the sums from solving Problem 2.  If Problem 2 is solved, so is Problem 3.

It should be clear (from previous problems, time constraints, and "count the number of ways...") that some combinatorics will be involved.

Problem 1 is straightforward.

Problem 2 is the most difficult.
***

In order to count the number of ways to create each partition (for a given size, n), observe that each rabbit warren represented as a graph can have at most 1 cycle.  This is because each rabbit bumps exactly 1 rabbit other than itself.  This means if a cycle forms in a warren, the only way a rabbit can join that warren is by bumping one of the rabbits in the cycle (and so it cannot form a cycle with another rabbit, nor can it bump more than one rabbit to join multiple cycles).  Undirected graphs with at most one cycle are known as pseudoforests.

Reading about pseudoforests is very helpful.

https://en.wikipedia.org/wiki/Pseudoforest

In particular:

https://en.wikipedia.org/wiki/Pseudoforest#Enumeration

**NOTE:**
> "A graph is simple if it has no self-loops and no multiple edges with the same endpoints."

does not hold true for rabbit warrens because we can have multiple edges with the same endpoints, such as:
```
A->B
B->A
```

> "If self-loops are not allowed, the number of maximal directed pseudoforests is instead `(n-1)^n`."

This gives us the total number of ways to create all possible partitions - AKA, Problem 3.
***

Searching for "count number of pseudoforests" I found:

https://math.stackexchange.com/questions/1090498/how-to-calculate-the-expected-maximum-tree-size-in-a-pseudoforest

It's rtheunissen.  I've found his questions before in solving foobar problems.  He's pretty good.  The explanation given by Jacopo Notarstefano is helpful and outlines an algorithm that solves Problem 2.

It links to a second article:

https://math.stackexchange.com/questions/1071564/how-many-good-graphs-of-size-n-are-there

which points to OEIS A000435.

https://oeis.org/A000435

Calculating A000435 directly may lead to rounding errors, from the formulas available it was simpler to calculate as A001864(n) / n

https://oeis.org/A001864

After implementing the algorithm outlined by Jacopo Notarstefano, the only other problems I had were:
- meeting time constraints.  I forgot to memoize the calculation of the binomial coefficient - a quick fix.
- for values n = 2 and n = 3 the answer will reduce to "2" and "3" respectively.  They need to be in the format "num/den".  I hardcoded it - also a quick fix.


***
You may find these links useful:

https://en.wikipedia.org/wiki/Partition_(number_theory)

https://en.wikipedia.org/wiki/Pseudoforest

https://en.wikipedia.org/wiki/Pseudoforest#Enumeration

https://math.stackexchange.com/questions/1090498/how-to-calculate-the-expected-maximum-tree-size-in-a-pseudoforest

https://math.stackexchange.com/questions/1071564/how-many-good-graphs-of-size-n-are-there

https://oeis.org/A000435

https://oeis.org/A001864

https://en.wikipedia.org/wiki/Binomial_coefficient

https://en.wikipedia.org/wiki/Falling_and_rising_factorials

https://math.stackexchange.com/questions/202554/how-do-i-compute-binomial-coefficients-efficiently

https://stackoverflow.com/questions/18503096/python-integer-partitioning-with-given-k-partitions

**I also suggest checking out the last link and rtheunissen's solution.  The last link details a generating function for generating the partitions which is better than my dp approach.  rtheunissen also used a generating function.**




Repository Contents
-------------------
* **/solution2.py** - Hardcoded and possibly wrong solution to zombit_pandemic.
* **/solution.py** - Final solution for zombit_pandemic.
* **/problem_files** - Initial problem files.
* **/problem_files/constraints.txt** - Problem Constraints.
* **/problem_files/readme.txt** - Problem Description.



License Information
-------------------

All code is released under [GNU GPLv3.0](http://www.gnu.org/copyleft/gpl.html).

If you find any errors please message about them.
