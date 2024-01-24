# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         for i in range(len(nums) - 1):
#             diff = nums[i + 1] - nums[i]
#             if diff <= 0:
#                 return nums[i + 1]

#         return nums[0]  # no negative diff -> first element is smallest


"""
Using Binary Search Solution
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]  # left ptr == right ptr
