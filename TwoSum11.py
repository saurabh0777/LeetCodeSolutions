from typing import List
# Array is starting from 1 index and it is sorted . We are solving this with 2 pointer approach.
# we need to find the elements whoes sum is equal to the target value
class solution:

    def twoSum(arr:List[int],target)->List[int]:
        start = 0
        last = len(arr)-1
        final_out =[]
        while(start<last):
            currentSum = arr[start] + arr[last]
            if (currentSum<target):
                start = start+1
            elif(currentSum>target):
                last = last -1
            else:
                final_out.append(start+1)
                final_out.append(last+1)
                break

        return final_out

    numbers = [2, 7, 11, 15]
    target = 9

    out = twoSum(numbers,target)
    print(out)

