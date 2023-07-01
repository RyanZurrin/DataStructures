# string matching algorithms

# brute force algorithm
def brute_force(text, pattern):
    return next(
        (
            i
            for i in range(len(text) - len(pattern) + 1)
            if text[i : i + len(pattern)] == pattern
        ),
        -1,
    )


# rabin karp algorithm
def rabin_karp(text, pattern):
    # use built-in hash function to get the hash value of the pattern
    pattern_hash = hash(pattern)
    # use built-in hash function to get the hash value of the text
    text_hash = hash(text[:len(pattern)])
    # loop through all the possible starting points in the text
    for i in range(len(text) - len(pattern) + 1):
        # check if the current substring in the text is the same as the pattern
        if text_hash == pattern_hash and text[i:i + len(pattern)] == pattern:
            return i
        # get the hash value of the next substring in the text
        text_hash = hash(text[i + 1:i + 1 + len(pattern)])
    return -1


def prefix_function(pattern):
    pf = [0] * len(pattern)
    pf[0] = 0
    k = 0
    for q in range(1, len(pattern)):
        while k > 0 and pattern[k] != pattern[q]:
            k = pf[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pf[q] = k
    return pf


def knuth_morris_pratt(text, pattern):
    pf = prefix_function(pattern)
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = pf[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == len(pattern):
            return i - len(pattern) + 1
    return -1
