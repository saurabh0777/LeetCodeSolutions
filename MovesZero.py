from typing import List
class Solution:
    # Optimal approach is to swap the element element which are non zero should move to left side
    def moveZeroes_optimal(nums: List[int]) -> List[int]:
     start_point =0
     for i in range(len(nums)):
         if (nums[i] !=0):
             nums[i],nums[start_point]= nums[start_point], nums[i]
             start_point +=1
     return nums




    def moveZeroes(nums: List[int]) ->  List[int]:
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)

        count_of_zero = nums.count(0)
        for i in range(count_of_zero):
            temp.append(0)

        return temp


    output = moveZeroes([0,0,1])
    print(output)
    output1 = moveZeroes_optimal([0, 0, 1])
    print(output1)