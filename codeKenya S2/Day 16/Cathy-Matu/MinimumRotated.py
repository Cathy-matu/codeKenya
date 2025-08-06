from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than the rightmost, min is on the right side
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Min is at mid or in the left half
                right = mid
        
        # Left will point to the minimum
        return nums[left]


sol = Solution()
print(sol.findMin([3,4,5,6,1,2]))   #
print(sol.findMin([4,5,0,1,2,3]))   
print(sol.findMin([4,5,6,7]))       
