import sys
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
input_data = sys.stdin.read().splitlines()
nums = list(map(int, input_data[0].split()))
target = int(input_data[1])
sol = Solution()
result = sol.search(nums, target)
print(result)
