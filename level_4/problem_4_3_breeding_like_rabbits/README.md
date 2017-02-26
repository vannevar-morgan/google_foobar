Breeding Like Rabbits
=============================================

I've included the constraints and problem description, as well as wrong solutions.

Note that Answer.java is the final solution submitted.

solution.py, solution2.py, and solution3.py are incorrect.
solution4.py to my knowledge is also correct but is too slow.

solution3 is incorrect due to errors with floating point precision.  In the while loop for the binary search, when `n_mid` is calculated (halving the range on each iteration) eventually the half-range `(n_end - n_beg) / 2` is significantly smaller than `n_beg` (i.e., n_beg may be on the order of 10^25, while the half_range is 64).  This is a common issue with floating point math.  When adding the values, there isn't enough precision to add the small float to the large float so the value calculated for `n_mid = n_beg + (n_end - n_beg) / 2` becomes simply `n_beg`.  This causes the exit conditions for the loop to never occur and we have an infinite loop.  solution4 solves this by using the Decimal module, but it's still too slow for large str_S input.  I'm not sure why it's slow - maybe I'm doing something wrong but I've experienced issues related to precision with the Decimal module in python2.7 in the past (specifically, problem_4_1_line_up_the_captives).  Testing with python3.4 it's still slow - so it may or may not be an implementation issue.  Note I also tried evaluating only the even sequence - I think (but haven't proven to myself) the even sequence should be >= the odd sequence.  So if the value exists in the even sequence it should be the greatest instance of the value for both sequences.  If so then you don't need to check the odd sequence if the value exists in the even sequence.  Note this doesn't solve the speed issue because you still need to check both sequences if the value doesn't exist in the even sequence.

I found it simpler to solve the speed problem by reimplementing in java so I could use BigInteger.  The java implementation passes all test cases and is the final solution submitted.


Solving the Problem
-------------------
Note the name of the problem "breeding_like_rabbits" should hint at the fibonacci series.

My initial idea to solve this problem was, basically, as I solved it in the end.  Calculate the n-th value and make use of a hash table to store previously calculated values.  Do a binary search, calculating values as needed, to find the index corresponding to the value searched for (or "None" if the value doesn't exist).

It might be a little tricky to calculate the n-th value correctly.  For my first implementation solution.py (although I meant to calculate the n-th value from the top down using the dictionary) the sequence definition confused me because it's defined in a way that the n-th value depends on advance values.

```
    R(2n) = R(n) + R(n + 1) + n (for n >  1)
R(2n + 1) = R(n) + R(n - 1) + 1 (for n >= 1)
```

I was expecting to look up previous values from the dictionary but I can't look up values that haven't been calculated yet.  (the fix is to treat 2n as i, n as i / 2, for the i-th index in R(i), then call these values recursively - oops I must've been asleep).  What I ended up doing was calculating from the bottom up - filling the dictionary with values for each n.  Because str_S can be a value up to 10^25 we'd need to store ~ 1.67 * 10^24 values in the dictionary - obviously wrong!  solution.py is still useful for calculating the n-th value for small n.  Not useful for much else.

My next idea was to try to find a closed form solution to the recurrence relation.  With the fibonacci sequence for example, a number, x, is a fibonacci number iff `5x^2 + 4` or `5x^2 - 4` is a square number.  This property of the fibonacci sequence arises from the closed form of the fibonacci recurrence relation.  If you can find a closed form, usually you can determine if a number is a member of the sequence and where in the sequence the number is located.  Read through some of the following for a better understanding:

https://www.tutorialspoint.com/discrete_mathematics/discrete_mathematics_recurrence_relation.htm

https://www.stat.auckland.ac.nz/~fewster/325/notes/ch4.pdf

https://math.stackexchange.com/questions/255505/what-is-generally-the-strategy-for-converting-recurrence-to-closed-form

ftp://ftp.cis.upenn.edu/pub/wilf/index.html.old

https://www.math.upenn.edu/~wilf/DownldGF.html

https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-042j-mathematics-for-computer-science-fall-2005/readings/ln11.pdf

http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/LRGF.html

https://en.wikipedia.org/wiki/Fibonacci_number


Ultimately I can't find a generating function for this recurrence relation and so I can't get a closed form solution.  It may or may not be possible.  Eventually I ended up searching for `different recurrence relations when odd` which led to a stackexchange thread:

https://math.stackexchange.com/questions/1060154/help-with-a-recurrence-with-even-and-odd-terms

Clearly it's other people trying to solve the same problem.  This was very helpful because it got me back on track for what I was originally trying to do.  In solution2.py I've reimplemented the `build_fib_map()` function.  Now it's calculating top-down recursively the way I had originally intended.  Being able to calculate the n-th value of the sequence makes the rest of the problem straight forward.  Observe that the even and odd sequences, treated separately, are both monotonically increasing.  This means you can do a binary search on the separate ranges for str_S.  This is pretty straightforward to implement.  The only other real issues were the floating point precision and the speed problem.  As discussed above, I ended up reimplementing in java and using BigInteger.  I'm not sure what's causing the speed problem in python other than possible limitations related to the decimal module.



You may find these links useful:

https://stackoverflow.com/questions/21749904/python-sum-of-big-float-numbers

https://docs.python.org/2/tutorial/floatingpoint.html

https://math.stackexchange.com/questions/1060154/help-with-a-recurrence-with-even-and-odd-terms

https://math.stackexchange.com/questions/1045477/convoluted-recurrence-f2n-fnfn1n-f2n1-fnfn-11




Repository Contents
-------------------
* **/solutions 1 - 4.py** - Attempted solutions to breeding_like_rabbits.
* **/Answer.java** - Final solution for breeding_like_rabbits.
* **/constraints.txt** - Problem Constraints.
* **/readme.txt** - Problem Description.



License Information
-------------------

All code is released under [GNU GPLv3.0](http://www.gnu.org/copyleft/gpl.html).

If you find any errors please message about them.
