def bubbleSort(lis):
    length = len(lis)
    for i in range(length):
        for j in range(length - i):
            a = lis[j]
            b = lis[j + 1]
            if a > b:
                lis[j] = b
                lis[j + 1] = a
    return lis


if __name__ == "__main__":
    int_list = [6, 4, 3, 7, 6, 5, 3, 2]
    print(bubbleSort(int_list))
