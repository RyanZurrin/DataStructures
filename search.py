# different search algorithms

def linear_search(arr, target, ordered=False):
    """linear_search

    Parameters
    ----------
    arr : list
        list to be searched
    target : int
        target to be searched
    ordered : bool, optional
        if the list is ordered, set to True, by default False

    Returns
    -------
    int
        index of the target, if found, otherwise None
    """
    for i in range(len(arr)):
        if ordered and arr[i] > target:
            return None
        elif ordered and arr[i] == target or not ordered and arr[i] == target:
            return i
    return None


def jump_search(ordered_list, target):
    """jump_search. Requires the list to be sorted.

    Parameters
    ----------
    ordered_list : list
        list to be searched
    target : int
        target to be searched

    Returns
    -------
    int
        index of the target, if found, otherwise None
    """
    import math
    list_size = len(ordered_list)
    block_size = math.sqrt(list_size)
    i = 0
    while i != len(ordered_list) - 1 and ordered_list[i] <= target:
        if i + block_size > len(ordered_list):
            block_size = len(ordered_list) - i
            block_list = ordered_list[i:i + block_size]
            j = linear_search(block_list, target, ordered=True)
            if j is None:
                return
            return i + j
        if ordered_list[i + block_size] == target:
            return i + block_size - 1
        elif ordered_list[i + block_size - 1] > target:
            block_array = ordered_list[i:i + block_size - 1]
            j = linear_search(block_array, target, ordered=True)
            if j is None:
                return
            return i + j
        i += block_size


def binary_search(ordered_list, target):
    """
    binary search
    """
    left = 0
    right = len(ordered_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if ordered_list[mid] == target:
            return mid
        elif ordered_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def nearest_min(input_list, low_index, upper_index, search_value):
    """nearest_min
    """
    mid = low_index + (((upper_index - low_index) / (input_list[upper_index] -
                                                     input_list[low_index])) * (
                                   search_value -
                                   input_list[low_index]))
    return int(mid)


def interpolation_search(ordered_list, target):
    """interpolation search
    """
    low_index = 0
    upper_index = len(ordered_list) - 1
    while low_index <= upper_index:
        mid_point = nearest_min(ordered_list, low_index, upper_index, target)
        if mid_point > upper_index or mid_point < low_index:
            return None
        if ordered_list[mid_point] == target:
            return mid_point
        if target > ordered_list[mid_point]:
            low_index = mid_point + 1
        else:
            upper_index = mid_point - 1
    return None
