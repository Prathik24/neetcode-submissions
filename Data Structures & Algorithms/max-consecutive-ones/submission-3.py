class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_streak = 0
        for num in nums:
            if num == 1:
                counter += 1
            else :
                max_streak = max(max_streak, counter)
                counter = 0
        max_streak = max(max_streak, counter)
        return max_streak
        