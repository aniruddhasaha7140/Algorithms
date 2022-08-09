#O(N^2) time complexity
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    temp=nums[j]
                    nums[j]=nums[i]
                    nums[i]=temp
                    
        return nums[k-1]

#O(N) time complexity
#Use Heap