from typing import List
def maxProdSubarr(arr:List[int])-> List[int]:
    maxsofar =arr[0]
    currentprod = arr[0]

    for i in range(1,len(arr)):
        currentprod = i*i-1
        if currentprod <= maxsofar:
            maxsofar =0



