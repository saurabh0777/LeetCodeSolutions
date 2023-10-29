def maxSumArray(arr)->int:
    maxsofar = arr[0]
    currentsum = arr[0]

    for i in range(len(arr)):
        if (currentsum<0):
            currentsum =0

        currentsum += arr[i]

        if (currentsum> maxsofar):
            maxsofar = currentsum


    return maxsofar


out = maxSumArray([-2,1,-3,4,-1,2,1,-5,4])

print(out)