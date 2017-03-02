Carrotland
=============================================

I've included the constraints and problem description, as well as test cases and solutions.

Note that solution7.py is the final solution submitted.

solution6 is also correct but solution7 is more polished.

The only difference between solution4 and solution5 is solution5 switches to python2.7 instead of python3.4.

(I develop in python3.x locally but code on google foobar runs in a python2.7.6 sandbox.  solution4.py will give the correct answers running as python3.x.)

solution5 yields wrong answers because the switch to python2.7 means '/' is integer division.  solution6 fixes this with:

```python
from __future__ import division
```

which must be the first import statement.



Test Cases
-------------------
I found these values by trial and error.  You can test to see if a certain value will solve the test case by returning that value for all test cases.  Then return that value only if it matches the expected input.

At the present time these values should represent the correct input and output test cases for this problem.  It's possible they may be changed with no warning in the future.  For test cases 3 and 5, it's not possible to determine what the exact input is - only that the output should be zero.

For test cases 1, 2, and 4 the input test case could be verified because the input for the test case is an example in the problem description.

The alt_test_cases are test cases I tested against while solving.  They could be helpful to test against.



Solving the Problem
-------------------
FYI the key to solving this problem is [Pick's Theorem](https://en.wikipedia.org/wiki/Pick%27s_theorem "Pick's Theorem").

First, you should observe that this problem probably relies on some mathematical property.  i.e., if you know this property, you can easily solve this problem.  You know this from the time constraints on the problem - maximum value for a coordinate is 10^9 - if you try to scan all possible points to check if they're interior to the triangle you won't meet time constraints.  Also, you can observe that the area of the triangle bounds the maximum value of possible points interior to the triangle - because each point must be located at integer coordinates each point has a maximum of 1 unit area associated with it.  Search for a way to calculate the area of a triangle from the vertices of the triangle.

Generally you'll find that the area you calculate for the test cases is greater than but very close to the correct value.  It should also be obvious that points on the edges (with integer coordinates) are also involved, subtracted in some way from the area.  You can see what I tried (just guessing) in solutions 1-3 before I found Pick's Theorem.

Try searches describing the problem:

`"count points in a triangle with constraint that no points lie on the perimeter"`

`"count points interior to a triangle"`


Eventually you'll find your way to Pick's Theorem.


You may find these links useful:

http://www.mathopenref.com/coordtrianglearea.html

http://www.had2know.com/academics/triangle-area-perimeter-angle-3-coordinates.html

https://stackoverflow.com/questions/1049409/how-many-integer-points-within-the-three-points-forming-a-triangle

http://jwilson.coe.uga.edu/EMAT6680Fa05/Schultz/6690/Pick/Pick_Main.htm

https://www.cs.umd.edu/~mount/754/Lects/754lects.pdf

http://ftp.ams.stonybrook.edu/geometry/knap.ps.gz

https://en.wikipedia.org/wiki/Pick%27s_theorem



Repository Contents
-------------------
* **/solutions 1 - 7** - Attempted solutions to carrotland.
* **/solution7.py** - Final solution for carrotland.
* **/constraints.txt** - Problem Constraints.
* **/readme.txt** - Problem Description.
* **/test_cases** - Test Cases used on google foobar for Carrotland.
* **/alt_test_cases** - Additional test cases I made to test against.



License Information
-------------------

All code is released under [GNU GPLv3.0](http://www.gnu.org/copyleft/gpl.html).

If you find any errors please message about them.
