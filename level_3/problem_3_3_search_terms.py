#! /usr/bin/env python3

def answer(document, searchTerms):
    """
    Returns the shortest snippet of the document containing all search terms.
    
    Search terms can appear in any order in the snippet returned.

    Inputs:
       document is assumed to be a string consisting of lowercase letters [a-z] and spaces.
          -words in the document are separated by single spaces.
          -words can appear multiple times in the document.
          -The document is assumed guaranteed to contain all search terms.
       searchTerms is a list of words comprised of lowercase letters [a-z]
          -all search terms are distinct.
          -a search term must be an exact match to a word in the document to be considered a match
             -e.g., "hop" != "hopping"

    Outputs:
       (string) The shortest snippet of the document containing all search terms.

       The length of a snippet is the number of words in the snippet.

       If two snippets have the same length, the first snippet is returned.
          -e.g., given document = "world there hello hello where world"
                 and searchTerms = ["hello", "world"]
                 the snippet returned is "world there hello"

    """
    docText = document.strip().split(" ")

    snippets = []
    # For all words in the document text, check if the word is a search term.
    for i in range(0, len(docText)):
        word = docText[i]
        if word in searchTerms:
            # If the word is a search term, find the snippet that contains all search terms,
            # in the substring starting from this word to the end of the document.
            last_term_index = 0
            for term in searchTerms:
                # Look for the search term in the substring of the document text.
                #    -Find the index of the last term in the substring -> this is the end of the snippet.
                #    -If a search term is not found in the substring then the substring cannot have a snippet.
                try:
                    term_index = docText[i::].index(term)
                    last_term_index = max(last_term_index, term_index)
                except ValueError as e:
                    last_term_index = -1
                    break
            if last_term_index < 0:
                # There can be no more snippets in the substring because not all search terms are present in the substring.
                break
            else:
                # Create the snippet from the substring using the two search term indexes we've found.
                # Add the snippet to the list of snippets we've found so far.
                last_term_index += i
                snippet = word
                for text in docText[i+1:last_term_index+1]:
                    snippet += (" " + text)
                snippets.append(snippet)

    #return snippets
    min_snippet_length = len(snippets[0]) # note that I am assuming a snippet was found, valid since all search terms are guaranteed to be in the document text...
    min_snippet_index = 0
    for i in range(1, len(snippets)):
        if len(snippets[i]) < min_snippet_length:
            min_snippet_length = len(snippets[i])
            min_snippet_index = i

    return snippets[min_snippet_index]
