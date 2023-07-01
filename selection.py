# selection algorithms
import sorting as s


def quick_select(arr, start, end, k):
    split = s.partition(arr, start, end)
    if split == k:
        return arr[split]
    elif split < k:
        return quick_select(arr, split + 1, end, k)
    else:
        return quick_select(arr, start, split - 1, k)


def deterministic_select(arr, start, end, k):
    if start == end:
        return arr[start]
    split = s.partition(arr, start, end)
    if split == k:
        return arr[split]
    elif split < k:
        return deterministic_select(arr, split + 1, end, k)
    else:
        return deterministic_select(arr, start, split - 1, k)


def median_of_medians(elems):
    sublists = [elems[i:i + 5] for i in range(0, len(elems), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    if len(medians) <= 5:
        return sorted(medians)[len(medians) // 2]
    else:
        return median_of_medians(medians)
