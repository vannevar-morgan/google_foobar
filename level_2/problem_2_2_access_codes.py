def answer(x):
    """
    Given a list of codes, x, returns the unique codes.
    Two codes are considered to be "identical" (not unique) if they're exactly the same, or the same but reversed.
    
    e.g., 
    Inputs: (string list) x = ["foo", "bar", "oof", "bar"]
    Output: (int) 2

    Inputs: (string list) x = ["x", "y", "xy", "yy", "", "yx"]
    Output: (int) 5
    """
    
    codes = list(set(x)) # get rid of duplicates
    
    """
    Count those codes that are unique, using a dict
    to exclude palindromes of previous codes.
    """
    flipped = {}
    unique_count = 0
    for code in codes:
        if not flipped.get(code):
            flipped[code[::-1]] = code
            unique_count += 1
    return unique_count
    
