# string matching algorithms

# brute force algorithm

def brute_force(text, pattern):
    """
    brute force algorithm
    """
    l1 = len(text)
    l2 = len(pattern)
    i = 0
    j = 0
    flag = False
    while i < l1:
        j = 0
        count = 0
        while j < l2:
            if i + j < l1 and text[i + j] == pattern[j]:
                count += 1
            j += 1
        if count == l2:
            return i
        i += 1
    if not flag:
        return -1


# The Rabin-Karp algorithm
def generate_hash(text, pattern):
    ord_text = [ord(i) for i in
                text]
    ord_pattern = [ord(j) for j in
                   pattern]
    len_text = len(text)
    len_pattern = len(pattern)
    len_hash_array = len_text - len_pattern + 1
    hash_text = [0] * (
        len_hash_array)
    hash_pattern = sum(ord_pattern)
    for i in range(0,
                   len_hash_array):
        if i == 0:  # Base condition
            hash_text[i] = sum(
                ord_text[:len_pattern])
        else:
            hash_text[i] = ((hash_text[i - 1] - ord_text[i - 1]) + ord_text[
                i + len_pattern - 1])
    return [hash_text, hash_pattern]


def rabin_karp(text, pattern):
    text = str(text)
    pattern = str(pattern)
    hash_text, hash_pattern = generate_hash(text, pattern)
    len_text = len(text)
    len_pattern = len(pattern)
    flag = False
    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern:
            count = 0
            for j in range(len_pattern):
                if pattern[j] == text[i + j]:
                    count += 1
                else:
                    break
            if count == len_pattern:
                return i
    return -1


def pfun(pattern):  # function to generate prefix function for the given pattern
    n = len(pattern)  # length of the pattern
    prefix_fun = [0] * (n)  # initialize all elements of the list to 0
    k = 0
    for q in range(2, n):
        while k > 0 and pattern[k + 1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k + 1] == pattern[
            q]:  # If the kth element of the pattern is equal to the qth element
            k += 1  # update k accordingly
        prefix_fun[q] = k
    return prefix_fun  # return the prefix function


def KMP_Matcher(text, pattern):  # KMP matcher function
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-' + text  # append dummy character to make it 1-based indexing
    pattern = '-' + pattern  # append dummy character to the pattern also
    prefix_fun = pfun(pattern)  # generate prefix function for the pattern
    q = 0
    for i in range(1, m + 1):
        while q > 0 and pattern[q + 1] != text[
            i]:  # while pattern and text are not equal, decrement the value of q if it is > 0
            q = prefix_fun[q]
        if pattern[q + 1] == text[
            i]:  # if pattern and text are equal, update value of q
            q += 1
        if q == n:  # if q is equal to the length of the pattern, it means that the pattern has been found.
            print("Pattern occours with shift",
                  i - n)  # print the index, where first match occours.
            flag = True
            q = prefix_fun[q]
    if not flag:
        print('\nNo match found')
