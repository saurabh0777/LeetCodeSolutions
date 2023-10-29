from typing import List

def colorsort(arr:List[int])->List[int]:
    zero =0
    one =0
    two =0
    out = []

    for i in arr:
        if i ==0:
            zero +=1
        if i ==1:
            one +=1
        if i ==2:
            two +=1

    print("value count of ",zero,one,two)

    for i in range(len(arr)):
        if zero !=0:
            arr[i] = 0
            zero -=1

        elif one !=0:
            arr[i] =1
            one -=1
        else:
             arr[i] = 2
             two -=1

    print(arr)




colorsort([0,1,0,1,0,2,2])


