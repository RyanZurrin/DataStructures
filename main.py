import string_matching
# import library to time the execution time of the algorithm
import timeit

# test the time taken by the algorithm
def test_time(algorithm, text, pattern):
    print(algorithm.__name__, timeit.timeit(lambda: algorithm(text, pattern), number=1000))

# test the algorithm on the given text and pattern
print(string_matching.brute_force('acbcabccababcaacbcac', 'acbcac'))
test_time(string_matching.brute_force, 'acbcabccababcaacbcac', 'acbcac')


print(string_matching.rabin_karp('acbcabccababcaacbcac', 'acbcac'))
test_time(string_matching.rabin_karp, 'acbcabccababcaacbcac', 'acbcac')


print(string_matching.knuth_morris_pratt('acbcabccababcaacbcac', 'acbcac'))
test_time(string_matching.knuth_morris_pratt, 'acbcabccababcaacbcac', 'acbcac')