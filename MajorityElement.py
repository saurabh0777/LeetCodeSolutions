from typing import List
import time

class Solution:

  # approch 1:

    def majorityElementAp1(nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return (nums[n//2])
    def majorityElement(nums: List[int]) -> int:
        record_count = 0
        major_element= nums[1]

        for i in nums:
            curr_count = nums.count(i)
            if curr_count>record_count:
                record_count =curr_count
                major_element = i

        return major_element


    start_time = time.time()
    ele  = majorityElement([2,2,1,1,1,2,2,2,1,1,1,2,0,2,2,1,1,1,2,2,2,1,1,1,2,2,2,1,1,1,2,2,2,1,1,1,2,0,2,2,1,1,1,2,2,2,1,1,1,2])
    print(ele)
    end_time = time.time()
    time_taken = start_time-end_time
    print(f"total time in brute force {time_taken} seconds")
    start_time = time.time()
    element_using_ap1 = majorityElement([2,2,1,1,1,2,2,2,1,1,1,2,0,2,2,1,1,1,2,2,2,1,1,1,2,2,2,1,1,1,2,2,2,1,1,1,2,0,2,2,1,1,1,2,2,2,1,1,1,2])
    end_time = time.time()
    time_taken = start_time - end_time
    print(element_using_ap1)
    print(f"total time in optimized approach {time_taken} seconds")


