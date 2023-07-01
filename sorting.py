# sorting algorithms

def bubble_sort(arr):
    """Bubble sort, worst-case: O(n^2), average: O(n^2), best-case: O(n)

    Parameters
    ----------
    arr : list
        The array to be sorted.

    Returns
    -------
    list
        The sorted array.
    """
    for _ in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    """Selection sort, worst-case: O(n^2), average: O(n^2), best-case: O(n^2)

    Parameters
    ----------
    arr : list
        The array to be sorted.

    Returns
    -------
    list
        The sorted array.
    """
    for i in range(len(arr)):
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insertion_sort(arr):
    """Insertion sort, worst-case: O(n^2), average: O(n^2), best-case: O(n)

    Parameters
    ----------
    arr : list
        The array to be sorted.

    Returns
    -------
    list
        The sorted array.
    """
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
    return arr


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(arr):
    """Merge Sort, worst-case: O(n log n), average: O(n log n), best-case: O(n)

    Parameters
    ----------
    arr : list
        The array to be sorted.

    Returns
    -------
    list
        The sorted array.
    """
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(i, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    """Quick Sort, worst-case: O(n^2), average: O(n log n), best-case: O(n log n)

    Parameters
    ----------
    arr : list
        The array to be sorted.
    low : int
        The lower bound of the array.
    high : int
        The upper bound of the array.

    Returns
    -------
    list
        The sorted array.
    """
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)
    return arr


def tim_sort(arr, run):
    """Tim Sort, wost-case: O(n log n), average: O(n log n), best-case: O(n)

    Parameters
    ----------
    arr : list
        The array to be sorted.
    run : int
        The size of the run.

    Returns
    -------
    list
        The sorted array.
    """
    for x in range(0, len(arr), run):
        arr[x:x + run] = insertion_sort(arr[x:x + run])

    run_size = run
    while run_size < len(arr):
        for x in range(0, len(arr), 2 * run_size):
            arr[x:x + 2 * run_size] = merge(arr[x:x + run_size],
                                            arr[x + run_size:x + 2 * run_size])
        run_size *= 2
    return arr
