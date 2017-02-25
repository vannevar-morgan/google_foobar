package com.google.challenges; 
import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;


public class Answer {

    private static Map<BigInteger, BigInteger> fib_map = new HashMap<BigInteger, BigInteger>();
    private static BigInteger BigInt_TWO = new BigInteger("2");

    public static void main(String[] args)
    {
	/*
	 * For testing the Answer class.
	 */
	Answer a = new Answer();
	System.out.println(a.answer(args[0]));
    }
    
    public static String answer(String str_S) { 
	/*
	 * Takes the base-10 string representation of an integer S; returns the largest n such that R(n) = S.
	 *
	 * Input:
	 *     str_S - base-10 string representation of an integer
	 *
	 * Output:
	 *     A String representing the largest n such that R(n) = S.
	 *     If S does not exist in R(n) then the string "None" is returned.
	 *
	 * Note:
	 *     S will be no greater than 10^25
	 *
	 */
	
	BigInteger s = new BigInteger(str_S);
	return find_n(s);
    }

    public static String find_n(BigInteger s){
	/*
	 * Return (as a Str) the greatest index, n, such that R(n) = s
	 * 
	 * If no R(n) = s then "None" is returned. 
	 */
	if(s == BigInteger.ONE){
	    return "1";
	}
	if(s == BigInt_TWO){
	    return "2";
	}
	
	fib_map.put(BigInteger.ZERO, BigInteger.ONE);
	fib_map.put(BigInteger.ONE, BigInteger.ONE);
	fib_map.put(BigInt_TWO, BigInt_TWO);

	// search the odd range, then search the even range, return the greater index, or None
	BigInteger even_n = bin_search(s, BigInteger.valueOf(4));
	BigInteger odd_n = bin_search(s, BigInteger.valueOf(3));

	if(even_n.compareTo(BigInteger.valueOf(-1)) == 0 && odd_n.compareTo(BigInteger.valueOf(-1)) == 0){
	    return "None";
	}else if(odd_n.compareTo(BigInteger.valueOf(-1)) == 0){
	    return even_n.toString();
	}else{
	    return odd_n.toString();
	}

    }

    public static BigInteger bin_search(BigInteger s, BigInteger n_beg){
	/*
	 * Perform binary search starting at index n_beg, to find R(n) == s
	 *
	 * Input:
	 *     s     -  value to search for in the sequence.
	 *     n_beg -  index, n, to begin searching in the sequence R(n).
	 *
	 * Output:
	 *     The last index, n, in the sequence R(n) which yields the value s.
	 *     If the value s does not exist in the sequence, R(n), then -1 is returned.
	 *
	 * Note:
	 *     The odd and even sequences must be searched separately.  Treated separately, 
	 *     both sequences are monotonically increasing.
	 */
	BigInteger offset = BigInteger.ZERO; // offset for even
	if(n_beg.mod(BigInt_TWO).compareTo(BigInteger.ZERO) != 0){
	    offset = BigInteger.ONE; // offset for odd
	}
	
	// find the upper bound for n
	BigInteger n_end = n_beg; // upper bound for n
	build_fib_map(n_end);
	
	while(fib_map.get(n_end).compareTo(s) == -1){
	    n_end = n_end.multiply(BigInt_TWO).subtract(offset);
	    build_fib_map(n_end);
	}
	
	if(fib_map.get(n_end).compareTo(s) == 0){
	    return n_end;
	}
	
	// find the lower bound for n
	n_beg = n_beg.max((n_end.add(offset)).divide(BigInt_TWO)); // lower bound for n
	build_fib_map(n_beg);
	
	// binary search to find n for R(n) == s
	while(n_beg != n_end){
	    if(n_beg.add(BigInt_TWO).compareTo(n_end) == 0){
		build_fib_map(n_beg);
		build_fib_map(n_end);
		break;
	    }
	    BigInteger n_mid = n_beg.add((n_end.subtract(n_beg)).divide(BigInt_TWO));
	    build_fib_map(n_mid);
	    
	    if(fib_map.get(n_mid).compareTo(s) == -1){
		n_beg = n_mid;
	    }else if(fib_map.get(n_mid).compareTo(s) == 1){
		n_end = n_mid;
	    }else{
		n_beg = n_mid;
		n_end = n_mid;
		break;
	    }
	}
	
	if(fib_map.get(n_end).compareTo(s) == 0){
	    return n_end;
	}
	if(fib_map.get(n_beg).compareTo(s) == 0){
	    return n_beg;
	}
        return BigInteger.valueOf(-1);
    }

    public static BigInteger build_fib_map(BigInteger n){
	/*
	 * Calculate the n-th value of the sequence and add to the fib_map.
	 */
	if(fib_map.containsKey(n)){
	    return fib_map.get(n);
	}else{
	    if(n.mod(BigInt_TWO) == BigInteger.ZERO){
		// even sequence
		BigInteger half_n = n.divide(BigInt_TWO);
		BigInteger temp_val = build_fib_map(half_n).add(build_fib_map(half_n.add(BigInteger.ONE))).add(half_n);
		fib_map.put(n, temp_val);
		return temp_val;
	    }else{
		// odd sequence
		BigInteger half_n = (n.subtract(BigInteger.ONE)).divide(BigInt_TWO);
		BigInteger temp_val = build_fib_map(half_n).add(build_fib_map(half_n.subtract(BigInteger.ONE))).add(BigInteger.ONE);
		fib_map.put(n, temp_val);
		return temp_val;
	    }
	}
    }


}
