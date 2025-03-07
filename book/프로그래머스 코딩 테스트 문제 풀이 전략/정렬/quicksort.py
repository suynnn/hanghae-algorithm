sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]


def quickSort(data, low, high):
    p = data[(low + high) // 2]
    left, right = low, high

    while True:
        while data[left] < p:
            left += 1

        while data[right] > p:
            right -= 1

        if left >= right:
            break

        data[left], data[right] = data[right], data[left]

    if low < right:
        quickSort(data, low, right)

    if left < high:
        quickSort(data, right + 1, high)


def quicksort2(data):
    if len(data) <= 1:
        return data
    pivot, others = data[0], data[1:]

    left = [item for item in others if pivot > item]
    right = [item for item in others if pivot < item]

    return [*quicksort2(left), pivot, *quicksort2(right)]


# quickSort(sample, 0, len(sample)-1)
# print(sample)
print(quicksort2(sample))