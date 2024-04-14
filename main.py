class Solution:
    def solution(self, mas):
        res = []
        def backtrack(nums):
            if len(nums) == len(mas):
                res.append(nums[:])
                return
            for num in mas:
                if num not in nums:
                    nums.append(num)
                    backtrack(nums)
                    nums.pop()
        backtrack([])
        return res

solution = Solution()

print(solution.solution([1, 2, 3]))
print(solution.solution([0, 1]))
print(solution.solution([]))