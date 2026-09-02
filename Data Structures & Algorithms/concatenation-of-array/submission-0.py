class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums = 2 * nums
        ans =  nums 

        for i in range(len(nums)):
            ans[i] = nums[i]
        return ans

        