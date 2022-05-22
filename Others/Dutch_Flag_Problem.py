def dutch_flag_problem(num, pivot=1):
    i = 0
    j = 0
    k = len(num) - 1

    while j <= k:
        if num[j] < pivot:
            swap(num, i, j)
            i += 1
            j += 1
        elif num[j] > pivot:
            swap(num, j, k)
            k = k - 1
        else:
            j = j + 1


def swap(num, x, y):
    num[x], num[y] = num[y], num[x]


if __name__ == '__main__':
    num = [2, 1, 2, 1, 0, 0, 0]

    dutch_flag_problem(num)
    print(num)
