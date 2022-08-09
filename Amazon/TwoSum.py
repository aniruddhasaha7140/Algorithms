from typing import List
dic={}
nums=[2,6,5,8,11]
target=14

def twoSum(nums: List[int], target: int) -> List[int]:
    for i,n in enumerate(nums):
        diff=target-n
        if diff in dic.keys():
            return [dic[diff],i]
        else:
            dic[n]=i

print(twoSum(nums,target))
    