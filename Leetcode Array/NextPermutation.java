/*# 31. Next Permutation
# Medium
# Topics
# Companies
# A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

# For example, the next permutation of arr = [1,2,3] is [1,3,2].
# Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
# While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
# Given an array of integers nums, find the next permutation of nums.

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,18]

    
        #Brute force
        #Generate all combinations
        #Do a linear search
        #Next Index Permutation is returned as answer

        #Optimal
        #longer Prefix Match
        #a[i]<a[i+1]
        #After finding break point find greater than a[i] but smaller than every remaining 
        #Try and place them in ascending sorted order for the remaining
        #If no dip u can reverse the array and return answer*/

class NextPermutation {

    public static void main(String[] args)
    {
        int nums[]= {1,3,2};
        NextPermutation n = new NextPermutation();
        n.nextpermutation(nums);
        for(int i=0;i<nums.length;i++)
            System.out.print(nums[i]+ " ");
        System.out.println();
        return;
    } 

    public void nextpermutation(int[] nums)
    {
    int index=-1;
    int temp=0;
    int n=nums.length;
    for(int i=n-2;i>=0;i--)
    {
        if(nums[i]<nums[i+1])
        {
            index=i;
            break;
        }

    }
    if(index==-1)
    {
        reverse(nums,0);
        return;
    }
    for(int i=n-1;i>=index;i--)
    {
        if(nums[i]>nums[index])
        {
            temp=nums[i];
            nums[i]=nums[index];
            nums[index]=temp;
            break;
        }
    }
    reverse(nums,index+1);
    return;
    }

    void reverse(int[] arr,int index)
    {
        int start = index;
        int end = arr.length - 1;

        while (start < end) {
            // Swap elements at start and end
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            // Move indices towards the center
            start++;
            end--;
        }
    }
}
