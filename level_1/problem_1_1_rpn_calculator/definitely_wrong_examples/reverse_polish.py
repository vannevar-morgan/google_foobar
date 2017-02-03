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
    
    return generate_rpn(parse_op_seq(op_seq, numbers, ops))


def generate_rpn(num_stack, ops_stack):
    """
    Generates a reverse polish notation string representing an operation sequence
    defined by num_stack and ops_stack.

    e.g.,
    Inputs: (2 lists of strings)
             num_stack = ["2", "3"]
             ops_stack = ["+"]
    Output: (list of strings) "23+"

    Note that num_stack and ops_stack are assumed to be output from parse_op_seq,
    i.e., they only contain valid numbers and defined operations.
    """
    rpn_stack = []
    rpn_stack.append(num_stack.pop(0))
    rpn_stack.append(num_stack.pop(0))
    rpn_stack.append(ops_stack.pop(0))
    for symbol in ops_stack:
        if symbol == "*":
            rpn_stack.pop(
    
    

def parse_op_seq(op_seq, numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"], ops = ["*", "+"]):
    """
    Parses a sequence of addition and multiplication operations into stacks of numbers and operations.

    e.g.,
    Inputs: (string) (optional, list of strings of valid values) (optional, list of strings of defined operations)
             op_seq = "2+3"
    
    Output: (list of strings) (list of strings)
             num_stack = ["2", "3"]
             ops_stack = ["+"]
    """
    num_stack = [] # numbers in the sequence stack
    ops_stack = [] # operations in the sequence stack
    
    if len(op_seq) == 0 or op_seq[0] in ops:
        raise ValueError("specified operation sequence is ill-formatted (begins with operation)...")
    
    for symbol in op_seq:
        if symbol in numbers:
            num_stack.append(symbol)
        elif symbol in ops:
            ops_stack.append(symbol)
        else:
            raise ValueError("specified operation sequence contains an undefined operation...")

    return [num_stack, ops_stack]

