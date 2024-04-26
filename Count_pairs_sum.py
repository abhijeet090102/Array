''' Counts pairs whose sum is less than target '''
class Solution:
    def countPairs(self, nums: list[int], target: int):
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i < j and nums[i] + nums[j] < target:
                    count += 1
        return count
am = Solution()
lst = [-6,2,5,-2,6,8,-5,9]
ts = 0
print(am.countPairs(lst,ts))
