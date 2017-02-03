def answer(digest):
    """
    Finds the password to open Professor Boolean's door.

    Given a known hashing algorithm:
        digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256
        message[-1] = 0
    And hashes produced by the algorithm:
        digest
    Return the messages which produced the hashes.

    Input:
       digest (list of 16 ints 0-255)
    Output:
       messages (list of 16 ints 0-255)
    """
    """
       My Notes:
          start at digest 0:
             given the hashing algorithm, message[-1] = 0, and the digests,
             find message[0] by:
                making digests for all possible message[0]'s
                select the message that produced that digest.
          repeat for all digest values
    """
    # Note that I am not handling possible collisions, based on experimenting in repl.
    messages = []
    prev_message = 0
    for i in range(0, len(digest)):
        new_digest = {}
        for message in range(0, 256): # for each possible message value, calculate the digest value...
            new_digest[((129 * message) ^ prev_message) % 256] = message
        
        # Find the message value that produced the digest value.
        prev_message = new_digest[digest[i]]
        messages.append(prev_message)
        
    return messages

#digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256
#message[-1] is 0
