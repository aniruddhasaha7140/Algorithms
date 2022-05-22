# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version
# of your product fails the quality check. Since each version is developed based on the previous version,
# all the versions after a bad version are also bad. Suppose you have n versions [1, 2, ..., n] and you want to find
# out the first bad one, which causes all the following ones to be bad. You are given an API bool isBadVersion(
# version) which returns whether version is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# Just defining to make the program run

def isBadVersion(i):
    if i >= 15:
        return True
    else:
        return False


def firstBadVersion(n):
    """
    :type n: int
    :rtype: int
    """
    left = 1
    right = n
    badIndex = -1
    while left <= right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            badIndex = mid
            right = mid - 1
        else:
            left = mid + 1
    return badIndex


if __name__ == "__main__":
    print(firstBadVersion(100))
