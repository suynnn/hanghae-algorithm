sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]


def selectSort(data):
    for i in range(len(data)):
        idx = i

        for j in range(i+1, len(data)):
            if data[idx] > data[j]:
                idx = j

        data[i], data[idx] = data[idx], data[i]


selectSort(sample)
print(sample)