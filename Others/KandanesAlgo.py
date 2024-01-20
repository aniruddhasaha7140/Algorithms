def max_subarray():

    arr = [-2,-3,-4,-1,-2,1,5,3]
    n=len(arr)
    
    for i in range(0,n):
        for j in range(i,n):
            sum=0
            sum+=arr[j]
        maximum=max(maximum,sum)

    return maximum

def main():
    max=max_subarray
    print(max)
    