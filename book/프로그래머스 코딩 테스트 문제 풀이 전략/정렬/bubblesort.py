sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]


def bubbleSort(data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


bubbleSort(sample)

print(sample)