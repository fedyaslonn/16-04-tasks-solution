class Solution:
    def jump_by_index(self, nums):
        index = 0
        while index < len(nums) - 1:
            if nums[index] == 0:
                return False
            index += nums[index]
        return index == len(nums) - 1

solution = Solution()
print(solution.jump_by_index([2, 3, 1, 1, 4]))
print(solution.jump_by_index([3, 2, 1, 0, 4]))
