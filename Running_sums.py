''' Running sum of 1d array '''
class Solution:
    def runningSums(self, nums: list[int]):
        st = [0]*len(nums)
        for i in range(len(nums)):
            if i == 0:
                st[i] = nums[i]
            else:
                st[i] = st[i-1] + nums[i]
        return st
am = Solution()
lst = [1,2,3,10,1,7,8]
print(am.runningSums(lst))
