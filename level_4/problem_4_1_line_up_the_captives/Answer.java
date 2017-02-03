//package com.google.challenges; 
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

public class Answer
{

    private static Map<Integer, Map<Integer, BigInteger>> stirling_memo = new HashMap<>();
    private static Map<Integer, BigInteger> factorial_memo = new HashMap<Integer, BigInteger>();
    
    public static void main(String[] args)
    {
	Answer a = new Answer();
	int x = Integer.parseInt(args[0]);
	int y = Integer.parseInt(args[1]);
	int n = Integer.parseInt(args[2]);
	System.out.println(a.answer(x, y, n));
    }

    public static String answer(int x, int y, int n)
    { 
	//
	// Returns the number of possible ways to arrange n rabbits of unique heights
	// along an east to west line, so that only x are visible from the west, and
	// only y are visible from the east.
	//
	// The return value is a string representing the number in base 10.
	// 
	// If there is no possible arrangement, the string "0" is returned.
	//
	// Assumptions:
	//  -The number of rabbits (n) will be as small as 3 or as large as 40
	//  -The viewable rabbits from either side (x and y) will be as small as 1
	//   and as large as the total number of rabbits (n)
	//
	// Inputs:
	// (int) x = number of rabbits visible from the west.
	// (int) y = number of rabbits visible from the east.
	// (int) n = number of rabbits of unique heights.
	// 
	// Outputs:
	// (string) A string representing the number (in base 10) of ways to
	//          arrange the rabbits.
	//
	// e.g.,
	// Inputs:
	// (int) x = 2
	// (int) y = 2
	// (int) n = 3
	//
	// Output:
	// (string) "2"
	//
	// Inputs:
	// (int) x = 1
	// (int) y = 2
	// (int) n = 6
	//
	// Output:
	// (string) "24"
	//
	int n_min = 3;
	int n_max = 40;
	int x_min = 1;
	int y_min = 1;

	// Check constraints on parameters.
	if (n < n_min || n > n_max){
	    return "0";
	}
	if (x < x_min || x > n){
	    return "0";
	}
	if (y < y_min || y > n){
	    return "0";
	}
	
	// If the parameters have no solution, return "0"
	if (x + y > n + 1){
	    return "0";
	}
	
	// Return a string representing the number of permutations.
	return (calc_stirling(n - 1, x + y - 2).multiply(calc_mult(x + y - 2, x - 1))).toString();
    }

    
    public static BigInteger calc_stirling(int n, int k)
    {
	//
	// Returns the Stirling number of the first kind, given n and k.
	// s(n, k)
	//
	// Inputs:
	// (int) n = number of elements
	// (int) k = cycles
	//
	// Outputs:
	// (BigInteger) s = Stirling number of the first kind, s(n, k)
	//
	// The Stirling number of the first kind counts the number of
	// permutations given n elements and k cycles.
	//
        if (stirling_memo.containsKey(n)) {
            Map<Integer, BigInteger> cache_map = stirling_memo.get(n);
            if (cache_map.containsKey(k)) {
                return cache_map.get(k);
            }
        }
	if (n == 0 || k == 0){
	    // add value to stirling_memo
	    if (!stirling_memo.containsKey(n)) {
		stirling_memo.put(n, new HashMap<Integer, BigInteger>());
	    }
	    stirling_memo.get(n).put(k, BigInteger.valueOf(n == k ? 1 : 0));
	    return stirling_memo.get(n).get(k);
	}

	BigInteger stirling = (  BigInteger.valueOf(n - 1).multiply(calc_stirling(n - 1, k))  ).add(  calc_stirling(n - 1, k - 1)  );
	
	// add value to stirling_memo
	if (!stirling_memo.containsKey(n)) {
            stirling_memo.put(n, new HashMap<Integer, BigInteger>());
        }
        stirling_memo.get(n).put(k, stirling);
	
	return stirling;
    }

    public static BigInteger calc_mult(int n, int k)
    {
	//
	// Calculates the multiplicity of elements.
	// Combinations of elements shared between the left and right sides.
	//
	return calc_factorial(n).divide( (calc_factorial(k).multiply(calc_factorial(n - k))) );
    }

    public static BigInteger calc_factorial(int n)
    {
	//
	// Calculates factorials for BigIntegers.
	//
	// Input:
	// (int) n = integer to calculate factorial of
	//
	// Output:
	// (BigInteger) = n!
	//
	if (factorial_memo.containsKey(n)){
	    return factorial_memo.get(n);
	}
	if (n == 0){
	    factorial_memo.put(n, BigInteger.ONE);
	    return BigInteger.ONE;
	}
	if (n == 1){
	    factorial_memo.put(n, BigInteger.ONE);
	    return BigInteger.ONE;
	}
	BigInteger f_val = BigInteger.valueOf(n).multiply(calc_factorial(n - 1));
	factorial_memo.put(n, f_val);
	return f_val;
    }

}
