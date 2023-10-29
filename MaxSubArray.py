from typing import List

class solution:

    def maxSubArray(self,nums:List[int])-> int:
        maxsub = nums[0]
        currsum = 0
        for i in nums:
            if currsum <0:
                currsum = 0

            currsum += i
            maxsub = max(currsum,maxsub)

        return maxsub

d = solution()
out = d.maxSubArray([100,-3,100])
print(out)
