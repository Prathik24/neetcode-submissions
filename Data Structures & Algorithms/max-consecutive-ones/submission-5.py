class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxstreak = 0
        for num in nums:
            if num == 1:
                counter += 1 
                maxstreak = max(maxstreak ,counter)
            else :
                counter = 0 
                 
        return maxstreak
        