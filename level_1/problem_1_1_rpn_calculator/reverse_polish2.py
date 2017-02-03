#! /usr/bin/env python3

def convert_to_rpn(op_seq):
    """
    Takes a string representing a sequence of addition and multiplication operations
    and returns a string representing the operation sequence in reverse polish notation.
    
    e.g.,
    Inputs: (string) str = "2*4*3+9*3+5"
    Output: (string) "243**93*5++"

    Numbers are assumed 0-9, only addition "+" and multiplication "*"
    """
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] # allowed numbers
    ops = ["*", "+"] # allowed operations

    # check for undefined symbols in the operation sequence
    for symbol in op_seq:
        if symbol not in numbers and symbol not in ops:
            raise ValueError("specified operation sequence contains an undefined symbol...\"" + symbol + "\"")

    # check for leading op condition
    if len(op_seq) > 0 and op_seq[0] in ops:
        raise ValueError("specified operation sequence is ill-formed (missing leading value)...")

    # check for trailing op condition
    if len(op_seq) > 0 and op_seq[len(op_seq) - 1] in ops:
        raise ValueError("specified operation sequence is ill-formed (missing trailing value)...")

    # check for balanced expressions
    for i in range(0, len(op_seq), 2):
        if op_seq[i] in ops:
            raise ValueError("specified operation sequence is ill-formed (unbalanced expression)...")

    for i in range(1, len(op_seq), 2): # assumes leading ops condition is checked
        if op_seq[i] not in ops:
            raise ValueError("specified operation sequence is ill-formed (unbalanced expression)...")
    
    # convert to reverse polish notation
    # basically I want to sort the string:
    #   "+" splits the string into blocks separated by "*"
    #   all "*" in a block move to the end of the block
    #   all "+" between blocks move to the end of the string
    rpn_string = ""
    
    mult_blocks = op_seq.split("+") # split into blocks of multiplication operations
    
    for mult_op in mult_blocks:
        nums = mult_op.split("*")
        for i in nums:
            rpn_string += str(i)
        op_string = "*" * (len(nums) - 1)
        rpn_string += op_string

    op_string = "+" * (len(mult_blocks) - 1)
    rpn_string += op_string

    return rpn_string
