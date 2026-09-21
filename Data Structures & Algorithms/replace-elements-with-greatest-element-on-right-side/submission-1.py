class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        rightmax = -1
        ans = [0] * n
        for i in range(len(arr) -1 , -1 ,-1):
            ans[i] = rightmax
            rightmax = max(arr[i] , rightmax)
        return ans
            



        

