from typing import List

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # if all integers are used up
            if first == n-1:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                nums[first], nums[i] = nums[i], nums[first]
                # use next integers to complete the permutations
                backtrack(first + 1)
                # backtrack
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        output = []
        backtrack()
        return output

class Solution:
    def permute(self, lst: List[int]) -> List[List[int]]:
        # If lst is empty then there are no permutations
        #if len(lst) == 0:
        #    return []
 
        # If there is only one element in lst then, only
        # one permutation is possible
        if len(lst) == 1:
            return [lst]
 
        # Find the permutations for lst if there are
        # more than 1 characters
 
        l = [] # empty list that will store current permutation
 
        # Iterate the input(lst) and calculate the permutation
        for i in range(len(lst)):
            m = lst[i]
 
        # Extract lst[i] or m from the list.  remLst is
        # remaining list
            remLst = lst[:i] + lst[i+1:]
 
        # Generating all permutations where m is first
        # element
            for p in self.permute(remLst):
                l.append([m] + p)
        return l

s=Solution()
print(s.permute([1,2,3]))

