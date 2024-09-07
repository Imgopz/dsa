# import numpy as np
# from collections import Counter
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # nums.sort()
        # return any(nums[i] == nums[i+1] for i in range(len(nums)-1))

        # return len(Counter(nums)) != len(nums)

        # return len(np.unique(nums)) != len(nums)

        # seen = set()
        # for num in nums:
        #     if num in seen:
        #         return True
        #     seen.add(num)
        # return False


        # bit_vector = 0
        # for num in nums:
        #     mask = 1 << num
        #     if bit_vector & mask:
        #         return True
        #     bit_vector |= mask
        # return False


        # return len(nums) != len(set(nums))


        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        
        return False


listArray = [[1,2,3,1],[1,2,3,4],[1,1,1,3,3,4,3,2,4,2]]

for la in listArray:
    sol = Solution()
    print(sol.containsDuplicate(la))