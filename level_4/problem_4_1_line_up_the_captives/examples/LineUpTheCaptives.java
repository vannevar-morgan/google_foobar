import java.math.BigInteger;
import java.util.HashMap;
import java.util.Map;

/**
 * Solution for line_up_the_captives
 *
 * Thoughts:
 *
 * - Answer is returned as String means we should be using BigInteger
 * for everything here.
 *
 * - This one looks tricky; you can hide rabbits in between the
 * start and the tallest rabbit.
 *
 * - The tallest rabbit presents a special case; that's where you can
 * split the problem into two smaller problems. The tricky part will
 * be how the two problems affect each other - you can always have
 * a rabbit on the West side also be on the East. But it should just
 * be a bit of math to determine how to count that; since all rabbits
 * have different heights we can exchange them freely and the problem
 * remains the same.
 *
 * - If we only worry about how many rabbits are visible from one side,
 * then the problem becomes a lot simpler (I think).
 *
 * - The tallest rabbit has a bound of locations between x and y. For
 * example, if x needs to see 3 rabbits, obviously the tallest rabbit
 * cannot be first in line.
 *
 * - Given N rabbits, you can show from 1 to N rabbits to someone!
 */
public class LineUpTheCaptives {

    static final Factorials sFactorials = new Factorials();

    // Store interstitial results, since a lot of duplicate calculations would
    // have to be repeated otherwise.
    static Map<Integer, Map<Integer, BigInteger>> sStoredResults = new HashMap<>();

    /**
     * @param x the # rabbits visible from one side (1-40)
     * @param y the # rabbits visible from the other side (1-40)
     * @param n the # of rabbits (3-40)
     * @return String representation of the number of solutions (base 10)
     */
    public static String answer(int x, int y, int n) {
        // Iterate the tallest rabbit to split this problem in twain
        //
        // While the setup is almost exactly the same as permutationsForSide(), it's
        // enough different that it's simpler to just keep them separate.
        BigInteger count = BigInteger.ZERO;
        for (int tallestPosition = x - 1; tallestPosition < n - y + 1; tallestPosition++) {
            int numRabbitsX = tallestPosition;
            int numRabbitsY = n - numRabbitsX - 1;

            // Solve problem for each side
            BigInteger xPermutations = permutationsForSide(x - 1, numRabbitsX);
            BigInteger yPermutations = permutationsForSide(y - 1, numRabbitsY);

            // Figure out how many ways we can split remaining rabbits between two sides
            BigInteger combinations = combinations(n - 1, numRabbitsX);

            count = count.add(xPermutations.multiply(yPermutations).multiply(combinations));
        }

        return count.toString();
    }

    public static BigInteger permutationsForSide(int numVisible, int numRabbits) {
        if (sStoredResults.containsKey(numVisible)) {
            Map<Integer, BigInteger> results = sStoredResults.get(numVisible);
            if (results.containsKey(numRabbits)) {
                return results.get(numRabbits);
            }
        }

        // Base cases
        if (numVisible > numRabbits) {
            // Impossible to solve
            return BigInteger.ZERO;
        }
        else if (numVisible == numRabbits) {
            // Only one solution: all rabbits in order, from smallest to largest
            return BigInteger.ONE;
        }

        // Split the problem into a smaller problem!
        // 1. Take the tallest rabbit and iterate its position in the line
        // 2. Figure out # of combinations of rabbits on left vs. right of tallest rabbit
        // 3. Figure out # of permutations of rabbits on unseen side of tallest rabbit
        // 4. Figure out # of permutations on seen side of tallest rabbit by recursion
        // 5. Combine all results: (# combinations) * (# permutations seen) * (# permutations unseen)
        BigInteger count = BigInteger.ZERO;
        for (int tallestPosition = 0; tallestPosition < numRabbits; tallestPosition++) {
            // Stored for simplicity
            int numSeenRabbits = tallestPosition;
            int numUnseenRabbits = numRabbits - numSeenRabbits - 1;

            // Number of ways we can divide rabbits between seen/unseen side of tallest rabbit
            BigInteger combinations = combinations(numRabbits - 1, numSeenRabbits);

            // Number of ways we can permute unseen rabbits - simple, since any order is legit
            BigInteger unseenPermutations = sFactorials.calculate(numUnseenRabbits);

            // Number of ways we can permute seen rabbits
            BigInteger seenPermutations = permutationsForSide(numVisible - 1, numSeenRabbits);

            // Add it all to the count
            count = count.add(combinations.multiply(unseenPermutations).multiply(seenPermutations));
        }

        // Store the result
        if (!sStoredResults.containsKey(numVisible)) {
            sStoredResults.put(numVisible, new HashMap<Integer, BigInteger>());
        }

        sStoredResults.get(numVisible).put(numRabbits, count);

        return count;
    }

    static BigInteger combinations(int numElements, int numChosen) {
        BigInteger nFact = sFactorials.calculate(numElements);
        BigInteger kFact = sFactorials.calculate(numChosen);
        BigInteger nMinusKFact = sFactorials.calculate(numElements - numChosen);
        return nFact.divide(kFact.multiply(nMinusKFact));
    }

    // Class that caches the values of Factorials, just so we don't have to worry
    // about efficiency so much. (Since our max input is 40, not much is stored.)
    static class Factorials {
        Map<Integer, BigInteger> cache = new HashMap<>();

        BigInteger calculate(int in) {
            if (!cache.containsKey(in)) {
                BigInteger result = BigInteger.ONE;
                for (int a = 2; a <= in; a++) {
                    result = result.multiply(BigInteger.valueOf(a));
                }
                cache.put(in, result);
            }

            return cache.get(in);
        }
    }
}
