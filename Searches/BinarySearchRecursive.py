def BinarySearchRecur(nums, l, r, x):
    """
    :type nums: List[int]
    :type x: int
    :rtype: int
    """
    # base condition
    if r < l:
        return -1
    else:
        mid = l + (r - l) // 2
        if x == mid:
            return mid
        elif x > mid:
            BinarySearchRecur(nums, mid+1, r, x)
        else:
            BinarySearchRecur(nums, l, mid-1, x)


if __name__ == "__main__":
    nums = [1, 2, 6, 9, 12, 14]
    print(BinarySearchRecur(nums, 0, len(nums)-1, 12))
