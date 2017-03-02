Undercover Underground
=============================================

I've included the constraints and problem description, as well as wrong solutions.

Note that solution.py is the final solution submitted.

Answer.java is incorrect and won't even run on foobar.


Solving the Problem
-------------------
I kinda disliked this problem.  It's pretty tough to attack if you don't have a good mathematical background in combinatorics.

I started this problem by searching for `count graphs for given number of nodes and edges` which led to a stackexchange thread:

https://math.stackexchange.com/questions/689526/how-many-connected-graphs-over-v-vertices-and-e-edges

This is exactly what I need to solve the problem, very in depth - but almost too much.  It kind of spoils the problem.  Ultimately I ended up translating the maple code posted in the stackoverflow thread to python code.  I had a couple problems with speed and division (again, I typically use python3.x but foobar code runs in python2.7.6 - integer / floating point division is backwards between the two).  I passed the first 3 test cases but test cases 4 and 5 failed.  I rewrote it in Java but unfortunately Java doesn't have a built-in Pair / tuple data structure to memoize for (n, k) pairs so I copy-pasted as an inner class a Pair class I wrote for a battleship game.  foobar didn't seem to like the Pair class and gave a general "your code can't be run" message - not enough information to debug with.  Eventually I switched back to python and solved the division and speed problems.



You may find these links useful:

https://math.stackexchange.com/questions/689526/how-many-connected-graphs-over-v-vertices-and-e-edges

https://en.wikipedia.org/wiki/Binomial_coefficient

https://en.wikipedia.org/wiki/Analytic_combinatorics



Repository Contents
-------------------
* **/Answer.java** - Attempted solution to undercover_underground.
* **/solution.py** - Final solution for undercover_underground.
* **/constraints.txt** - Problem Constraints.
* **/readme.txt** - Problem Description.



License Information
-------------------

All code is released under [GNU GPLv3.0](http://www.gnu.org/copyleft/gpl.html).

If you find any errors please message about them.
