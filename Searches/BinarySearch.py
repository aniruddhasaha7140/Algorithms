def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    check = 0
    l = 0
    r = len(nums)-1
    while l <= r:
        # But if we calculate the middle index like this means our code is not 100 % correct, it contains bugs. That
        # is, it fails for larger values of int variables low and high.Specifically, it fails if the sum of low and
        # high is greater than the maximum positive int value(2^31 – 1 ).
        # The sum overflows to a negative value and the value stays negative when divided by 2.
        # In java, it throws ArrayIndexOutOfBoundException.

        # mid = (r + l) // 2
        mid = l + (r - l) // 2
        if target > nums[mid]:
            l = mid + 1
        elif target < nums[mid]:
            r = mid - 1
        else:
            check += 1
            break
    if check == 0:
        return -1
    else:
        return mid


if __name__ == "__main__":
    nums = [1, 2, 6, 9, 12, 14]
    print(search(nums, 12))
