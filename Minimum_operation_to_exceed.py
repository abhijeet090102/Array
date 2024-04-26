''' minimum operation to exceed threshold value I '''
class Solution:
    def minOperat(self, nums: list[int], k: int):
        count = 0
        for i in range(len(nums)):
            if nums[i] < k:
                count += 1
        return count
ma = Solution()
lst = [2,11,10,1,3,14,6,8]
k = 10
print(ma.minOperat(lst,k))
