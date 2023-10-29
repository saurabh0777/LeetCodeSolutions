def max_prd_three(arr):
    arr.sort()
    print(arr)
    return max(arr[0]*arr[1]*arr[-1],arr[-1]*arr[-2]*arr[-3])

print(max_prd_three([0,10,-10,100,-1,5]))