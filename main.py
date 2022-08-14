import random

import sorting

# create an unsorted array of 40 random numbers between 1 and 100
arr = [random.randint(1, 100) for i in range(40)]
# print the unsorted array
print("Unsorted Array:", arr)

# sort the array using the bubble sort algorithm
sorted_arr = sorting.bubble_sort(arr.copy())
# print the unsorted array
print("Unsorted Array:", arr)
# print the sorted array
print("bubble_sort:", sorted_arr)
# print the unsorted array
print("Unsorted Array:", arr)
sorted_arr = sorting.selection_sort(arr.copy())
print("selection_sort:", sorted_arr)
# print the unsorted array
print("Unsorted Array:", arr)
sorted_arr = sorting.insertion_sort(arr.copy())
print("insertion_sort:", sorted_arr)
# print the unsorted array
print("Unsorted Array:", arr)
sorted_arr = sorting.merge_sort(arr.copy())
print("merge_sort:", sorted_arr)
# print the unsorted array
print("Unsorted Array:", arr)
sorted_arr = sorting.quick_sort(arr.copy(), 0, len(arr) - 1)
print("quick_sort:", sorted_arr)
# print the unsorted array
print("Unsorted Array:", arr)
sorted_arr = sorting.tim_sort(arr.copy(), 4)
print("tim_sort:", sorted_arr)



