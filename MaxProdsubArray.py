from typing import List

## We have to calculate the prod from left to right 
def maxProd(arr:List[int])->List[int]:

    if len(arr)==1:
        return arr

    ans =0
    current_product =1
    for i in arr:
        if i!=0:
            current_product = i*current_product
            ans = max(ans,current_product)
        else:
            current_product=0

    current_product=1
    for i in range(len(arr)-1,-1,-1):
        if arr[i]!=0:
            current_product=current_product*arr[i]
            ans = max(current_product,ans)
        else:
            current_product =1

    return ans

out = maxProd([-1,-2,-3,0])
print(out)

