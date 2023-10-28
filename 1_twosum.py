class Solution:
    def twoSum(self, nums, target):
        solution = []
        loop_break = 0
        for base in range(0, len(nums)):
            for i in range(0, len(nums)):
                if nums[base] + nums[i] == target:
                    if base != i:
                        solution.append(base)
                        solution.append(i)
                        loop_break = 1
                
                if loop_break:
                    break
            if loop_break:
                break

        return solution