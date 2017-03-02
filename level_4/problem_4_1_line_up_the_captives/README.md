Line Up The Captives
=============================================

Note that Answer.java is the final solution submitted.

captives.py gives the correct answer running in python3.x, but is incorrect running in python2.7.6 (which is what code runs in on foobar).  The problem is due to differences in precision related to the decimal module.  I should have just used long.  long has unlimited precision, decimal should be used for floating points when more precision is needed than is possible with float.  Using decimal makes it slower and causes the precision problems.  Don't use decimal when you solve it.

I switched to java so I could use BigInteger.  Generally when dealing with problems involving precision I've preferred using java to make use of BigInteger.



definitely_wrong_examples
-------------------
These are solutions I tried initially as I developed towards the final solution.  I've kept them to illustrate the different approaches I tried.



examples
-------------------
These are solutions I found online.  I used these as a sanity check before realizing foobar was running code in a different version of python than I was running code in.  It's possible some of these solutions are wrong.  Sorry, I don't remember where I found them - if you're the author, please message me and I can credit you, or remove them if you prefer.



Solving the Problem
-------------------
You should make two observations:

1. You can solve a simpler subproblem by fixing the tallest rabbit to one side (say, to the left side).  If you can solve this, then the solution to the general problem (with the tallest rabbit at any location) is a multiple of this solution.
2. Due to time constraints, there's likely a mathematical property that can assist in solving this problem.

FYI the key to solving this problem is [Stirling Numbers of the first kind](https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind "Stirling Numbers").

I solved this problem by first solving the subproblem with the tallest rabbit fixed to the left side.  With this assumption, I was able to make a derivation for the recurrence relation for Stirling numbers of the first kind.  I don't have a significant background in combinatorics and I hadn't seen Stirling numbers before but they get used a lot for counting permutations in combinatoric problems.  You should be able to see that the general solution is a multiple of the subproblem.

To pass test cases, you also need to have the correct precision.  Use long, it has unlimited precision.  In my case, using decimal was a mistake - there are differences in implementation between python2.7.6 and python3.x.  I failed test cases because of this, and drove myself **nuts** trying to track down bugs not realizing I had the correct answer in python3 and the failed test cases on foobar were because foobar runs python2.7.6.  This is the only foobar problem where I've explicitly sought out other people's solutions as a sanity check - I've posted these in the examples folder.  Eventually I switched to java to make use of BigInteger.  My solution ends up pretty much the same as the others I've seen - the key is to make use of the recurrence relation for Stirling numbers of the first kind.



You may find these links useful:

https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind

https://en.wikipedia.org/wiki/Combinatorics

https://en.wikipedia.org/wiki/Permutation

https://en.wikipedia.org/wiki/Analytic_combinatorics



Repository Contents
-------------------
* **/captives.py** - Correct under python3, incorrect under python2.7.6 (differences in the decimal module)
* **/Answer.java** - Final solution for Carrotland.
* **/definitely_wrong_examples** - Wrong solutions illustrating different approaches tried.
* **/examples** - Solutions by other people - used as a sanity check (please message if you're the author).



License Information
-------------------

All code is released under [GNU GPLv3.0](http://www.gnu.org/copyleft/gpl.html).

If you find any errors please message about them.
