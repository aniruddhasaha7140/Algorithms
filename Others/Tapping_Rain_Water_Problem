# min(MaxLeft,MaxRight)-height at index

def trapping_water_problem(heights):
    if len(heights) < 3:
        return

    left_max = [0 for _ in range(len(heights))]
    right_max = [0 for _ in range(len(heights))]

    # dealing with the left max values
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i - 1], heights[i - 1])

    # dealing with the right max values
    for i in range(len(heights) - 2, -1, -1):
        right_max[i] = max(left_max[i + 1], heights[i + 1])

    print(left_max)
    print(right_max)
    trapped_water = 0
    # consider all the items in O(N) and sum up the trapped rain water
    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped_water += min(left_max[i], right_max[i]) - heights[i]

    print(trapped_water)


if __name__ == '__main__':
    heights = [0, 3, 2, 1, 2, 3, 0, 3]
    trapping_water_problem(heights)
