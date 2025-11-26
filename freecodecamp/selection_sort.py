def selection_sort(items:list):
    for i in range(len(items)-1):
        tmp = items[i]
        minimum = min(items[i:])
        min_index = i
        for num, val in enumerate(items[i:]):
            if val == minimum:
                min_index = i + num
                break
        items[i] = minimum
        items[min_index] = tmp
        # print(items)
    return items
# print(selection_sort([33, 1, 89, 2, 67, 245]))