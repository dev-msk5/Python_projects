def quick_sort(ints:list):
    if len(ints) < 2:
        return ints[:]
    pivot = ints[0]
    bigger = [i for i in ints if i>pivot]
    equal = [i for i in ints if i==pivot]
    smaller = [i for i in ints if i<pivot]
    sorted_list = quick_sort(smaller) + equal + quick_sort(bigger)
    return sorted_list
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))
