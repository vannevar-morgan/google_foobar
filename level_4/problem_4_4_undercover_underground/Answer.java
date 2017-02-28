//package com.google.challenges;

import java.math.BigInteger;
import java.util.Map;
import java.util.HashMap;
import java.util.Objects;
import java.lang.Math;


public class Answer {

    public class Pair<T1, T2>{
	private final T1 first;
	private final T2 second;
	
	public Pair(T1 p1, T2 p2){
	    this.first = p1;
	    this.second = p2;
	}
	
	public boolean equals(Object o){
	    if(!(o instanceof Pair)){
		return false;
	    }
	    Pair<?, ?> p = (Pair<?, ?>) o;
	    return Objects.equals(p.first(), this.first) && Objects.equals(p.second(), this.second);
	}
	
	public int hashCode() {
	    int hashFirst = this.first != null ? this.first.hashCode() : 0;
	    int hashSecond = this.second != null ? this.second.hashCode() : 0;
	    
	    return (hashFirst + hashSecond) * hashSecond + hashFirst;
	}
	
	public T1 first(){
	    return this.first;
	}
	
	public T2 second(){
	    return this.second;
	}
    }
    
    private static Map<Pair<Integer, Integer>, BigInteger> memo_bin_coeff = new HashMap<Pair<Integer, Integer>, BigInteger>();
    private static Map<Pair<Integer, Integer>, BigInteger> memo_res = new HashMap<Pair<Integer, Integer>, BigInteger>();



    public static void main(String[] args){
	/*
	 * For testing the Answer class.
	 */
	int n = 2;
	int k = 1;
	n = Integer.parseInt(args[0]);
	k = Integer.parseInt(args[1]);
	Answer a = new Answer();
	System.out.println(a.answer(n, k));	
    }
    
    public String answer(int n, int k) {
	/*
	 *
	 */
	return calc_ans(n, k).toString();

    }

    public BigInteger calc_ans(int n, int k){
	/*
	 *
	 */
	Pair<Integer, Integer> nk_pair = new Pair<Integer, Integer>(n, k);
	if(memo_res.containsKey(nk_pair)){
	    return memo_res.get(nk_pair);
	}

	if(k < n - 1 || k > n * (n - 1) / 2){
	    memo_res.put(nk_pair, BigInteger.ZERO);
	    return BigInteger.ZERO;
	}
	
	if(k == n - 1){
	    BigInteger temp = BigInteger.valueOf((int) Math.pow(n, n - 2));
	    // System.out.println("k = n - 1\t" + temp.toString());
	    memo_res.put(nk_pair, temp);
	    return temp;
	}
	
	BigInteger res = calc_bin_coeff(n * (n - 1) / 2, k);
	// System.out.println("n: " + Integer.toString(n) + "\tk: " + Integer.toString(k));
	// System.out.println("res\t" + res.toString());
	BigInteger res2;
	for(int m = 0; m < n - 1; ++m){
	    res2 = BigInteger.ZERO;
	    int p = Math.max(0, (k - (m + 1) * m / 2) );
	    for(; p < k - m + 1; ++p){
		res2.add(calc_bin_coeff( (n - 1 - m) * (n - 2 - m) / 2, p).multiply(calc_ans(m + 1, k - p)));
	    }
	    res.subtract(calc_bin_coeff(n - 1, m).multiply(res2));
	}
	memo_res.put(nk_pair, res);
	return res;
    }

    public BigInteger calc_bin_coeff(int n, int k){
	/*
	 * Return the binomial coefficient for n, choose k.
	 */
	Pair<Integer, Integer> nk_pair = new Pair<Integer, Integer>(n, k);	
	if(memo_bin_coeff.containsKey(nk_pair)){
	    return memo_bin_coeff.get(nk_pair);
	}
	
	if(n - k < 0){
	    memo_bin_coeff.put(nk_pair, BigInteger.ZERO);
	    return BigInteger.ZERO;
	}
	
	BigInteger temp = calc_factorial(n).divide(calc_factorial(k).multiply(calc_factorial(n - k)));
	memo_bin_coeff.put(nk_pair, temp);
	return temp;
    }
    
    public static BigInteger calc_factorial(int n){
	/*
	 * Return n factorial.
	 */
	BigInteger temp = BigInteger.ONE;
	if(n <= 0){
	    return temp;
	}
	for(int i = n; i > 0; --i){
	    temp.multiply(BigInteger.valueOf(i));
	}
	return temp;
    }

}


